import sys
import os
import requests
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.properties import ObjectProperty, StringProperty
from kivy.lang import Builder
from kivy_garden.graph import Graph, LinePlot
import numpy as np
from login import LoginScreen  # Ensure LoginScreen is correctly imported

# Ensure the garden package path is added to sys.path
garden_path = os.path.join(os.path.expanduser("~"), ".kivy", "garden")
if garden_path not in sys.path:
    sys.path.append(garden_path)

# Define global variables for API URL and other constants
API_URL = "http://apps.openioe.in/openioe/api/"
DEVICE_ID = "9lpqiYnhjfesPnWTvi3l"
DATA_KEYS = ["Voltage", "Current", "Power", "Energy"]

class Dashboard(Screen):
    voltage = StringProperty("0")
    current = StringProperty("0")
    power = StringProperty("0")
    energy = StringProperty("0")

    def __init__(self, **kwargs):
        super(Dashboard, self).__init__(**kwargs)
        Clock.schedule_once(self.update_data, 1)  # Schedule initial data update
        Clock.schedule_interval(self.update_data, 10)  # Update data every 10 seconds

    def update_data(self, dt):
        try:
            response = requests.get(f"{API_URL}/showdevicejson/{DEVICE_ID}/164/182")
            if response.status_code == 200:
                data = response.json()
                for key in DATA_KEYS:
                    if key in data:
                        setattr(self, key.lower(), str(np.mean(data[key])))
                    else:
                        print(f"Key '{key}' not found in API response.")
            else:
                print(f"Failed to fetch data. Status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error fetching data: {e}")

class GraphScreen(Screen):
    graph_layout = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(GraphScreen, self).__init__(**kwargs)
        self.graph = Graph(
            xlabel='X',
            ylabel='Y',
            x_ticks_minor=5,
            x_ticks_major=1,
            y_ticks_major=10,
            y_grid_label=True,
            x_grid_label=True,
            padding=5,
            xlog=False,
            ylog=False,
            xmin=0,
            xmax=10,
            ymin=0,
            ymax=100,
            background_color=[0.9, 0.9, 0.9, 1],
            border_color=[0, 0, 0, 1]
        )
        self.plots = []  # Initialize list to store LinePlot instances
        Clock.schedule_once(self.add_graph_to_layout)

    def add_graph_to_layout(self, dt):
        if self.graph_layout:
            self.graph_layout.add_widget(self.graph)
            Clock.schedule_interval(self.update_data, 10)  # Update graph data every 10 seconds
        else:
            print("graph_layout is not initialized")

    def update_data(self, dt):
        try:
            response = requests.get(f"{API_URL}/showdevicejson/{DEVICE_ID}/164/182")
            if response.status_code == 200:
                data = response.json()
                self.plot_graph(data)
            else:
                print(f"Failed to fetch data. Status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error fetching data: {e}")

    def plot_graph(self, data):
        for plot in self.plots:
            self.graph.remove_plot(plot)
        self.plots.clear()

        colors = {
            "Voltage": [1, 0, 0, 1],
            "Current": [0, 1, 0, 1],
            "Power": [0, 0, 1, 1],
            "Energy": [1, 1, 0, 1]
        }
        
        for key, value in data.items():
            if key in DATA_KEYS and isinstance(value, list):
                x = list(range(len(value)))
                y = [float(v) for v in value]
                plot = LinePlot(line_width=1.5, color=colors.get(key, [1, 1, 1, 1]))
                plot.points = list(zip(x, y))
                self.graph.add_plot(plot)
                self.plots.append(plot)
            else:
                print(f"Unexpected data format for '{key}'")

    def send_dummy_data(self, dt=None):
        data = {
            "Voltage": [np.random.randint(200, 250) for _ in range(10)],
            "Current": [np.random.uniform(2, 4) for _ in range(10)],
            "Power": [np.random.uniform(90, 100) for _ in range(10)],
            "Energy": [np.random.randint(60, 80) for _ in range(10)]
        }
        try:
            response = requests.post(f"{API_URL}/updatedevicejson/{DEVICE_ID}/164/182/", json=data)
            print(f"Status Code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error sending data: {e}")

class MyApp(App):
    def build(self):
        Builder.load_file('login.kv')
        Builder.load_file('my.kv')

        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(Dashboard(name='dashboard'))
        sm.add_widget(GraphScreen(name='graph'))
        return sm

if __name__ == '__main__':
    MyApp().run()

import sys
import os
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.properties import ObjectProperty, StringProperty
from kivy.lang import Builder
from kivy_garden.graph import Graph, LinePlot
import numpy as np
from login import LoginScreen  # Import LoginScreen from login.py

# Ensure the garden package path is added to sys.path
garden_path = os.path.join(os.path.expanduser("~"), ".kivy", "garden")
if garden_path not in sys.path:
    sys.path.append(garden_path)

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
            response = requests.get("http://apps.openioe.in/openioe/api/showdevicejson/9lpqiYnhjfesPnWTvi3l/164/182")
            if response.status_code == 200:
                data = response.json()
                self.voltage = str(np.mean(data["Voltage"]))
                self.current = str(np.mean(data["Current"]))
                self.power = str(np.mean(data["Power"]))
                self.energy = str(np.mean(data["Energy"]))
            else:
                print("Failed to fetch data")
        except Exception as e:
            print(f"Error fetching data: {e}")

class GraphScreen(Screen):
    graph_layout = ObjectProperty()

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
            ymax=100
        )
        self.graph_layout.add_widget(self.graph)
        self.plots = {}  # Keep track of plots and their labels
        Clock.schedule_interval(self.update_data, 10)  # Update data every 10 seconds

    def update_data(self, dt):
        try:
            response = requests.get("http://apps.openioe.in/openioe/api/showdevicejson/9lpqiYnhjfesPnWTvi3l/164/182")
            if response.status_code == 200:
                data = response.json()
                self.plot_graph(data)
            else:
                print("Failed to fetch data")
        except Exception as e:
            print(f"Error fetching data: {e}")

    def plot_graph(self, data):
        # Remove existing plots and labels
        for plot, label in self.plots.values():
            self.graph.remove_plot(plot)
            self.remove_widget(label)
        self.plots.clear()

        colors = {
            "Voltage": [1, 0, 0, 1],
            "Current": [0, 1, 0, 1],
            "Power": [0, 0, 1, 1],
            "Energy": [1, 1, 0, 1]
        }

        # Assuming 'data' is a dict with measurement names as keys and lists of values as values
        for key, value in data.items():
            if isinstance(value, list):  # Check if value is a list
                try:
                    x = list(range(len(value)))
                    y = [float(v) for v in value]
                    plot = LinePlot(line_width=1.5, color=colors.get(key, [1, 1, 1, 1]))  # You can adjust the color
                    plot.points = list(zip(x, y))
                    self.graph.add_plot(plot)

                    # Add label near the last point of the plot
                    label = Label(
                        text=key,
                        size_hint=(None, None),
                        size=(100, 30),
                        pos=(self.graph.pos[0] + (len(x)-1) * self.graph.width / 10,
                             self.graph.pos[1] + y[-1] * self.graph.height / 100)
                    )
                    self.add_widget(label)
                    self.plots[key] = (plot, label)
                except ValueError as e:
                    print(f"Error plotting data for {key}: {e}")
            else:
                print(f"Expected a list for {key}, but got {type(value)} instead.")

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(Dashboard(name='dashboard'))
        sm.add_widget(GraphScreen(name='graph'))
        return sm

if __name__ == '__main__':
    MyApp().run()

from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.properties import ObjectProperty, StringProperty
from kivy_garden.graph import Graph, LinePlot
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from api import fetch_data, send_dummy_data, DATA_KEYS
import numpy as np
from kivymd.uix.card import MDCard

class GraphScreen(Screen):
    graph_layout = ObjectProperty(None)
    selected_data_series = StringProperty('Voltage')  # Default selected series
    max_points = 100  # Maximum number of points to display on the graph

    def __init__(self, **kwargs):
        super(GraphScreen, self).__init__(**kwargs)
        self.colors = {
            "Voltage": [1, 0, 0, 1],  # Red
            "Current": [0, 1, 0, 1],  # Green
            "Power": [0, 0, 1, 1],    # Blue
            "Energy": [1, 1, 0, 1]    # Yellow
        }
        self.graph = Graph(
            xlabel='Time',
            ylabel=self.selected_data_series,
            x_ticks_minor=5,
            x_ticks_major=1,
            y_ticks_major=10,
            y_grid_label=True,
            x_grid_label=True,
            label_options={'color': [0, 0, 0, 1], 'bold': True},  # Set label color to black
            padding=5,
            xlog=False,
            ylog=False,
            xmin=0,
            xmax=self.max_points,
            ymin=0,
            ymax=100,
            background_color=[0.9, 0.9, 0.9, 1],
            border_color=[0, 0, 0, 1]
        )
        self.plot = LinePlot(color=self.colors[self.selected_data_series])
        self.graph.add_plot(self.plot)
        self.data_history = {key: [] for key in DATA_KEYS}
        self.last_fetched_data = None
        self.update_interval = 1  # Update interval in seconds
        self.update_event = None

    def on_enter(self):
        print("GraphScreen entered")
        Clock.schedule_once(self.add_graph_to_layout)
        self.update_event = Clock.schedule_interval(self.update_data, self.update_interval)

    def on_leave(self):
        print("GraphScreen left")
        if self.update_event:
            self.update_event.cancel()

    def add_graph_to_layout(self, dt):
        if self.graph_layout and not self.graph_layout.children:
            self.graph_layout.add_widget(self.graph)

    def update_data(self, dt):
        print("Attempting to fetch data...")
        try:
            data = fetch_data()
            print(f"Fetched data: {data}")
            if data and data != self.last_fetched_data:
                self.last_fetched_data = data
                self.update_data_history(data)
                self.plot_graph()
            else:
                print("Data has not changed or no data fetched.")
                self.send_dummy_data()
        except Exception as e:
            print(f"Error fetching data: {e}")
            self.send_dummy_data()

    def update_data_history(self, data):
        for key in DATA_KEYS:
            if key in data:
                self.data_history[key] = (self.data_history[key] + data[key])[-self.max_points:]  # Keep only the latest max_points values

    def plot_graph(self):
        selected_series = self.selected_data_series
        y = self.data_history[selected_series]
        x = list(range(len(y)))
        if y:  # Check if there is data to plot
            self.plot.points = list(zip(x, y))
            # Update axis labels and graph range dynamically
            self.graph.xlabel = "Time"
            self.graph.ylabel = selected_series
            self.graph.xmax = max(len(x), self.max_points)
            self.graph.ymin = min(y) if y else 0
            self.graph.ymax = max(y) if y else 100
            # Ensure ymin and ymax are not equal to avoid division by zero
            if self.graph.ymin == self.graph.ymax:
                self.graph.ymax += 0.1
        else:
            print(f"No data to plot for {selected_series}")

    def send_dummy_data(self, dt=None):
        data = {
            "Voltage": [np.random.randint(200, 250) for _ in range(1)],  # Send only one new value per series
            "Current": [np.random.uniform(2, 4) for _ in range(1)],
            "Power": [np.random.uniform(90, 100) for _ in range(1)],
            "Energy": [np.random.randint(60, 80) for _ in range(1)]
        }
        try:
            status_code = send_dummy_data(data)
            if status_code:
                print(f"Status Code: {status_code}")
                self.update_data_history(data)
                self.plot_graph()
            else:
                print("Failed to send dummy data.")
        except Exception as e:
            print(f"Error sending dummy data: {e}")

    def update_selected_data_series(self, key):
        self.selected_data_series = key
        self.plot.color = self.colors[key]
        self.plot_graph()

    def open_dropdown(self, button):
        dropdown = DropDown()
        for key in DATA_KEYS:
            btn = Button(text=key, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)
        dropdown.bind(on_select=lambda instance, x: setattr(button, 'text', x))
        dropdown.bind(on_select=lambda instance, x: self.update_selected_data_series(x))
        dropdown.open(button)

from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.properties import ObjectProperty, StringProperty
from kivy_garden.graph import Graph, LinePlot
from api import fetch_data, send_dummy_data, DATA_KEYS
import numpy as np

class GraphScreen(Screen):
    graph_layout = ObjectProperty(None)
    selected_data_series = StringProperty('Voltage')  # Default selected series

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
        self.plots = []
        Clock.schedule_once(self.add_graph_to_layout)

    def add_graph_to_layout(self, dt):
        if self.graph_layout:
            self.graph_layout.add_widget(self.graph)
            Clock.schedule_interval(self.update_data, 1.7)
        else:
            print("graph_layout is not initialized")

    def update_data(self, dt):
        data = fetch_data()
        if data:
            self.plot_graph(data)
        else:
            print("Failed to fetch data.")

    def plot_graph(self, data):
        # Clear existing plots
        for plot in self.plots:
            self.graph.remove_plot(plot)
        self.plots.clear()

        colors = {
            "Voltage": [1, 0, 0, 1],  # Red
            "Current": [0, 1, 0, 1],  # Green
            "Power": [0, 0, 1, 1],    # Blue
            "Energy": [1, 1, 0, 1]    # Yellow
        }

        # Plot only the selected data series
        selected_series = self.selected_data_series
        if selected_series in DATA_KEYS and isinstance(data.get(selected_series), list):
            y = [float(v) for v in data[selected_series]]
            x = list(range(len(y)))
            plot = LinePlot(line_width=1.5, color=colors.get(selected_series, [1, 1, 1, 1]))
            plot.points = list(zip(x, y))
            self.graph.add_plot(plot)
            self.plots.append(plot)

            # Update axis labels and graph range dynamically
            self.graph.xlabel = selected_series
            self.graph.ylabel = "Value"
            self.graph.xmax = len(x) - 1 if x else 10
            self.graph.ymin = min(y) if y else 0
            self.graph.ymax = max(y) if y else 100
        else:
            print(f"Unexpected data format for '{selected_series}'")

    def send_dummy_data(self, dt=None):
        data = {
            "Voltage": [np.random.randint(200, 250) for _ in range(10)],
            "Current": [np.random.uniform(2, 4) for _ in range(10)],
            "Power": [np.random.uniform(90, 100) for _ in range(10)],
            "Energy": [np.random.randint(60, 80) for _ in range(10)]
        }
        status_code = send_dummy_data(data)
        if status_code:
            print(f"Status Code: {status_code}")
        else:
            print("Failed to send dummy data.")

    def update_selected_data_series(self, checkbox, value, key):
        if value:
            self.selected_data_series = key
            self.update_data(0)
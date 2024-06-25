import sys
import os

# Add the garden path manually
garden_path = os.path.join(os.path.expanduser("~"), ".kivy", "garden")
if garden_path not in sys.path:
    sys.path.append(garden_path)

from kivy_garden.graph import Graph, LinePlot

print("Kivy Garden Graph module imported successfully!")

# Create a simple Kivy app to test the graph widget
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class GraphApp(App):
    def build(self):
        layout = BoxLayout()
        graph = Graph(xlabel='X', ylabel='Y', x_ticks_minor=5,
                      x_ticks_major=25, y_ticks_major=1,
                      y_grid_label=True, x_grid_label=True, padding=5,
                      x_grid=True, y_grid=True, xmin=0, xmax=100, ymin=-1, ymax=1)

        plot = LinePlot(line_width=1.5, color=[1, 0, 0, 1])
        plot.points = [(x, x ** 0.5) for x in range(0, 101)]
        graph.add_plot(plot)
        
        layout.add_widget(graph)
        return layout

if __name__ == '__main__':
    GraphApp().run()

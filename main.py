import os
import sys
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder

# Add the root directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from Screens.login import LoginScreen
from Screens.dashboard import Dashboard
from Screens.graph import GraphScreen
from Screens.sidebar import Sidebar  # Import the Sidebar widget from Screens

# Ensure the garden package path is added to sys.path
garden_path = os.path.join(os.path.expanduser("~"), ".kivy", "garden")
if garden_path not in sys.path:
    sys.path.append(garden_path)

class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"

        Builder.load_file('kv/login.kv')
        Builder.load_file('kv/dashboard.kv')
        Builder.load_file('kv/graph.kv')
        Builder.load_file('kv/sidebar.kv')  # Load the sidebar.kv file

        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(Dashboard(name='dashboard'))
        sm.add_widget(GraphScreen(name='graph'))
        return sm

if __name__ == '__main__':
    MyApp().run()

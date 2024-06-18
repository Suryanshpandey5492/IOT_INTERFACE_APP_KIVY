import os
import sys
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder

# Add the root directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from Screens.login import LoginScreen
from Screens.dashboard import Dashboard
from Screens.graph import GraphScreen

# Ensure the garden package path is added to sys.path
garden_path = os.path.join(os.path.expanduser("~"), ".kivy", "garden")
if garden_path not in sys.path:
    sys.path.append(garden_path)

class MyApp(App):
    def build(self):
        Builder.load_file('kv/login.kv')
        Builder.load_file('kv/dashboard.kv')
        Builder.load_file('kv/graph.kv')

        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(Dashboard(name='dashboard'))
        sm.add_widget(GraphScreen(name='graph'))
        return sm

if __name__ == '__main__':
    MyApp().run()
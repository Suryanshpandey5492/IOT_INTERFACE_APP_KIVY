import os
import sys
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.clock import Clock

# Add the root directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from Screens.login import LoginScreen
from Screens.dashboard import Dashboard
from Screens.graph import GraphScreen
from Screens.sidebar import Sidebar
from Screens.control import Control 
from Screens.settings import Settings 
from custom_screen import CustomScreen 

# Ensure the garden package path is added to sys.path
garden_path = os.path.join(os.path.expanduser("~"), ".kivy", "garden")
if garden_path not in sys.path:
    sys.path.append(garden_path)

class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Red"

        Builder.load_file('kv/login.kv')

        self.sm = ScreenManager()
        self.sm.add_widget(LoginScreen(name='login'))

        # Schedule the loading of other screens after 1 second
        Clock.schedule_once(self.load_other_screens, 1)

        return self.sm

    def load_other_screens(self, dt):
        Builder.load_file('kv/dashboard.kv')
        Builder.load_file('kv/graph.kv')
        Builder.load_file('kv/sidebar.kv')
        Builder.load_file('kv/control.kv')
        Builder.load_file('kv/settings.kv')  # Load the KV file for ControlScreen

        self.sm.add_widget(Dashboard(name='dashboard'))
        self.sm.add_widget(GraphScreen(name='graph'))
        self.sm.add_widget(Control(name='control'))
        self.sm.add_widget(Settings(name='settings'))  # Add ControlScreen

    # def on_start(self):
    #     # Optional: You can use this method to switch to the login screen if needed
    #     self.sm.current = 'login'

if __name__ == '__main__':
    MyApp().run()

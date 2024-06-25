import os
import sys

# Disable Kivy's argument parsing
os.environ['KIVY_NO_ARGS'] = '1'

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from Screens.login import LoginScreen
from Screens.dashboard import Dashboard
from Screens.graph import GraphScreen
from Screens.sidebar import Sidebar  # Import the Sidebar widget from Screens

# Add the root directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Ensure the garden package path is added to sys.path
garden_path = os.path.join(os.path.expanduser("~"), ".kivy", "garden")
if garden_path not in sys.path:
    sys.path.append(garden_path)

class TestApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"

        if '--test-sidebar' in sys.argv:
            return self.build_test_sidebar()
        elif '--test-login' in sys.argv:
            return self.build_test_login()
        elif '--test-dashboard' in sys.argv:
            return self.build_test_dashboard()
        elif '--test-graph' in sys.argv:
            return self.build_test_graph()
        else:
            return self.build_full_app()

    def build_test_sidebar(self):
        Builder.load_file('kv/sidebar.kv')
        Builder.load_file('kv/test_sidebar.kv')
        return Builder.load_file('kv/test_sidebar.kv')

    def build_test_login(self):
        Builder.load_file('kv/login.kv')
        return LoginScreen()

    def build_test_dashboard(self):
        Builder.load_file('kv/sidebar.kv')  # Load sidebar.kv because it's used in the dashboard
        Builder.load_file('kv/dashboard.kv')
        return Dashboard()

    def build_test_graph(self):
        Builder.load_file('kv/graph.kv')
        return GraphScreen()

    def build_full_app(self):
        Builder.load_file('kv/login.kv')
        Builder.load_file('kv/dashboard.kv')
        Builder.load_file('kv/graph.kv')
        Builder.load_file('kv/sidebar.kv')

        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(Dashboard(name='dashboard'))
        sm.add_widget(GraphScreen(name='graph'))
        return sm

if __name__ == '__main__':
    TestApp().run()

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import os

# Load the login.kv file
Builder.load_file(os.path.join(os.path.dirname(__file__), 'login.kv'))

class LoginScreen(Screen):
    def validate_login(self, username, password):
        # Add your login validation logic here
        if username == 'user' and password == 'pass':
            self.manager.current = 'dashboard'
        else:
            print("Invalid credentials")

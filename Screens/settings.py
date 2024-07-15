from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty
from api import set_device_id

class SettingsScreen(Screen):
    device_id_input = ObjectProperty(None)
    device_id = StringProperty("9lpqiYnhjfesPnWTvi3l")  # Default device ID

    def save_device_id(self):
        new_device_id = self.device_id_input.text
        set_device_id(new_device_id)
        self.device_id = new_device_id
        print(f"Device ID set to {new_device_id}")

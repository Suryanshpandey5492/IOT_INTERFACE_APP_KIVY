from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty
from api import set_api_details
from custom_screen import CustomScreen  # Ensure this import is correct
from Screens.config import update_graph_screen_interval
update_interval = 1  # Default value

class Settings(CustomScreen):
    read_api_input = ObjectProperty(None)
    write_api_input = ObjectProperty(None)
    update_interval_input = ObjectProperty(None)  # New property for the update interval

    def set_update_interval(self, interval):
        global update_interval
        update_interval = interval
        print(f"Update interval set to: {update_interval}")
        update_graph_screen_interval(self)

    def get_update_interval(self):
        return update_interval

    def save_api_details(self):
        read_api_url = self.read_api_input.text if self.read_api_input.text else None
        write_api_url = self.write_api_input.text if self.write_api_input.text else None
        interval_text = self.update_interval_input.text if self.update_interval_input.text else None

        if interval_text and interval_text.isdigit():
            interval = int(interval_text)
            self.set_update_interval(interval)  # Update the interval
        else:
            print("Update interval must be a positive integer")

        set_api_details(read_api_url, write_api_url)  # Set the new API details

        print(f"API details set to Read API: {read_api_url}, Write API: {write_api_url}, Update Interval: {interval if interval_text else 'Not Changed'}")






from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.properties import StringProperty, ObjectProperty
from kivy.core.window import Window
from api import fetch_data, DATA_KEYS  # Ensure fetch_data and DATA_KEYS are correctly imported
import numpy as np
from custom_screen import CustomScreen  # Import CustomScreen from the new module

class Dashboard(CustomScreen):  # Inherit from CustomScreen
    error_message = ObjectProperty(None) 
    voltage = StringProperty("N/A")
    current = StringProperty("N/A")
    power = StringProperty("N/A")
    energy = StringProperty("N/A")
    update_interval = 10  # Update interval in seconds 

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.last_fetched_data = None
        self.update_event = None  # To store the scheduled update event
        Window.bind(on_resize=self.on_resize)
        self.on_resize(Window, Window.width, Window.height)

    def on_enter(self):
        self.start_update()

    def on_leave(self):
        self.stop_update()

    def start_update(self):
        self.update_data(0)  # Initial immediate update
        self.update_event = Clock.schedule_interval(self.update_data, self.update_interval)

    def stop_update(self):
        if self.update_event:
            self.update_event.cancel()
            self.update_event = None

    def update_data(self, dt):
        try:
            data = fetch_data()
            if data and data != self.last_fetched_data:
                self.last_fetched_data = data
                self.error_message.text = ""  # Clear the error message

                for key in DATA_KEYS:
                    if key in data:
                        # Assuming data[key] is a list or array of values
                        avg_value = np.mean(data[key])
                        truncated_value = round(avg_value, 3)
                        setattr(self, key.lower(), str(truncated_value))
                    else:
                        print(f"Key '{key}' not found in API response.")
            else:
                print("Data has not changed.")
                self.error_message.text = "Data has not changed."
        except Exception as e:
            print(f"Error fetching data: {e}")

    def on_resize(self, window, width, height):
        grid_layout = self.ids.grid_layout
        if width < 800:
            grid_layout.cols = 1
        elif width < 1200:
            grid_layout.cols = 2
        else:
            grid_layout.cols = 3

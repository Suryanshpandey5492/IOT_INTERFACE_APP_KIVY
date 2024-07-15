from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.properties import StringProperty
from api import fetch_data, DATA_KEYS  # Ensure fetch_data and DATA_KEYS are correctly imported
import numpy as np
from custom_screen import CustomScreen  # Import CustomScreen from the new module

class Dashboard(CustomScreen):  # Inherit from CustomScreen
    voltage = StringProperty("0")
    current = StringProperty("0")
    power = StringProperty("0")
    energy = StringProperty("0")
    update_interval = 10  # Update interval in seconds

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.update_event = None  # To store the scheduled update event

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
            if data:
                for key in DATA_KEYS:
                    if key in data:
                        # Assuming data[key] is a list or array of values
                        avg_value = np.mean(data[key])
                        truncated_value = round(avg_value, 3)
                        setattr(self, key.lower(), str(truncated_value))
                    else:
                        print(f"Key '{key}' not found in API response.")
            else:
                print("Failed to fetch data.")
        except Exception as e:
            print(f"Error fetching data: {e}")

from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.properties import StringProperty
from api import fetch_data, DATA_KEYS  # Import DATA_KEYS from api module
import numpy as np

class Dashboard(Screen):
    voltage = StringProperty("0")
    current = StringProperty("0")
    power = StringProperty("0")
    energy = StringProperty("0")

    def __init__(self, **kwargs):
        super(Dashboard, self).__init__(**kwargs)
        Clock.schedule_once(self.update_data, 1)  # Schedule initial data update
        Clock.schedule_interval(self.update_data, 10)  # Update data every 10 seconds

    def update_data(self, dt):
        data = fetch_data()
        if data:
            for key in DATA_KEYS:
                if key in data:
                    setattr(self, key.lower(), str(np.mean(data[key])))
                else:
                    print(f"Key '{key}' not found in API response.")
        else:
            print("Failed to fetch data.")

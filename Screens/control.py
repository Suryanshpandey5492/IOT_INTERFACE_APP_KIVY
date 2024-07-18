from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
from custom_screen import CustomScreen

from api import send_dummy_data  

class Control(CustomScreen):
    voltage_input = ObjectProperty(None)
    current_input = ObjectProperty(None)
    power_input = ObjectProperty(None)
    energy_input = ObjectProperty(None)

    def submit_data(self, instance):
        voltage = self.voltage_input.text
        current = self.current_input.text
        power = self.power_input.text
        energy = self.energy_input.text

        data = {
            'Voltage': [float(voltage) if voltage else 0],
            'Current': [float(current) if current else 0],
            'Power': [float(power) if power else 0],
            'Energy': [float(energy) if energy else 0]
        }

        try:
            status_code = send_dummy_data(data)
            if status_code:
                print(f"Data sent successfully: {data}")
            else:
                print("Failed to send data.")
        except Exception as e:
            print(f"Error sending data: {e}")

    def go_back(self, instance):
        self.manager.current = self.manager.previous()  # Navigate to the previous screen

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

from api import send_dummy_data  # Make sure this function is implemented to send data to your database

class Control(Screen):
    voltage_input = ObjectProperty(None)
    current_input = ObjectProperty(None)
    power_input = ObjectProperty(None)
    energy_input = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Voltage
        self.layout.add_widget(Label(text="Voltage (Current Value: 0):", font_size='18sp', bold=True))
        self.voltage_input = TextInput(multiline=False, font_size='16sp', height='40dp', size_hint_y=None)
        self.layout.add_widget(self.voltage_input)
        
        # Current
        self.layout.add_widget(Label(text="Current (Current Value: 0):", font_size='18sp', bold=True))
        self.current_input = TextInput(multiline=False, font_size='16sp', height='40dp', size_hint_y=None)
        self.layout.add_widget(self.current_input)
        
        # Power
        self.layout.add_widget(Label(text="Power (Current Value: 0):", font_size='18sp', bold=True))
        self.power_input = TextInput(multiline=False, font_size='16sp', height='40dp', size_hint_y=None)
        self.layout.add_widget(self.power_input)
        
        # Energy
        self.layout.add_widget(Label(text="Energy (Current Value: 0):", font_size='18sp', bold=True))
        self.energy_input = TextInput(multiline=False, font_size='16sp', height='40dp', size_hint_y=None)
        self.layout.add_widget(self.energy_input)
        
        # Submit Button
        self.submit_button = Button(text="Submit", on_release=self.submit_data, font_size='18sp', height='50dp', size_hint_y=None, background_color=[0.1, 0.5, 0.8, 1], color=[1, 1, 1, 1])
        self.layout.add_widget(self.submit_button)

        # Back Button
        self.back_button = Button(text="Back", on_release=self.go_back, font_size='18sp', height='50dp', size_hint_y=None, background_color=[0.5, 0.5, 0.5, 1], color=[1, 1, 1, 1])
        self.layout.add_widget(self.back_button)

        self.add_widget(self.layout)

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

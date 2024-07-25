import requests
import random
from Screens.config import update_dashboard_screen, update_graph_screen

READ_API_KEY = "http://apps.openioe.in/openioe/api/showdevicejson/9lpqiYnhjfesPnWTvi3l/164/182"
WRITE_API_KEY = "http://apps.openioe.in/openioe/api/updatedevicejson/9lpqiYnhjfesPnWTvi3l/164/182/"
DATA_KEYS = ["Voltage", "Current", "Power", "Energy"]

def fetch_data():
    try:
        response = requests.get(READ_API_KEY)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def send_dummy_data(data):
    try:
        response = requests.post(WRITE_API_KEY, json=data)
        response.raise_for_status()
        return response.status_code
    except requests.RequestException as e:
        print(f"Error sending data: {e}")
        return None

def set_api_details(new_read_api_url=None, new_write_api_url=None):
    global WRITE_API_KEY, READ_API_KEY
    if new_read_api_url:
        READ_API_KEY = new_read_api_url
        print(f"READ_API_KEY changed to: {READ_API_KEY}")
    if new_write_api_url:
        WRITE_API_KEY = new_write_api_url
        print(f"WRITE_API_KEY changed to: {WRITE_API_KEY}")

def update_data_keys():
    data = fetch_data()
    if data:
        global DATA_KEYS
        DATA_KEYS = list(data.keys())
        print(f"DATA_KEYS updated to: {DATA_KEYS}")
        update_dashboard_screen()
        update_graph_screen()



# Example usage
if __name__ == "__main__":
    update_data_keys()  # Update DATA_KEYS based on the fetched data
    print(DATA_KEYS)  # Print updated DATA_KEYS
    dummy_data = {key: [random.randint(200, 249)] for key in DATA_KEYS}
    status_code = send_dummy_data(dummy_data)
    if status_code:
        print(f"Data sent successfully with status code: {status_code}")
    else:
        print("Failed to send data.")

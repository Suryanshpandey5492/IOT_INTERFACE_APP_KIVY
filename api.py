import requests

API_URL = "http://apps.openioe.in/openioe/api/"
DEVICE_ID = "9lpqiYnhjfesPnWTvi3l"
DATA_KEYS = ["Voltage", "Current", "Power", "Energy"]

def fetch_data():
    try:
        response = requests.get(f"{API_URL}/showdevicejson/{DEVICE_ID}/164/182")
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def send_dummy_data(data):
    try:
        response = requests.post(f"{API_URL}/updatedevicejson/{DEVICE_ID}/164/182/", json=data)
        response.raise_for_status()
        return response.status_code
    except requests.RequestException as e:
        print(f"Error sending data: {e}")
        return None

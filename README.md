IoT_APP - Kivy Example with Firebase Authentication and Data Visualization
This project is an example of an IoT application built using Kivy. It includes Firebase authentication and data visualization using kivy_garden.graph. The application fetches data from an API and displays it in a dashboard as well as in graphical form.

Features
Firebase Authentication: Secure user authentication using Firebase.
Data Fetching: Fetch real-time data from a specified API.
Dashboard: Display key metrics (Voltage, Current, Power, Energy) on a dashboard.
Graphical Representation: Plot real-time data using graphs.
Prerequisites
Python 3.x
Kivy
Kivy Garden
Requests
Numpy
Installation
Clone the Repository:

sh
Copy code
git clone https://github.com/yourusername/IoT_APP.git
cd IoT_APP
Create and Activate Virtual Environment:

sh
Copy code
python -m venv kivy_venv
source kivy_venv/bin/activate  # On Windows use `kivy_venv\Scripts\activate`
Install Dependencies:

sh
Copy code
pip install kivy requests numpy kivy_garden.graph
Install Kivy Garden Graph:

sh
Copy code
garden install graph
Add Garden Path to sys.path:
Ensure the garden package path is added to your sys.path as shown in the script:

python
Copy code
garden_path = os.path.join(os.path.expanduser("~"), ".kivy", "garden")
if garden_path not in sys.path:
    sys.path.append(garden_path)
Firebase Configuration:
Make sure to set up Firebase authentication and include your Firebase configuration files correctly.

Running the Application
Start the Application:

sh
Copy code
python main.py
Login Screen:

The application starts with a login screen. Ensure that the LoginScreen is properly configured and imported in the script.
Dashboard and Graph:

After logging in, you will be redirected to the Dashboard.
The Graph screen displays real-time data plots for Voltage, Current, Power, and Energy.
Directory Structure
bash
Copy code
IoT_APP/
├── main.py                # Main application script
├── login.kv               # Kivy file for login screen
├── my.kv                  # Kivy file for dashboard and graph screens
├── README.md              # Readme file
└── other necessary files  # Include other required files and configurations
Script Explanation
main.py
Imports: Necessary modules and classes are imported, including Kivy modules, requests for API calls, numpy for data handling, and custom screens.
Constants: Define global variables for the API URL and device ID.
Classes:
Dashboard: Displays real-time data metrics. It updates the data every 10 seconds by making an API call.
GraphScreen: Plots real-time data on graphs. It updates the graph every 10 seconds by making an API call.
MyApp: Main application class that builds the screen manager and loads the Kivy files.
Kivy Files
login.kv: Define the layout and behavior of the login screen.
my.kv: Define the layout and behavior of the dashboard and graph screens.
Troubleshooting
Push Rejection Due to Secrets: If your push to GitHub is rejected due to detected secrets (e.g., Firebase credentials), ensure to remove sensitive information from the commit history. Refer to GitHub documentation on removing sensitive data for more information.
Contributions
Feel free to fork the repository, make changes, and submit pull requests. Contributions are welcome!

License
This project is licensed under the MIT License. See the LICENSE file for details.
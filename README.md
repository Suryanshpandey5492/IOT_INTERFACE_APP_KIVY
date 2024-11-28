# IoT Based app for Energy Management

This project is an example of an IoT application built using Kivy. It includes **Firebase authentication** and **data visualization**. The application fetches data from an API and displays it in a dashboard and as a graph.

## Features
- **Firebase Authentication**: Secure user authentication using Firebase.
- **Data Fetching**: Fetch real-time data from a specified API.
- **Dashboard**: Display key metrics like **Voltage**, **Current**, **Power**, and **Energy**.
- **Graphical Representation**: Plot real-time data using graphs.






## Installation

#### Prerequisites
- Python 3.x
- Kivy
- Kivy Garden
- Requests
- Numpy

#### Setup
1. Clone repo:
```bash
  git clone https://github.com/Suryanshpandey5492/IOT_INTERFACE_APP_KIVY.git
```
2. Activate virtual environment:
```bash
  python -m venv venv
  source venv/bin/activate # For Windows: venv\Scripts\activate
```
or
```bash
  pipenv shell
```
3. Make sure to install prerequisites

4. Firebase Configuration:
Make sure to set up Firebase authentication and include your Firebase configuration file in ```login.py``` file.


### Troubleshooting
**Push Rejection Due to Secrets**: If your push to GitHub is rejected due to detected secrets (e.g., Firebase credentials), ensure to remove sensitive information from the commit history. Refer to the [GitHub documentation](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository) on removing sensitive data for more details.
## Contributing

Feel free to fork the repository, make changes, and submit pull requests. Contributions are welcome!


## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/). 



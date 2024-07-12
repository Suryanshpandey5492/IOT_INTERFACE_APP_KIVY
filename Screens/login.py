from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty
import firebase_admin
from firebase_admin import credentials, auth
from firebase_admin._auth_utils import EmailAlreadyExistsError, UserNotFoundError

# Initialize Firebase
cred = credentials.Certificate("C:/Users/sampa/Desktop/Project/IoT_APP/kivy_examples-main/iotinteract-1a1b9-firebase-adminsdk-lynn1-c2a0d8520e.json")
firebase_admin.initialize_app(cred)

class LoginScreen(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    error_message = StringProperty("")

    def login(self):
        email = self.username.text.strip()
        password = self.password.text.strip()

        if not email or not password:
            self.error_message = "Email and password cannot be empty."
            return

        try:
            user = auth.get_user_by_email(email)
            if self.verify_password(user.uid, password):
                self.manager.current = 'dashboard'  # Switch to dashboard on successful login
            else:
                self.error_message = "Invalid password."
        except UserNotFoundError:
            self.error_message = "User does not exist."
        except ValueError as e:
            self.error_message = str(e)
        except Exception as e:
            self.error_message = f"Error: {e}"

    def signup(self):
        email = self.username.text.strip()
        password = self.password.text.strip()

        if not email or not password:
            self.manager.current = 'dashboard'
            #self.error_message = "Email and password cannot be empty."
            return

        try:
            user = auth.create_user(email=email, password=password)
            self.manager.current = 'dashboard'  # Switch to dashboard on successful signup
        except EmailAlreadyExistsError:
            self.error_message = "Email already exists."
        except ValueError as e:
            self.error_message = str(e)
        except Exception as e:
            self.error_message = f"Error: {e}"

    def verify_password(self, uid, password):
        try:
            user = auth.get_user(uid)
            password_hash = user.password_hash
            # Replace with a secure hashing function and compare with stored hash
            # Example: return check_password_hash(password, user.password_hash)
            return True  # Placeholder, replace with actual logic
        except Exception as e:
            # Handle errors appropriately
            return False

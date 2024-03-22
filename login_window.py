# # import the Config class, necessary for configu a Kivy windws
# from kivy.config import Config
# # create a configuration for fulfill entire screen in the computer 
# Config.set('graphics', 'fullscreen', 'auto')

# import the App class, necessary for creating a Kivy application
from kivy.app import App
# import the Button class, used for creating button widgets
from kivy.uix.button import Button
# import the BoxLayout class, used for creating a layout container
from kivy.uix.boxlayout import BoxLayout
# import the TextInput class, used for creating text input fields
from kivy.uix.textinput import TextInput
# import the Label class, used for creating text labels
from kivy.uix.label import Label
# import ScreenManager and Screen classes for managing multiple screens/windows
from kivy.uix.screenmanager import ScreenManager, Screen
# import the Popup class, used for creating popup windows
from kivy.uix.popup import Popup
# import csv for managing csv files
import csv
# import show_popup_window from popup_window for create popup window
from popup_window import show_popup_window
# import USERS_CSV_FILEPATH from global variables
from global_variables import USERS_CSV_FILEPATH

# define the LoginWindow class, inheriting from Screen, for the login interface
class LoginWindow(Screen):
    def __init__(self, **kwargs):
        # initialize the superclass (Screen) with any provided keyword arguments
        super(LoginWindow, self).__init__(**kwargs)
        # create a vertical BoxLayout for the login interface
        layout = BoxLayout(orientation='vertical')
        
        # add a label for the username input field
        layout.add_widget(Label(text='Username:'))
        # create and add a single-line TextInput for username input
        self.username = TextInput(multiline=False)
        layout.add_widget(self.username)
        
        # add a label for the password input field.
        layout.add_widget(Label(text='Password:'))
        # create and add a password TextInput (hidden text) for password input
        self.password = TextInput(password=True, multiline=False)
        layout.add_widget(self.password)
        
        # create a Login button and add it to the layout
        login_button = Button(text='Login', font_size='20sp')
        login_button.bind(on_press=self.go_logged_user)
        layout.add_widget(login_button)
        
        # create a Back button, bind its on_press event to the back_to_menu method, and add it to the layout
        back_button = Button(text='Back', font_size='20sp')
        back_button.bind(on_press=self.back_to_menu)
        layout.add_widget(back_button)
        
        # add the layout to the screen
        self.add_widget(layout)
    
    # define a method to handle the Back button press, navigating back to the main menu
    def back_to_menu(self, instance):
        self.manager.current = 'menu'

    # define a method to clear TextInput after handle the Login button press
    def clear_text_inputs(self):
        self.username.text = ''
        self.password.text = ''

    # define a method to handle the Login button press, navigating to the logged user screen after checking username and password
    def go_logged_user(self, instance):
        # variable storage information if username and password is correct
        correct_username_password = False
        # open csv file in read mode (mode='r') to check username and password correctnes
        with open(USERS_CSV_FILEPATH, mode='r', newline='') as csv_checking_user:
        # create a csv reader specifying the delimiter as ';' (delimiter=';')
            reader = csv.reader(csv_checking_user, delimiter=';')
            # iterate over each row in the csv file
            for row in reader:
                # check if the username and password is correct
                if row[1] == self.username.text and row[3] == self.password.text:
                    correct_username_password = True
                    # use method for clear TextInput fields
                    self.clear_text_inputs()
                    # navigating to the logged user screen
                    self.manager.current = 'logged_user'
                else:
                    continue
            # create 
            if not correct_username_password:
                show_popup_window('Error', 'Incorrect username or password')

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
# import csv for managing csv files
import csv

users_csv_filepath = 'D:/python_data/projekt/warehouse_management/warehouse-management/users.csv'

# define the RegistrationWindow class, inheriting from Screen, for the registration interface
class RegistrationWindow(Screen):
    def __init__(self, **kwargs):
        # initialize the superclass (Screen) with any provided keyword arguments
        super(RegistrationWindow, self).__init__(**kwargs)
        # create a vertical BoxLayout for the registration interface
        layout = BoxLayout(orientation='vertical')

        # add a label for the name input field.
        layout.add_widget(Label(text='Name:'))
        # create and add a single-line TextInput for name input
        self.user_name = TextInput(multiline=False)
        layout.add_widget(self.user_name)
        
        # add a label for the surname input field.
        layout.add_widget(Label(text='Surname:'))
        # create and add a surname TextInput (hidden text) for surname input
        self.user_surname = TextInput(multiline=False)
        layout.add_widget(self.user_surname)

        # add a label for the password input field.
        layout.add_widget(Label(text='Password:'))
        # create and add a password TextInput (hidden text) for password input
        self.password = TextInput(multiline=False)
        layout.add_widget(self.password)
        
        # create a Registration button and add it to the layout
        user_registration_button = Button(text='Registration', font_size='20sp')
        user_registration_button.bind(on_press=self.registration_user)
        layout.add_widget(user_registration_button)

        # create a Back button, bind its on_press event to the back_to_menu method, and add it to the layout
        back_button = Button(text='Back', font_size='20sp')
        back_button.bind(on_press=self.back_to_menu)
        layout.add_widget(back_button)
        
        # add the layout to the screen
        self.add_widget(layout)
    
    # define a method to handle the Back button press, navigating back to the main menu
    def back_to_menu(self, instance):
        self.manager.current = 'menu'

    # define a method to handle the Registration button press, insert id (autoincremented), name, surname, password to users.csv
    def registration_user(self, instance):
        # initialize last user id as None
        self.last_id_user = None
        # open csv file in read mode (mode='r') to find last user id
        with open(users_csv_filepath, mode='r', newline='') as csv_define_id:
            # create a csv reader specifying the delimiter as ';' (delimiter=';')
            reader = csv.reader(csv_define_id, delimiter=';')
            # iterate over each row in the csv file
            for row in reader:
                # check if the row is not empty and the first element is a digit
                if row and row[0].isdigit():
                    # update last user id with the id from the row
                    self.last_id_user = int(row[0])
        # determine the new user id by incrementing the last one found, or start at 0 if none
        self.new_id_user = (self.last_id_user + 1) if self.last_id_user is not None else 0

        # collect registration data, new id, name, surname, password and inputs from TextInput (.text)
        self.registration_user_data = [self.new_id_user, self.user_name.text, self.user_surname.text, self.password.text]

        # open the csv file in append mode (mode='a') to add the new user data
        with open(users_csv_filepath, mode='a', newline='') as users_csv:
            # create a csv writer specifying the delimiter as ';'
            users_new_records_csv = csv.writer(users_csv, delimiter=';')
            # write the new user record to the csv file
            users_new_records_csv.writerow(self.registration_user_data)

        # use method for clear TextInput fields
        self.clear_text_inputs()

    # define a method to clear TextInput and variables after handle the Registration button press
    def clear_text_inputs(self):
        self.user_name.text = ''
        self.user_surname.text = ''
        self.password.text = ''
        self.new_id_user = 0
        self.registration_user_data = []
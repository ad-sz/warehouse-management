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

# define the LoginWindow class, inheriting from Screen, for the login interface
class LoginWindow(Screen):
    def __init__(self, **kwargs):
        # initialize the superclass (Screen) with any provided keyword arguments
        super(LoginWindow, self).__init__(**kwargs)
        # create a vertical BoxLayout for the login interface
        layout = BoxLayout(orientation='vertical')
        
        # add a label for the username input field.
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

    # define a method to handle the Login button press, navigating to the logged user
    def go_logged_user(self, instance):
        self.manager.current = 'logged_user'
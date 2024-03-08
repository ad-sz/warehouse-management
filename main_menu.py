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

# define the MainMenu class, inheriting from Screen, for the main menu interface
class MainMenu(Screen):
    def __init__(self, **kwargs):
        # initialize the superclass (Screen) with any provided keyword arguments
        super(MainMenu, self).__init__(**kwargs)
        # create a vertical BoxLayout for the main menu
        layout = BoxLayout(orientation='vertical')
        
        # create a Login button, bind its on_press event to switch_to_login method, and add it to the layout
        login_button = Button(text='Login', font_size='20sp')
        login_button.bind(on_press=self.switch_to_login)
        layout.add_widget(login_button)
        
        # create a Registration button, bind its on_press event to switch_to_registration method, and add it to the layout
        registration_button = Button(text='Registration', font_size='20sp')
        registration_button.bind(on_press=self.switch_to_registration)
        layout.add_widget(registration_button)
        
        # add the layout to the screen
        self.add_widget(layout)

    # define methods to handle button presses, switching to the login or registration screens
    def switch_to_login(self, instance):
        self.manager.current = 'login'

    def switch_to_registration(self, instance):
        self.manager.current = 'registration'
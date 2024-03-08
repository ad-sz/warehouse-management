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
        registration_button = Button(text='Registration', font_size='20sp')
        layout.add_widget( registration_button)

        # create a Back button, bind its on_press event to the back_to_menu method, and add it to the layout
        back_button = Button(text='Back', font_size='20sp')
        back_button.bind(on_press=self.back_to_menu)
        layout.add_widget(back_button)
        
        # add the layout to the screen
        self.add_widget(layout)
    
    # define a method to handle the Back button press, navigating back to the main menu
    def back_to_menu(self, instance):
        self.manager.current = 'menu'
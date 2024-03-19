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
class LoggedUserWindow(Screen):
    def __init__(self, **kwargs):
        # initialize the superclass (Screen) with any provided keyword arguments
        super(LoggedUserWindow, self).__init__(**kwargs)
        # create a vertical BoxLayout for the login interface
        layout = BoxLayout(orientation='vertical')
        
        # add a label for the username input field.
        layout.add_widget(Label(text='Enter item name:'))
        # create and add a single-line TextInput for username input
        self.item_name = TextInput(multiline=False)
        layout.add_widget(self.item_name)
        
        # add a label for the password input field.
        layout.add_widget(Label(text='Enter item number:'))
        # create and add a password TextInput (hidden text) for password input
        self.item_number = TextInput(multiline=False)
        layout.add_widget(self.item_number)
        
        # create a Search item button and add it to the layout
        search_button = Button(text='Search item', font_size='20sp')
        layout.add_widget(search_button)
        
        # create a Logout button, bind its on_press event to the back_to_menu method, and add it to the layout
        logout_button = Button(text='Logout', font_size='20sp')
        logout_button.bind(on_press=self.back_to_menu)
        layout.add_widget(logout_button)
        
        # add the layout to the screen
        self.add_widget(layout)
    
    # define a method to handle the Logout button press, navigating back to the main menu
    def back_to_menu(self, instance):
        self.item_name.text = ''
        self.item_number.text = ''
        self.manager.current = 'menu'
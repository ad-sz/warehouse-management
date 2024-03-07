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

# define the MyApp class, inheriting from App, as the main application class
class MyApp(App):
    def build(self):
        # set the main window title
        self.title = 'Warehouse_management'
        # create a ScreenManager for managing multiple screens
        self.screen_manager = ScreenManager()
        
        # add the MainMenu, LoginWindow, and RegistrationWindow to the ScreenManager
        self.screen_manager.add_widget(MainMenu(name='menu'))
        self.screen_manager.add_widget(LoginWindow(name='login'))
        self.screen_manager.add_widget(RegistrationWindow(name='registration'))
        
        # return the screen manager to be used as the root widget
        return self.screen_manager

# run the application if this script is executed as the main program
if __name__ == '__main__':
    MyApp().run()

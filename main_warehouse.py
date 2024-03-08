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

# import the LoginWindow class, used for creating login window
from login_window import LoginWindow
# import the RegistrationWindow class, used for creating registration window
from registration_window import RegistrationWindow
# import the MainMenu class, used for creating main menu window
from main_menu import MainMenu

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

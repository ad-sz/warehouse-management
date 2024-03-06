#iimport Config for configure window size
from kivy.config import Config
Config.set('graphics', 'fullscreen', 'auto')

#impoert basic class App which is neede to create Kivy aplication
from kivy.app import App
#import Widget class which is basic class for all UI elements in Kivy
from kivy.uix.widget import Widget
#import Button class for creae buttons
from kivy.uix.button import Button
#import BoxLayout class for creae layout
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

#create class for the login window which inherits from Screen from kivy library
class LoginWindow(Screen):
    def __init__ (self, **kwargs):  #class initialization method. **kwargs allows to pass any number of dictionary arguments to a method
       super(LoginWindow, self).__init__(**kwargs)  #calling the parent class's initialization method
       layout = BoxLayout(orientation='vertical')   #set vertical orientation in BoxLayout

       #create field for enter username
       layout.add_widget(Label(text='Username:'))   #adding a Label with the text "Username:" to the layout. This label serves as a description for the username entry field
       self.username = TextInput(multiline=False)   #creating a text field (TextInput) for the username. multiline=False - the field will be single-line
       layout.add_widget(self.username) #adding a previously created text field to the layout

       #create field for enter password
       layout.add_widget(Label(text='Password:'))   #adding a Label with the text "Password:" to the layout. This label serves as a description for the password entry field
       self.password = TextInput(password=True, multiline=False)   #creating a text field (TextInput) for the password. password=True - cover text like for passwords
       layout.add_widget(self.password) #adding a previously created text field to the layout

       #create login button
       login_button = Button(text='Login', font_size='100sp')
       layout.add_widget(login_button)
       self.add_widget(layout)

#create class for the registrtion window which inherits from Screen from kivy library
class RegistrationWindow(Screen):
    pass

#create class which inherits from BoxLayout for the main menu
class MainMenu(BoxLayout):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        self.orientation = 'vertical'   #set vertical orientation in BoxLayout
        self.add_widget(Button(text='Login', font_size='100sp')) #adding login button
        self.add_widget(Button(text='Registration', font_size='100sp')) #adding registration button

#create class which inherits from App
class MyApp(App):
    def build(self):
        self.title = 'Warehause_management' #set title of the window
        return MyWidget()
    
if __name__ == '__main__':
    MyApp().run()
#impoert basic class App which is neede to create Kivy aplication
from kivy.app import App
#import Widget class which is basic class for all UI elements in Kivy
from kivy.uix.widget import Widget
#import Button class for creae buttons
from kivy.uix.button import Button
#import BoxLayout class for creae layout
from kivy.uix.boxlayout import BoxLayout

#create class which inherits from Widget
class MyWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'   #set vertical orientation in BoxLayout
        self.add_widget(Button(text='Login')) #adding login button
        self.add_widget(Button(text='Registration')) #adding registration button

#create class which inherits from App
class MyApp(App):
    def build(self):
        self.title = 'Warehause_management' #set title of the window
        return MyWidget()
    
if __name__ == '__main__':
    MyApp().run()
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
# import the Popup class, used for creating popup windows
from kivy.uix.popup import Popup

# define a method to handle the popup window
def show_popup_window(popup_window_title, popup_window_message):
    # define a method to clouse the popup window
    def dismiss_popup(instance):
        popup_window.dismiss()

    # create a vertical BoxLayout for the popup window
    layout = BoxLayout(orientation='vertical', spacing=5)

    # add a label for message popup window
    layout.add_widget(Label(text=popup_window_message, font_size='20sp'))

    # create a Ok button which close the popup window and add it to the layout
    ok_button = Button(text='Ok', font_size='20sp', size_hint=(1, 0.2))
    ok_button.bind(on_press=dismiss_popup)
    layout.add_widget(ok_button)

    popup_window = Popup(title=popup_window_title, content=layout, size_hint=(None, None), size=(400, 400), auto_dismiss=False)
    popup_window.open()
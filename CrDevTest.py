from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from functools import partial
from CrWFileTest import *

class Entry(GridLayout):
    def __init__(self,**kwargs):
        super(Entry,self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Device Name'))
        self.DevName = TextInput(text = 'Enter Name',multiline=False)
        self.add_widget(self.DevName)
        self.name = 'Entry'
        self.id = 'Entry'

class Layout(GridLayout):
    def __init__(self,**kwargs):
        super(Layout,self).__init__(**kwargs)
        self.cols = 1
        self.Entry = Entry()
        self.add_widget(self.Entry)
        self.save = Button(text = 'Add Device')
        self.save.bind(on_release = self.InfoSave)
        self.add_widget(self.save)

    def InfoSave(self,instance):
        WTF('Device',self.Entry.DevName.text)

class MyApp(App):
    def build(self):
        return Layout()

if __name__ == "__main__":
    MyApp().run()
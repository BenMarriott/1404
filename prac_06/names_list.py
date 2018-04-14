from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.uix.label import Label

class DynamicNameList(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name_list = ["Mary", "John", "Bob", "Sarah", "Joy", "Frank"]

    def build(self):
        self.title = "Name List"
        self.root = Builder.load_file('names_list.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.name_list:
            temp_label = Label(text=str(name))
            self.root.ids.entries_box.add_widget(temp_label)

DynamicNameList().run()



from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    """Dynamically create labels for names in a list"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Jesse", "Liam", "Sam", "Jordan"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.names:
            temp_label = Label(id=name, text=name)
            self.root.ids.entries_box.add_widget(temp_label)


DynamicLabelsApp().run()
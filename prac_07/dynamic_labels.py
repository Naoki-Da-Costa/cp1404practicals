"""
CP1404/CP5632 Practical
Kivy GUI program to create dynamic labels
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Kivy App for converting to create dynamic labels."""
    def __init__(self, **kwargs):
        """Initialise list of names."""
        super().__init__(**kwargs)
        self.names = ["bob", "james", "kate", "jacob", "clark"]

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels for name in names."""
        for name in self.names:
            label_name = Label(text=name, id=name)
            self.root.ids.entries_box.add_widget(label_name)


DynamicLabelsApp().run()

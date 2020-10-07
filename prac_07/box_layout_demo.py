"""
CP1404/CP5632 Practical
Kivy GUI program to greet user
"""

from kivy.app import App
from kivy.lang import Builder


class GreetUserApp(App):
    """Kivy App for greeting user."""
    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle greeting function."""
        # print("greet")
        # print("test")
        # self.root.ids.output_label.text = "Hello "
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def clear_field(self):
        """Clear input and output field."""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""


GreetUserApp().run()

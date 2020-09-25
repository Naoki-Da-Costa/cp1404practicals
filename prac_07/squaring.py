"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Naoki Da Costa'


class SquareNumberApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """
    def build(self):
        """Build the Kivy app from the kv file."""
        Window.size = (200, 100)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        """Handle calculation for squaring a number."""
        result = value ** 2
        self.root.ids.output_label.text = str(result)


SquareNumberApp().run()

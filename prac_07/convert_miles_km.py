"""
CP1404/CP5632 Practical
Kivy GUI program to convert miles to kilometres
"""

from kivy.app import App
# from kivy.app import StringProperty
from kivy.lang import Builder


class MilesConverterApp(App):
    """Kivy App for converting miles to kilometres."""
    MILES_TO_KM = 1.60934
    # output = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """Handle calculation and print to label."""
        value = self.validate_input()
        result = value * MilesConverterApp.MILES_TO_KM
        # self.output = str(result)
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        """Handle up/down button press, update text input with new value, call calculation function."""
        value = self.validate_input() + change
        self.root.ids.user_input.text = str(value)
        self.handle_calculate()

    def validate_input(self):
        """If input is a string or empty return zero."""
        try:
            value = float(self.root.ids.user_input.text)
            return value
        except ValueError:
            return 0.0


MilesConverterApp().run()

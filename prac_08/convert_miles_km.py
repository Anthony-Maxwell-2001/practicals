"""
CP1404
Prac_08
convert_miles_km
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


def get_valid_number(text):
    try:
        return float(text)
    except ValueError:
        return 0.0


class ConvertMilesToKmApp(App):
    output = StringProperty()

    def build(self):
        self.title = "Convert Miles to Km"
        self.root = Builder.load_file('convert_miles_km.kv')

    def handle_calculate(self, text):
        miles = get_valid_number(text)
        self.update_output(miles)

    def handle_increment(self, text, change):
        miles = get_valid_number(text) + change
        self.root.ids.input_miles.text = str(miles)

    def update_output(self, miles):
        self.output = str(miles * 1.60934)


ConvertMilesToKmApp().run()

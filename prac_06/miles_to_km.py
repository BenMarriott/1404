from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934

class Distance_Converter_App(App):
    def build(self):
        self.title = "Miles to Kilometers Converter"
        self.root = Builder.load_file('miles_to_km.kv')
        return self.root

    def handle_conversion(self):
        value = self.get_valid_integer()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = "Miles in Kilometers: " + str(result)

    def handle_increment(self, incrementation):
        value = self.get_valid_integer() + incrementation
        self.root.ids.input_miles.text = str(value)
        self.handle_conversion()

    def get_valid_integer(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


Distance_Converter_App().run()


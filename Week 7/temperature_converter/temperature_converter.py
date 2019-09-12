from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock

from temperatures import celsius_to_fahrenheit as c_to_f
from temperatures import fahrenheit_to_celsius as f_to_c

class TemperatureConverter(App):

    def build(self):
        self.title = "Temperature Converter"
        self.root = Builder.load_file('temperature_converter.kv')
        #Clock.schedule_interval(self.update, 1.0/60.0)
        return self.root

    def handle_changes(self, changed_value):
        temp = int(self.root.ids.user_input.text)
        if(temp + changed_value <0):
            self.root.ids.user_input.text = str(temp)
        else:
            temp += changed_value
            self.root.ids.user_input.text = str(temp)
    

        

    def handle_celsius_to_fahrenheit(self, value):
        self.root.ids.converted_output.text = str(c_to_f(value))

    def handle_fahrenheit_to_celsius(self, value):
        self.root.ids.converted_output.text = str(f_to_c(value))


    def handle_validation(self, value):
        if (value <=0):
            self.root.ids.converted_output.text = "Error Invalid Value Try Again"
        else:
            self.handle_(value)


# create and start the App running
def main():
    TemperatureConverter().run()

if __name__ == "__main__":
    main()
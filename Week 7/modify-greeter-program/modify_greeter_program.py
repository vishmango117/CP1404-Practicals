from kivy.app import App
from kivy.lang import Builder


class ModifyGreeterProgram(App):
    
    def build(self):
        self.title = "Greeter Program"
        self.root = Builder.load_file('modify_greeter_program.kv')
        return self.root

    def handle_clear(self):
        self.root.ids.name_input.text = ''
        self.root.ids.output_label.text = ''


    def handle_greet(self, name):
        print("test")
        self.root.ids.output_label.text = "Hello, " + name

ModifyGreeterProgram().run()

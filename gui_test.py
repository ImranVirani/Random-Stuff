from guizero import App, Text, TextBox
app = App(title="Hello World")
welcome_message = Text(app, text="Welcome to my App")
my_name = TextBox(app)
app.display()

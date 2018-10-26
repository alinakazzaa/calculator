class Controller:

    def __init__(self, model):
        self.model = model
        self.numbersPressed = ""

    def button_pressed(self, button_label):
        if button_label ==  "C":
            self.numbersPressed = ""
            self.model.set_display("0")
        elif button_label == "Del":
            self.numbersPressed = button_label
            self.model.set_display(numbersPressed)
        else:
            self.numbersPressed += button_label
            self.model.set_display(self.numbersPressed)



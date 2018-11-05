class Controller:

    def __init__(self, model):
        self.model = model
        self.numbersPressed = ""
        self.counter = 0

    def button_pressed(self, button_label):
        if button_label ==  "C":
            self.numbersPressed = ""
            self.model.set_display("0")
        elif button_label == "Del":
             self.numbersPressed [:-1]
             self.model.set_display(self.numbersPressed)
        else:
            self.numbersPressed += button_label
            self.counter = self.counter+1
            self.model.set_display(self.numbersPressed)



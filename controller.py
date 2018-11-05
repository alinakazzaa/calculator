class Controller:

    def __init__(self, model):
        self.model = model
        self.numbersPressed = ""
        self.numsBefore = 0
        #self.numsAfter

    def button_pressed(self, button_label):
        if button_label ==  "C":
            self.numbersPressed = ""
            self.model.set_display("0")
        elif button_label == "Del" or button_label == "CE":
             self.numbersPressed = self.numbersPressed[0:-1]
             self.model.set_display(self.numbersPressed)
        elif button_label == "+":
             self.numsBefore = self.numbersPressed
             #self.numsAfter = self.number
             self.model.set_display(self.numsBefore + "+")
        else:
            self.numbersPressed += button_label
            self.model.set_display(self.numbersPressed)



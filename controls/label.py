import tkinter

class Label:
    def __init__(self, tk, text=None):

        self.tk = tk
        self.text_variable = tkinter.StringVar()
        if text is not None:
            self.text_variable.set(text)
        else:
            self.text_variable.set('<blank>')
        # self.text_variable.trace('w', self.text_updated)

        self.label = tkinter.Label(self.tk, text=self.text_variable.get())

    # def text_updated(self, *args):
        # tkinter.Label(self.tk, textvariable=self.text_variable.get())

    def set_text(self, text):
        self.text_variable.set(text)

    def pack(self):
        self.label.pack()

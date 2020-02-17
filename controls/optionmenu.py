import tkinter

class OptionMenu:
    def __init__(self, tk, options):

        self.tk = tk

        if not isinstance(options, list):
            raise TypeError(f'Parameter options must be type list; type {typeof(options)} passed instead')

        if not options:
            self.options = ['<blank>']
        else:
            self.options = options

        self.selected = tkinter.StringVar(self.tk)
        self.selected.set(self.options[0])
        self.option_menu = tkinter.OptionMenu(*(self.tk, self.selected) + tuple(self.options))

    def get_selected_option(self):
        return self.selected.get()

    def pack(self):
        self.option_menu.pack()

import tkinter

class Window:
    def __init__(self, tk=None):
        """
        Creates a Tkinter window.

        Keyword Arguments:
        tk -- An existing Tkinter instance to bind to. If no instance is
        provided, a new instance is created.
        """

        # if Tkinter instance was not provided
        if tk is None:
            # create Tkinter instance
            self.tk = tkinter.Tk()
        # otherwise
        else:
            # use provided Tkinter instance
            self.tk =  tk

    def set_title(self, title):
        """
        Sets the title of the Tkinter window.

        Arguments:
        title -- A string containing the desired window title.
        """

        # set Tkinter window title
        self.tk.title(title)
        # return Tkinter instance for method chaining
        return self

    def set_fullscreen(self, is_fullscreen):
        """
        Changes the window's fullscreen setting.

        Arguments:
        is_fullscreen -- A boolean determining fullscreen state.
        """

        # set fullscreen state of Tkinter window
        self.tk.attributes('-fullscreen', is_fullscreen)
        # return Tkinter instance for method chaining
        return self

    def set_size(self, width, height):
        """Sets the size of the Tkinter window."""

        self.tk.geometry(f'{width}x{height}')
        return self

    def set_background(self, background=""):
        """Sets the color of Tkinter window's background."""

        self.frame = tkinter.Frame(self.tk, bg=background)

    def add_keybind(self, key, method):
        """Triggers method 'action' when key is pressed."""
        self.tk.bind(key, method)

    def pack(self, menubar=None):
        """
        Packs Tkinter menubar into Frame, if provided.

        Keyword Arguments:
        menubar -- The MenuBar instance to be bound to the Window instance.
        """

        # if MenuBar instance was provided
        if menubar is not None:
            # set the window's menu to the MenuBar instance
            self.tk.config(menu=menubar)

        try:
            self.frame.pack()
        # if the Window instance's frame has not been created yet
        except AttributeError:
            self.frame = tkinter.Frame(self.tk, bg="")
            self.frame.pack()

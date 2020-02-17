import tkinter

from .menu import Menu

class MenuBar:
    def __init__(self, window):
        """
        Creates a toolbar on the Tkinter instance.

        Keyword Arguments:
        tk -- The tkinter instance to bind to. If no instance is provided, a new
        instance is created.
        """

        # get Tkinter instance from Window instance
        self.tk = window.tk

        # create a toolbar menu
        self.menubar = tkinter.Menu(self.tk)

    def add_menu(self, name):
        """Adds menu to menubar."""
        
        menu = Menu(self.menubar, name)
        return menu

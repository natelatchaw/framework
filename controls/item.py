from tkinter import Tk

class Item:
    def __init__(self, menu, name, action):
        """
        Creates an item and adds it to the menu.

        Arguments:
        menu -- The Menu instance to bind the item to.
        name -- The name of the Item instance.
        action -- The function to execute on item click.
        """

        self.menu = menu
        self.name = name
        self.action = action

        # get Tkinter instance from Menu instance
        self.tk = menu.tk

        # if action argument is callable
        if callable(action):
            # create an item in the Menu instance
            self.menu.add_command(label=name, command=lambda: action())

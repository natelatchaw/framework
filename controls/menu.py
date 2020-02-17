import tkinter

from .item import Item

class Menu:
    def __init__(self, menubar, name, tearoff=0):
        """
        Creates a menu and adds it to the menubar.

        Keyword Arguments:
        menubar -- The MenuBar instance to bind the menu to.
        name -- The name of the Menu instance.
        """

        self.name = name
        self.menubar = menubar

        # get Tkinter instance from MenuBar instance
        self.tk = menubar.tk

        # create a menu in the Menubar instance
        self.menu = tkinter.Menu(menubar, tearoff=tearoff)
        self.menubar.add_cascade(label=self.name, menu=self.menu)

    def add_item(self, name, action):
        item = Item(self.menu, name, action)
        return item

import os

from .folder import Folder
from .module import Module
from ..formats.configuration import Configuration

class Directory(Folder):
    """Represents a directory on disk containing other folders."""
    def __init__(self, path, ignored_folders=[], ignored_modules=[]):
        """
        Creates a representation of a folder of folders.

        Arguments:
        path -- a string containing a path to the target folder. Any valid path
        representation can be provided (both relative path and absolute path).
        """

        super().__init__(path)
        # initialize modules and folders lists
        self.folders = []
        self.modules = []

        self.ignored_folders = ignored_folders
        self.ignored_modules = ignored_modules

        # set default class name (None uses the module's filename)
        self.default_class_name = None

        # set default config_path
        self.config_path = os.path.join(self.directory, 'folders.ini')
        self.configuration = Configuration(self.config_path)

    def get_property(self, property, fallback=None):
        """
        Returns a property of the instance.

        Arguments:
        property -- The name of the property to return. The instance if checked
        for an attribute of the name contained in 'property' first; if that
        fails, the configuration file is checked for an entry with the name
        contained in 'property'.
        Keyword Arguments:
        fallback -- If the two sources above fail to contain the name contained
        in property, the value of fallback will be returned. If fallback is not
        provided, None is returned.
        """

        # get 'property' attribute
        property_value = getattr(self, property, '')
        # if string representation of property from instance attribute is an empty string
        if len(str(property_value).strip()) == 0:
            # get property from configuration file
            property_value = self.configuration.get_keyvalue(self.name, property)

        # if string representation of property from configuration file if an empty string
        if len(str(property_value).strip()) == 0:
            property_value = fallback

        setattr(self, property, property_value)

        return property_value

    def set_config(self, config_path):
        """Allows the location of the configuration file to be changed."""

        self.config_path = config_path

    def set_ignored_objects(self, ignored_folders=[], ignored_modules=[]):
        """Defines a list of directories to pass over when parsing."""

        if not isinstance(ignored_folders, list):
            raise TypeError(f'Parameter ignored_folders must be list type, {type(ignored_folders)} type passed instead')
        self.ignored_folders = ignored_folders

        if not isinstance(ignored_modules, list):
            raise TypeError(f'Parameter ignored_modules must be list type, {type(ignored_modules)} type passed instead')
        self.ignored_modules = ignored_modules

    def parse(self):
        """Programmatically scans subfolders and their contents for modules."""

        # for each file or folder object in directory
        for item in self.contents:
            # assemble item path
            item_path = os.path.join(self.abspath, item)

            # if the item is a directory
            if os.path.isdir(item_path) and item not in self.ignored_folders:
                # create Directory instance from item
                directory = Directory(item_path, ignored_folders=self.ignored_folders, ignored_modules=self.ignored_modules)
                # check if directory is valid
                if directory.valid:
                    # get metadata for directory
                    directory.get_config_properties()
                    # parse directory's contents
                    directory.parse()
                    # add directory to self.folders
                    self.folders.append(directory)

            # if the item is not a directory
            elif not os.path.isdir(item_path) and item not in self.ignored_modules:
                # create Module instance from item
                module = Module(item_path)
                # check if module is valid
                if module.valid:
                    # get metadata for module
                    module.get_config_properties()
                    # get the module's default class from name
                    module.get_class(class_name=self.default_class_name)
                    # add module to self.modules
                    self.modules.append(module)

    def get_config_properties(self):
        self.configuration.read()
        self.metadata = self.configuration.get_section(self.name)
        self.configuration.write()

        for key, value in self.metadata.items():
            # don't overwrite existing attributes
            if not hasattr(self, key):
                setattr(self, key, value)

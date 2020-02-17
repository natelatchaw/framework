import os
import sys
import inspect
from importlib import import_module

from .file import File
from ..formats.configuration import Configuration
from ...development.output import Output
from ...development.development import Development

class Module(File):
    """Represents a Python module, and by extension, a file on disk."""
    def __init__(self, path):
        """
        Creates a representation of a Module object as an extension of a File object.

        Arguments:
        path -- a string containing a path to the target file. Any valid path
        representation can be provided (both relative path and absolute path).
        """

        # call parent class' constructor
        super().__init__(path)

        # mark Module instance as invalid if it does not have a valid extension
        extensions = ['.py', '.pyw']
        if self.extension not in extensions:
            self.valid = False
            return
        else:
            self.valid = True

        self.config_path = os.path.join(self.directory, 'modules.ini')
        self.configuration = Configuration(self.config_path)

        # get relative import string
        self.relative_path = os.path.relpath(os.path.join(self.directory, self.name))
        self.relative_norm_path = os.path.normpath(self.relative_path)
        self.relative_import_path = self.relative_norm_path.replace(os.path.sep, '.')

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

    def get_config_properties(self):
        """
        Sets all entries in configuration file as instance attributes.

        Parses the associated section in the modules configuration file and
        obtains all fields in the form of a dictionary. The dictionary is then
        iterated over and each key/value pair is set as an instance attribute,
        unless the instance already has an attribute of the name contained in
        'key'.
        """

        self.configuration.read()
        properties = self.configuration.get_section(self.name)

        for key, value in properties.items():
            if not hasattr(self, key):
                setattr(self, key, value)

    def get_class(self, class_name=None, tk=None):
        """
        Returns a class from the module.

        Arguments:
        relative_path -- the path relative to the current working directory to
        import the Module instance from.
        Keyword Arguments:
        class_name -- The name of the class to be retrieved. If no name is
        specified, the class with the same name as the module will be returned.
        If no class matching the value in class_name is found, None is returned.
        """

        if not self.valid:
            return None

        try:
            imported_module = import_module(self.relative_import_path)
            # for each member in imported_module where the member is a class member
            for name, obj in inspect.getmembers(imported_module, lambda member: inspect.isclass(member)):
                # if the lowercase name of the class matches the lowercase name of the module
                if name.lower() == self.name.lower():
                    class_name = name
                # naive method
                elif class_name is None:
                    class_name = self.name.title()
            imported_class = getattr(imported_module, class_name)
            imported_class.tk = tk
        except ModuleNotFoundError as moduleNotFoundError:
            self.valid = False
            print(moduleNotFoundError)
            return None
        except AttributeError as attributeError:
            self.valid = False
            print(attributeError)
            return None

        return imported_class

    def get_attribute(self, attribute_name, class_name=None):
        """Returns a class attribute from a class in the module.

        Arguments:
        attribute_name -- The name of the class attribute to be retrieved. If no
        class attribute matching the value in attribute_name is found, None is
        returned.
        class_name -- The name of the class to retrieve the class attribute
        from. If no class matching the value in class_name is found, None is
        returned.
        """
        imported_class = self.get_class(class_name=class_name)

        if imported_class is None:
            return None

        try:
            attribute = getattr(imported_class, attribute_name)
        except AttributeError:
            return None

        return attribute

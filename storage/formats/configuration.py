import os
import configparser

class Configuration():
    def __init__(self, path):
        self.configuration = configparser.ConfigParser()

        self.path = path
        self.parent_folder = os.path.dirname(self.path)
        if not os.path.isdir(self.parent_folder):
            os.mkdir(self.parent_folder)
        if not os.path.exists(self.path):
            self.preexisting = False
            with open(self.path, 'w') as configuration_file:
                self.configuration.write(configuration_file)
        else:
            self.preexisting = True
        self.configuration.read(self.path)
        self.abspath = os.path.abspath(path)

    def setup(self, dictionary=None, list=None):
        # TODO: Add support for interactive value entry when values are missing
        # TODO: Add support for using lists, dictionaries, or other formats
        if dictionary:
            self.configuration.read_dict(dictionary)
        elif list:
            # TODO: add support for lists
            pass

    def load_dict(self, dict):
        self.configuration.read_dict(dict)

    def read(self):
        self.configuration.read(self.path)

    def write(self):
        with open(self.path, 'w') as configuration_file:
            self.configuration.write(configuration_file)

    def add_keypairs(self, section, dict):
        """Adds keypairs from dictionary to config section"""
        if not self.configuration.has_section(section):
            self.configuration.add_section(section)
        for key, value in dict.items():
            self.configuration[section][key] = value

    def get_keyvalue(self, section, key):
        # if the section in the section parameter does not exist
        if not self.configuration.has_section(section):
            # create the section
            self.configuration.add_section(section)
        if not self.configuration.has_option(section, key):
            self.configuration[section][key] = ''
        return self.configuration[section][key]

    def get_section(self, section):
        if section == 'DEFAULT':
            return None
        # if the section in the section parameter does not exist
        if not self.configuration.has_section(section):
            # create the section
            self.configuration.add_section(section)
            self.write()
        section_keypairs = self.configuration.items(section)
        section_dict = {}
        for section_keypair in section_keypairs:
            # get key from section keypair
            key = section_keypair[0]
            # try to get integer from section/key
            try:
                value = self.configuration.getint(section, key, fallback=None)
            except ValueError:
                # try to get float from section/key
                try:
                    value = self.configuration.getfloat(section, key, fallback=None)
                except ValueError:
                    # try to get boolean from section/key
                    try:
                        value = self.configuration.getboolean(section, key, fallback=None)
                    except ValueError:
                        # try to get other type of value from section key
                        value = self.configuration.get(section, key, fallback=None)

            # set key and value in section_dict
            section_dict[key] = value
        return section_dict

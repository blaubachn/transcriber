from configparser import ConfigParser
from os.path import isfile, expanduser

class Configuration_Manager:
    def __init__(self, config_file):
        self.config_file = config_file
        if not isfile(self.config_file):
            print('Config file not setup')
            print('Please change the default values in the settings editor')
            self.set_config_defaults()

    def get_config(self):
        config = ConfigParser()
        config.read(self.config_file)
        return {
            'username': config.get('credentials', 'username'),
            'password': config.get('credentials', 'password'),
            'speech'  : config.get('directories', 'speech'),
            'text'    : config.get('directories', 'text')
        }

    def set_config(self, username, password, speech, text):
        new_config = ConfigParser()
        new_config.add_section('credentials')
        new_config.set('credentials', 'username', username)
        new_config.set('credentials', 'password', password)
        new_config.add_section('directories')
        new_config.set('directories', 'speech', speech)
        new_config.set('directories', 'text', text)
        with open(self.config_file, 'w') as configfile:
            new_config.write(configfile)

    def update_config(self, section, key, value):
        config = ConfigParser()
        config.read(self.config_file)
        config.set(section, key, value)
        with open(self.config_file, 'w') as configfile:
            config.write(configfile)

    def update_username(self, value):
        self.update_config('credentials', 'username', value)

    def update_password(self, value):
        self.update_config('credentials', 'password', value)

    def update_speech_directory(self, value):
        self.update_config('directories', 'speech', value)

    def update_text_directory(self, value):
        self.update_config('directories', 'text', value)

    def set_config_defaults(self):
        self.set_config('<username>', '<password>', expanduser("~"), expanduser("~"))

    def print_config(self):
        print('Current Configuration:')
        for key, value in self.get_config().items(): 
            print(key.ljust(9) + ': ' + value)
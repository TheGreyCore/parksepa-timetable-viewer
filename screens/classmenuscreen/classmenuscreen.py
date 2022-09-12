from kivymd.uix.screen import MDScreen
import configparser
from kivy.lang import Builder
config = configparser.ConfigParser()

class ClassMenuScreen(MDScreen):
    
    def change_class(self, var_class):
        config['SETTINGS'] = {'Class_ID': f'{var_class}'}
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

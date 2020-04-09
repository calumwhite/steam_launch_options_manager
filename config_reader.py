import json
import os

import initialise


class config_reader:
    def read_config(self, file_name):
        try:
            initialise
            with open(file_name, 'r') as file:
                config = json.load(file)

            self.steam_path = config["path"]
            self.rules = config["rules"]
            return True
        except:
            return False

    def read(self):
        xdg = False
        root = os.getenv("XDG_CONFIG_HOME")
        if root != None:
            xdg = True

        if xdg:
            config_path = root + "/steam_launch_options_manager.config"
            status = self.read_config(config_path)
            if status:
                return

        root = os.getenv("HOME") + "/.config"
        config_path = root + "/steam_launch_options_manager.config"
        status = self.read_config(config_path)
        if status:
            return

        print(
            "No config for steam launch options manager found. Starting initialization. \n")
        initialise.initialise().initialise()


config_reader().read()

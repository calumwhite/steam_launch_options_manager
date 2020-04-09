import os
import json
import time

import steam_config_utils
import main


class config_manager:

    def gather_options(self):
        options = {}

        print("\n Initializing configuration and backup location for Steam Launch Options Manager \n")

        self.steam_config_getter = steam_config_utils.config_getter()
        path = self.steam_config_getter.get_file_name()
        options["path"] = path

        while True:
            value = input(
                "What is the first rule you want to add. 1. Enable Nvidia Optimus , 2. Add generic strings \n")
            if value == "1":
                options["rules"] = {"optimus": None}
                break
            elif value == "2":
                strings = input(
                    "Please insert the strings you want to add space seperated \n").split()
                options["rules"] = {"generic_string": strings}
                break

        while True:
            another_rule = input("No you want to add another rule y/n \n")
            if another_rule == "n":
                break
            elif another_rule == "y":
                value = input(
                    "What is the first rule you want to add. 1. Enable Nvidia Optimus , 2. Add generic strings \n")
                if value == "1":
                    options["rules"]["optimus"] = None
                elif value == "2":
                    strings = input(
                        "Please insert the strings you want to add space seperated. This will overwrite any generic strings entered before \n").split()
                    options["rules"]["generic_string"] = strings

        return options

    def save_options(self, options):
        config_path = self.get_config_path()

        print("Saving config options to " + config_path + "\n")
        json.dump(options, open(config_path, "w"))

    def get_config_path(self):
        root = os.getenv("XDG_CONFIG_HOME")
        if root == None:
            root = os.getenv("HOME") + "/.config"

        config_path = root + "/steam_launch_options_manager.config"
        return config_path


class initialise():

    def get_backup_path(self):
        root = os.getenv("XDG_DATA_HOME")
        if root == None:
            root = os.getenv("HOME") + "/.local/share"

        path = root + "/steam_launch_options_manager"
        return path

    def initialise(self):
        config_controller = config_manager()
        options = config_controller.gather_options()
        config_controller.save_options(options)

        data = config_controller.steam_config_getter.open_file(
            config_controller.steam_config_getter.config_name)
        config_controller.steam_config_getter.backup_config(
            data, self.get_backup_path(), "localconfig.vdf.backup"+str(int(time.time())))

        print("starting main program")
        main.main()


if __name__ == "__main__":
    initialise().initialise()

import vdf
import os


class config_getter:
    def save_file(self, data, path=None):
        if path == None:
            path = self.config_name
        vdf.dump(data, open(path, "w"), pretty=True)

    def get_file_name(self):
        while True:
            value = input(
                "Do you want to try and auto-detect location of localconfig.vdf? y/n \n")
            if value == "n":
                auto_detect = False
                break
            elif value == "y":
                auto_detect = True
                break

        if auto_detect:
            path = self.autodetect()
            if path == None:
                auto_detect = False

        if not auto_detect:
            while True:
                path = input(
                    "Please input path to localconfig.vdf \n the path should look something like $HOME/.steam/[distro specific path]/userdata/[id number]/config/localconfig.vdf \n")

                try:
                    with open(path) as f:
                        # print(f.readlines())
                        break
                except IOError:
                    print("File doesn't exist \n")

        self.config_name = path
        return path

    def autodetect(self):
        return "/home/calum/.steam/debian-installation/userdata/89980527/config/localconfig.vdf"

    def open_file(self, file_name):
        with open(file_name, 'r') as file:
            config = vdf.load(file)
        return config

    def backup_config(self, data, folder, file_name):
        # creates backup config directory
        try:
            os.mkdir(folder)
        except FileExistsError:
            pass

        print("Backing up to " + folder + "/" + file_name + "\n")
        self.save_file(data, folder + "/" + file_name)

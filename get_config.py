import vdf


class config_getter:
    def __init__(self):
        self.config_name = self.get_file_name()

    def get_file_name(self):
        return "/home/calum/.steam/debian-installation/userdata/89980527/config/localconfig.vdf"

    def open_file(self):
        with open(self.config_name, 'r') as file:
            config = vdf.load(file)
            pass
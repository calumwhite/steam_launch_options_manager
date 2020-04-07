import pathlib

import get_config
import modify_config


def main():
    p = get_config.config_getter()
    data = p.open_file()
    # creates backup first
    print("Creating backup at " + str(pathlib.Path().absolute()) +
          "/backup/localconfig.vdf")
    p.save_file(data, str(pathlib.Path().absolute())+"/backup/localconfig.vdf")
    modifer = modify_config.modifier([modify_config.enable_optimus()])
    modifer.modify(data)
    pass


main()

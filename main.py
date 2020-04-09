import pathlib

import steam_config_utils
import modify_config


def main():
    p = steam_config_utils.config_getter()
    data = p.open_file()
    # creates backup first
    print("Creating backup at " + str(pathlib.Path().absolute()) +
          "/backup/localconfig.vdf")
    p.save_file(data, str(pathlib.Path().absolute())+"/backup/localconfig.vdf")
    modifer = modify_config.modifier(
        [modify_config.enable_optimus()])
    modifer.modify(data)
    print("Saving modified file")
    p.save_file(data)
    pass


main()

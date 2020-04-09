import time

import steam_config_utils
import modify_config
import config_reader
import initialise


def main():
    # read in config for steam launch options manger
    config = config_reader.config_reader()
    config.read()
    # read in steam config
    p = steam_config_utils.config_getter()
    data = p.open_file(config.steam_path)
    # create backup
    p.backup_config(data, initialise.initialise().get_backup_path(),
                    "localconfig.vdf.backup"+str(int(time.time())))
    # modify steam backup
    modifer = modify_config.modifier(config.rules)
    modifer.modify(data)
    print("Saving modified file")
    p.save_file(data, config.steam_path)
    pass


if __name__ == "__main__":
    main()

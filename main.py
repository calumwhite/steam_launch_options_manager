import get_config
import modify_config


def main():
    p = get_config.config_getter()
    game = p.open_file()
    modifer = modify_config.modifier([modify_config.enable_optimus()])
    modifer.modify(game)


main()

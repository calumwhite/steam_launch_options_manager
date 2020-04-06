import get_config


def main():
    p = get_config.config_getter()
    p.open_file()


main()

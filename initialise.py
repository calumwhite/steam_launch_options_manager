import os
import json

import get_config


def gather_options():
    options = {}

    print("\n Initializing configuration and backup location for Steam Launch Options Manager \n")

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
        path = get_config.config_getter().auto_detect()

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
    options["path"] = path

    while True:
        value = input(
            "What is the first rule you want to add. 1. Enable Nvidia Optimus , 2. Add generic strings \n")
        if value == "1":
            options["rules"] = ["optimus"]
            break
        elif value == "2":
            strings = input(
                "Please insert the strings you want to add space seperated \n").split()
            options["rules"] = [strings]
            break

    while True:
        another_rule = input("No you want to add another rule y/n \n")
        if another_rule == "n":
            break
        elif another_rule == "y":
            value = input(
                "What is the first rule you want to add. 1. Enable Nvidia Optimus , 2. Add generic strings \n")
            if value == 1:
                options["rules"].append("optimus")
                break
            elif value == 2:
                strings = input(
                    "Please insert the strings you want to add space seperated \n").split()
                options["rules"].append(strings)
                break

    return options


def save_options(options):
    config_path = os.environ("XDG_CONFIG_HOME")
    if config_path == None:
        config_path = "$HOME/.config"
    json.dump(options, open(config_path, "w"))


def initialise():
    options = gather_options()
    save_options(options)


initialise()

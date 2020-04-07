class modifier:
    def __init__(self, rules):
        self.rules = rules

    def modify(self, game):
        for rule in self.rules:
            rule.run(game)


class add_to_LaunchOptions:
    def __init__(self, strings_to_add):
        self.strings_to_add = strings_to_add

    def run(self, data):
        installed_ids = list(
            data["UserLocalConfigStore"]["UserAppConfig"].keys())
        game_list = data["UserLocalConfigStore"]["Software"]["Valve"]["Steam"]["apps"]

        # iterate over installed games
        for id in [id for id in game_list.keys() if id in installed_ids]:
            if "LaunchOptions" in game_list[id].keys():
                LaunchOptions_initial = game_list[id]["LaunchOptions"].split()
            else:
                LaunchOptions_initial = []

            LaunchOptions_final = []

            # add new strings
            for string in self.strings_to_add:
                if string not in LaunchOptions_initial:
                    LaunchOptions_final.append(string)

            # keep old strings
            for string in LaunchOptions_initial:
                LaunchOptions_final.append(string)

            # ensure if there are custom commands that the generic command is added
            if r"%command%" not in LaunchOptions_final:
                LaunchOptions_final.append(r"%command%")

            # convert back to string
            LaunchOptions_string = " ".join(LaunchOptions_final)
            game_list[id]["LaunchOptions"] = LaunchOptions_string


class enable_optimus(add_to_LaunchOptions):
    def __init__(self):
        strings_to_add = ["__NV_PRIME_RENDER_OFFLOAD=1",
                          "__GLX_VENDOR_LIBRARY_NAME=nvidia"]
        super().__init__(strings_to_add)

class modifier:
    def __init__(self, rules):
        self.processed_rules = []
        for rule, params in rules.items():
            self.process_rule(rule, params)

    def modify(self, game):
        for rule in self.processed_rules:
            rule.run(game)

    def process_rule(self, rule, params):
        if rule == "optimus":
            self.processed_rules.append(enable_optimus())
        elif rule == "generic_string":
            self.processed_rules.append(add_to_LaunchOptions(params))


class add_to_LaunchOptions:
    def __init__(self, strings_to_add, only_installed_games=False):
        self.strings_to_add = strings_to_add
        self.only_installed_games = False

    def run(self, data):
        game_list = data["UserLocalConfigStore"]["Software"]["Valve"]["Steam"]["apps"]
        if self.only_installed_games:
            installed_ids = list(
                data["UserLocalConfigStore"]["UserAppConfig"].keys())

            # iterate over installed games
            for id in [id for id in game_list.keys() if id in installed_ids]:
                self.modify_game(game_list, id)

        else:
            for id in game_list.keys():
                self.modify_game(game_list, id)

    def modify_game(self, game_list, id):
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
    def __init__(self, only_installed_games=False):
        strings_to_add = ["__NV_PRIME_RENDER_OFFLOAD=1",
                          "__GLX_VENDOR_LIBRARY_NAME=nvidia"]
        super().__init__(strings_to_add, only_installed_games)

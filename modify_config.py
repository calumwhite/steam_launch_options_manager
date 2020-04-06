class modifier:
    def __init__(self, rules):
        self.rules = rules

    def modify(self, game):
        for rule in self.rules:
            rule.run(game)


class add_to_LaunchOptions:
    def __init__(self, string_to_add):
        self.string_to_add = string_to_add


class enable_optimus:
    def run(self, game):
        pass

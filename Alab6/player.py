class Player:
    def __init__(self, name):
        self._name = name
        self._scoreboard = {}

        self._top_score = 0
        self._bottom_score = 0
        self._bonus_bottom = 0
        self._total_score = 0

    def add_rolled(self, rolled_type , value):
        self._scoreboard[rolled_type] = value

    def add_top_score(self,value):
        self._top_score += value
    def add_top_bonus(self):
        needed_score_for_bonus = 63

        if self.get_top_score() >= needed_score_for_bonus:
            self._scoreboard['top_bonus'] = 50
        else:
            self._scoreboard['top_bonus'] = 0

        self._top_bonus = self._scoreboard['top_bonus']

    def get_top_score(self):
        return self._top_score

    def print_scoreboard(self):
        for key, value in self._scoreboard.items():
            print (f'{key} : {value}')
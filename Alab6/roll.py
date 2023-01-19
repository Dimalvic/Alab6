import random

class Roll:
    def __init__(self):
        self._current_dice_list = []
        self._current_kept_dice = []


    def roll_dice(self):
        self._current_kept_dice.clear()
        self._current_dice_list = [random.randint(1,6) for die in range(0,5)]
        print (f'you rolled {self._current_dice_list} ! \n')
        return self._current_dice_list

    def keep_dice(self):
        keep_input = input('which dice do you want to keep(use , between dices if you want to save more than one dice || press space if you want to roll all dices again) ')
        split_input = keep_input.split(',')

        if keep_input == '':
            return self._current_dice_list

        split_input_int = [int(item) for item in split_input]

        for die in split_input_int:
            self._current_kept_dice.append(die)

        for value in split_input_int:
            if value in self._current_dice_list:
                self._current_dice_list.remove(value)

        return self._current_dice_list


    def reroll_dice(self, dice_list):
        self._current_dice_list = [random.randint(1,6) for die in range(0,(len(dice_list)))]
        print (f'You rolled {self._current_dice_list} ! \n')
        return self._current_dice_list

    def get_current_dice(self):
        return self._current_dice_list

    def get_kept_dice(self):
        return self._current_kept_dice

    def forced_keep(self,dice_list):
        for die in dice_list:
            self._current_kept_dice.append(die)



    def single_values(self,dice_list,check_value):
        roll_score = 0
        for die in dice_list:
            if die == check_value:
                roll_score +=die
        return roll_score


    def check_one_pair(self, dice_list):
        pass

    def check_two_pairs(self, dice_list):
        dice_list.sort()
        if (dice_list[0] == dice_list[1] and dice_list[2] == dice_list[3]) or (dice_list[0] == dice_list[1] and dice_list[3] == dice_list[4]) or (dice_list[1] == dice_list[2] and dice_list[3] == dice_list[4]):
           return True
        return False

    def check_three_kind(self, dice_list):
        dice_list.sort()
        if dice_list[0] == dice_list[3] or dice_list[1] == dice_list[4]:
            return True
        return False

    def check_four_kind(self, dice_list):
        dice_list.sort()
        if dice_list[0] == dice_list[3] or dice_list[1] == dice_list[4]:
            return True
        return False

    def check_low_straight(self, dice_list):
        dice_list.sort()
        if len(set(dice_list)) == 5 and dice_list[4] == 5:
            return True

        return False

    def check_high_straight(self, dice_list):
        dice_list.sort()
        if len(set(dice_list)) == 5 and dice_list[4] == 6:
            return True

        return False

    def check_full_house(self,dice_list):
        dice_list.sort()

        if (len(set(dice_list))) != 2:
            return False

        elif dice_list[0] != dice_list[3] or dice_list[1] != dice_list[4]:
            return True

        return False

    def add_chance(self, dice_list):
        pass


    def check_yatzy(self, dice_list):
        if len(set(dice_list)) == 1:
            return True

        return False
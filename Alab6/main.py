from player import Player
from roll import Roll

def main():
    game_list_top = ['aces' , 'twos' , 'threes' , 'fours' , 'fives' , 'sixes']
    game_list_top_values = [1,2,3,4,5,6]

    player1 = Player('Dmytro')
    dice1 = Roll()

    for index,item in enumerate(game_list_top):
        print ('-'*40)
        print (f'rolling for {item}')
        print ('-'*40)

        dice1.roll_dice()
        keep1 = dice1.keep_dice()

        dice1.reroll_dice(keep1)
        keep2 = dice1.keep_dice()

        roll3 = dice1.reroll_dice(keep2)
        dice1.forced_keep(roll3)

        final_roll_collection = dice1.get_kept_dice()

        print (f'final roll collection: {final_roll_collection}')

        check_score = dice1.single_values(final_roll_collection,game_list_top_values[index] )

        player1.add_rolled(item , check_score)
        player1.add_top_score(check_score)

    player1.add_top_bonus()

    player1.print_scoreboard()

main()
import json
from datetime import datetime
import random

def first_player():
    print('Player 1, your turn: ')
    return random.randint(1, 6) + random.randint(1, 6)


def second_player():
    print('Player 2, your turn: ')
    return random.randint(1, 6) + random.randint(1, 6)


def main():
    start = input('Start game yes|no')
    player_1_sum = 0
    player_2_sum = 0
    new_dict = {'Round 1': {'player_1_name': "Player1", 'player_1_time': None, 'player_1_res': None, 'player_2_name': "Player2", 'player_2_time': None, 'player_2_res': None},
                'Round 2': {'player_1_name': "Player1", 'player_1_time': None, 'player_1_res': None, 'player_2_name': "Player2", 'player_2_time': None, 'player_2_res': None},
                'Round 3': {'player_1_name': "Player1", 'player_1_time': None, 'player_1_res': None, 'player_2_name': "Player2", 'player_2_time': None, 'player_2_res': None},
                'Round 4': {'player_1_name': "Player1", 'player_1_time': None, 'player_1_res': None, 'player_2_name': "Player2", 'player_2_time': None, 'player_2_res': None},
                'Round 5': {'player_1_name': "Player1", 'player_1_time': None, 'player_1_res': None, 'player_2_name': "Player2", 'player_2_time': None, 'player_2_res': None},
                'Round 6': {'player_1_name': "Player1", 'player_1_time': None, 'player_1_res': None, 'player_2_name': "Player2", 'player_2_time': None, 'player_2_res': None},
                'Round 7': {'player_1_name': "Player1", 'player_1_time': None, 'player_1_res': None, 'player_2_name': "Player2", 'player_2_time': None, 'player_2_res': None},
                'Round 8': {'player_1_name': "Player1", 'player_1_time': None, 'player_1_res': None, 'player_2_name': "Player2", 'player_2_time': None, 'player_2_res': None},
                'Round 9': {'player_1_name': "Player1", 'player_1_time': None, 'player_1_res': None, 'player_2_name': "Player2", 'player_2_time': None, 'player_2_res': None},
                'Round 10': {'player_1_name': "Player1", 'player_1_time': None, 'player_1_res': None, 'player_2_name': "Player2", 'player_2_time': None, 'player_2_res': None}
                }
    if start == 'yes':
        counter = 1
        while counter < 11:
            player_1_value = first_player()
            print(player_1_value)
            player_2_value = second_player()
            print(player_2_value)
            if player_1_value == player_2_value:
                continue
            player_1_sum += player_1_value
            player_2_sum += player_2_value
            new_dict['Round ' + str(counter)]['player_1_time'] = str(datetime.now())
            new_dict['Round ' + str(counter)]['player_1_res'] = player_1_value
            new_dict['Round ' + str(counter)]['player_2_time'] = str(datetime.now())
            new_dict['Round ' + str(counter)]['player_2_res'] = player_2_value
            counter += 1

        with open('new_file.json', 'w') as file:
            json.dump(new_dict, file, indent=4)

        if player_1_sum > player_2_sum:
            print('First player won')
            print(player_1_sum)
            print(player_2_sum)
            return

        if player_1_sum == player_2_sum:
            print('Draw')
            print(player_1_sum)
            print(player_2_sum)
            return

        print('Second player won')
        print(player_1_sum)
        print(player_2_sum)

main()

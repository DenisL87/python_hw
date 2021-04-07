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

            counter += 1

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




# import random
# new_dict = {'round1': {'player1name': "Player1", 'player2name': "Player2", 'player1res': None, 'player2res': None},
#             'round2': {'player1name': "Player1", 'player2name': "Player2", 'player1res': None, 'player2res': None},
#             'round3': {'player1name': "Player1", 'player2name': "Player2", 'player1res': None, 'player2res': None}
#             }


# for i in new_dict:
#   new_dict[i]['player1res'] = random.randint(1, 6) + random.randint(1, 6)
#   new_dict[i]['player2res'] = random.randint(1, 6) + random.randint(1, 6)

# print(new_dict)

table = [" " for _ in range(9)]

def show_table(table):
    print(" " + table[0] + " | " + table[1] + " | " + table[2])
    print("---|---|---")
    print(" " + table[3] + " | " + table[4] + " | " + table[5])
    print("---|---|---")
    print(" " + table[6] + " | " + table[7] + " | " + table[8])

player = "X"
is_game_over = False


def check_is_over(player):
    odds_of_winning = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (3, 6, 9), (2, 5, 8), (1, 5, 9), (3, 5, 7)]
    for odd in odds_of_winning:
        if table[odd[0]-1] == table[odd[1]-1] == table[odd[2]-1] == player:
            return True
    return False


def player_turn(turn):
    global is_game_over
    played = False
    while not played:
        show_table(table)
        player_move = input(f"{turn}, make your move. (1-9): ")
        if player_move.isdigit() and 0 < int(player_move) < 10 and table[int(player_move)-1]==" ":
            table[int(player_move)-1] = turn
            if check_is_over(player):
                print(f"{turn} wins")
                is_game_over = True
            else:
                turn = "O" if turn == "X" else "X"
        else:
            print("Please enter a valid number. (1-9): ")
            played = False

while not is_game_over:
    player_turn(player)
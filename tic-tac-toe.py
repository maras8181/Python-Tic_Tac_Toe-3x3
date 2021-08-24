#Function of winner or draw
def check_winner_2(status, player, move):
    if not status and move == 9:
        print(f"{separator}\n {'Draw.': ^40}\n{separator}")
    elif status:
        winner_message = f"Player {player} won. Game Over."
        print(f"{separator}\n{winner_message: ^40}\n{separator}")

#Function of printing topical game field
def print_field():
    for field in game_field:
        print(f"{''.join(field):^40}")

#Function of checking positions with the same char(s)
def check_winner(game_field, game_status, player):
    for index_line, char_line in enumerate(game_field):
        for index_column, char_column in enumerate(char_line):
            if not index_line % 2 == 0:
                if player == game_field[index_line][2] == game_field[index_line][6] == game_field[index_line][10]:
                    game_status = True
                elif index_column == 2:
                    if player == game_field[1][index_column] == game_field[3][index_column] == game_field[5][index_column]:
                        game_status = True
                elif index_column == 6:
                    if player == game_field[1][index_column] == game_field[3][index_column] == game_field[5][index_column]:
                        game_status = True
                elif index_column == 10:
                    if player == game_field[1][index_column] == game_field[3][index_column] == game_field[5][index_column]:
                        game_status = True
                elif player == game_field[1][10] == game_field[3][6] == game_field[5][2]:
                    game_status = True
                elif player == game_field[1][2] == game_field[3][6] == game_field[5][10]:
                    game_status = True
    return game_status

#Function of printing game field on start
def game_area():
    char = None
    for x in range(7):
        chars = []
        for y in range(13):
            if y % 4 == 0:
                char = '+' if x % 2 == 0 else '|'
                chars.append(char)
            else:
                char = '-' if x % 2 == 0 else ' '
                chars.append(char)
        game_field.append(chars)
    for game_line in game_field:
        print(f"{''.join(game_line):^40}")

#Function of printing Game Rules
def game_rules(options):
    for option in options:
        print(f"* {option}")

game_field = []
separator = "=" * 40
separator_2 = '-' * 40
def main():
    print(f"Welcome to Tic Tac Toe\n{separator}")
    print(f"{'GAME RULES:': ^40}")
    print("""Each player can place one mark (or stone)\nper turn on the 3x3 grid. The WINNER is\nwho succeeds in placing three of their\nmarks in a:""")
    game_rules(options=['horizontal,', 'vertical or', 'diagonal row'])
    game_start = "Let's start the game"
    print(f"{separator}\n{game_start:^40}\n{separator_2}")
    game_area()
    move = 0
    positions = ((1, 2), (1, 6), (1, 10), (3, 2), (3, 6), (3, 10), (5, 2), (5, 6), (5, 10))
    game_status = False
    status = None
    while True:
        player = 'X' if move % 2 == 0 else 'O'
        entry = input(f"Player {player} | Please enter your move number: ")
        try:
            entry = int(entry)
            if entry not in tuple(range(1, 10)):
                print("Your entry is not in the range.")
            else:
                entry -= 1
                if game_field[positions[entry][0]][positions[entry][1]] == ' ':
                    game_field[positions[entry][0]][positions[entry][1]] = player
                    move += 1
                    status = check_winner(game_field, game_status, player)
                else:
                    print("This field is occupied. Try it again...")
        except ValueError as e:
            print(f"{e.__class__.__name__}: Your entry is not a number.")
        print_field()
        check_winner_2(status, player, move)
        if move == 9 or status:
            exit()

if __name__ == "__main__":
    main()
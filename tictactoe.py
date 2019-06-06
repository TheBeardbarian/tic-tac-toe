'''Tic-Tac-Toe Game for 2 Players

Python:
    - 3.7

Usage:
    - $python tictactoe.py

Rules:
    1. First player selects either "X" or "O" as their player token, second player gets the remaining token.
    2. Players take turns placing their token in a space on the board, one space at a time.
    3. If, at any time, a player has three consecutive tokens horizontally, vertically, or diagonally, that player is the winner. If all spaces are occupied and neither player has three consecutive tokens, the game ends in a draw.
'''


import os


class Player:
    def __init__(self, token):
        self.token = token
        self.spaces = []
        self.win = False

    def take_turn(self):
        global board
        choice = input(f'Player {self.token.title()}, choose a space! ')
        while True:
            if choice not in all_spaces:
                choice = input("That's not a valid space! Please choose again. ")
            elif choice in chosen_spaces:
                choice = input("That space has already been chosen! Please choose again. ")
            else:
                break
        self.spaces.append(choice)
        chosen_spaces.append(choice)

        line2_split = list(board[1])
        line5_split = list(board[4])
        line8_split = list(board[7])
        if choice in line2_split:
            index = line2_split.index(choice)
            line2_split[index] = self.token.title()
            line2 = "".join(line2_split)
            board[1] = line2
        elif choice in line5_split:
            index = line5_split.index(choice)
            line5_split[index] = self.token.title()
            line5 = "".join(line5_split)
            board[4] = line5
        else:
            index = line8_split.index(choice)
            line8_split[index] = self.token.title()
            line8 = "".join(line8_split)
            board[7] = line8
        _ = os.system('cls' if os.name == 'nt' else 'clear')
        for line in board:
            print(line)


    def detect_winner(self):
        for combo in winning_combos:
            if combo[0] in self.spaces and combo[1] in self.spaces and combo[2] in self.spaces:
                self.win = True
            else:
                continue

def tictactoe():
    response = input("Would you like to be Xs or Os? (Please enter 'X' or 'O')")
    response = response.lower()
    while response not in choices:
        print("Hey! That's not an X or an O. Please try again.")
        response = input("Would you like to be Xs or Os? (Please enter 'X' or 'O') ")
        response = response.lower()

    player1 = Player(response)
    player_list.append(player1)
    choices.remove(response)
    player2 = Player(choices[0])
    player_list.append(player2)

    for line in board:
        print(line)

    while player1.win != True and player2.win != True:

        player1.take_turn()
        player1.detect_winner()
        if player1.win == True:
            break
        elif len(chosen_spaces) == 9:
            break
        player2.take_turn()
        player2.detect_winner()

    if player1.win == True:
        print(f'Player {player1.token.title()} is the winner!')
    elif player2.win == True:
        print(f'Player {player2.token.title()} is the winner!')
    else:
        print("It's a draw!")


board = ["   |   |   ", " 1 | 2 | 3 ", "___|___|___",
    "   |   |   ", " 4 | 5 | 6 ", "___|___|___",
    "   |   |   ", " 7 | 8 | 9 ", "   |   |   "]

all_spaces = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
choices = ['x', 'o']
chosen_spaces = []
player_list = []
winning_combos = [('1', '2', '3'), ('4', '5', '6'),
                ('7', '8', '9'), ('1', '4', '7'),
                ('2', '5', '8'), ('3', '6', '9'),
                ('1', '5', '9'), ('3', '5', '7')]


if __name__ == "__main__":
    tictactoe()

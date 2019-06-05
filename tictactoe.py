'''This is a tic-tac-toe game. It does not have an AI to play against, so both sides must be played by players.'''

import os

class Player:
    def __init__(self, token):
        self.token = token
        self.spaces = []
        self.win = False

    def take_turn(self):
        global line2, line5, line8, line_list
        choice = input("Player %s, choose a space! " % self.token.title())
        while True:
            if choice not in all_spaces:
                choice = input("That's not a valid space! Please choose again. ")
            elif choice in chosen_spaces:
                choice = input("That space has already been chosen! Please choose again. ")
            else:
                break
        self.spaces.append(choice)
        chosen_spaces.append(choice)

        line2_split = list(line2)
        line5_split = list(line5)
        line8_split = list(line8)
        if choice in line2_split:
            index = line2_split.index(choice)
            line2_split[index] = self.token.title()
            line2 = "".join(line2_split)
            line_list[1] = line2
        elif choice in line5_split:
            index = line5_split.index(choice)
            line5_split[index] = self.token.title()
            line5 = "".join(line5_split)
            line_list[4] = line5
        else:
            index = line8_split.index(choice)
            line8_split[index] = self.token.title()
            line8 = "".join(line8_split)
            line_list[7] = line8
        _ = os.system('cls' if os.name == 'nt' else 'clear')
        for line in line_list:
            print(line)



    def detect_winner(self):
        for combo in winning_combos:
            if combo[0] in self.spaces and combo[1] in self.spaces and combo[2] in self.spaces:
                self.win = True
            else:
                continue

line1 = "   |   |   "
line2 = " 0 | 1 | 2 "
line3 = "___|___|___"
line4 = "   |   |   "
line5 = " 3 | 4 | 5 "
line6 = "___|___|___"
line7 = "   |   |   "
line8 = " 6 | 7 | 8 "
line9 = "   |   |   "

line_list = [line1, line2, line3, line4, line5, line6, line7, line8, line9]

all_spaces = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
choices = ['x', 'o']
chosen_spaces = []
player_list = []
winning_combos = [['0', '1', '2'], ['3', '4', '5'],
                ['6', '7', '8'], ['0', '3', '6'],
                ['1', '4', '7'], ['2', '5', '8'],
                ['0', '4', '8'], ['2', '4', '6']]

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

    for line in line_list:
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
        print("Player %s is the winner!" % player1.token.title())
    elif player2.win == True:
        print("Player %s is the winner!" % player2.token.title())
    else:
        print("It's a draw!")

if __name__ == "__main__":
    tictactoe()

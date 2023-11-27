import time
from itertools import cycle
from random import randint

# Define the winning combinations for Tic Tac Toe
winning_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

myIterator = cycle([2, 1])


# Initialize game board with empty spaces
def initialize_board():
    return [["   ", "   ", "   "], ["   ", "   ", "   "], ["   ", "   ", "   "]]


# Print the game board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 11)


# Update the game board with the player's move
def update_board(board, row, col, player):
    if player == 1:
        board[row][col] = " X "
    else:
        board[row][col] = " O "


# Get player's move
def get_players_move(board, player):
    while True:
        try:
            row = int(input(
                "Enter the row (1,2,3): ")) - 1  # get the row the user wants to play in and adjust to 0-based indexing
            column = int(input(
                "Enter the column (1,2,3): ")) - 1  # get the column the user wants to play in and adjust to 0-based indexing
            if 0 <= row < 3 and 0 <= column < 3 and board[row][
                column] == "   ":  # checks to make sure the row and column values entered are valid and not in a position with a value already
                update_board(board=board, row=row, col=column, player=player)
                break
            else:
                print("Invalid input. Please choose an empty position.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def check_win(board, print_result):
    for combination in winning_combinations:
        a, b, c = [i - 1 for i in
                   combination]  # creates the values a,b,c from each combination to represent the 0-based indices for winning combination
        if board[a // 3][a % 3] == board[b // 3][b % 3] == board[c // 3][c % 3] and board[a // 3][
            a % 3] != "   ":  # checks if symbols at cells a,b,c are the same and make sure they are not empty spaces
            if print_result:
                print_board(board)
                print(f"Player {1 if board[a // 3][a % 3] == ' X ' else 2} wins!")
            return True

    if all(cell != "   " for row in board for cell in
           row):  # checks if all the cells on the board are not empty with no winner meaning it is a tie
        print_board(board)
        print("It's a tie!")
        return True
    return False


def computer_move(board):
    for row in range(3):
        for column in range(3):
            if board[row][column] == "   ":
                board[row][column] = " O "
                if check_win(board,
                             print_result=False):  # this checks if it is a winning move that the computer can play and does it
                    return
                board[row][column] = "   "  # if it's not a winning move then undo it

    for row in range(3):
        for column in range(3):
            if board[row][column] == "   ":
                board[row][column] = " X "
                if check_win(board, print_result=False):  # this checks if there is a blocking move that can be played
                    board[row][column] = " O "
                    return
                board[row][column] = "   "  # if it's not a blocking move then undo it

    while True:
        row = randint(0, 2)  # if there are no winning or blocking moves then play a random move
        col = randint(0, 2)
        if board[row][col] == "   ":
            update_board(board=board, row=row, col=col, player=2)
            break


def multiplayer():
    print("\n")
    game_board = initialize_board()
    print_board(game_board)
    print("Player 1 will go first and will be X.")
    print("Player 2 will go second and will be O.\n")
    current_player = 1
    while True:
        print(f"Player {current_player}'s turn")
        get_players_move(board=game_board, player=current_player)
        if check_win(game_board, print_result=True):
            break
        else:
            print_board(game_board)
            current_player = next(myIterator)
    print("Game Over!")


def single_player():
    print('\n')
    game_board = initialize_board()
    print_board(game_board)
    print("You are Player 1 and will be X.")
    print("Computer is Player 2 and will be O.\n")
    while True:
        print("Your turn")
        get_players_move(board=game_board, player=1)
        if check_win(game_board, print_result=True):
            break
        else:
            print_board(game_board)
            time.sleep(0.5)
            print("\n")

        print("Computer's turn")
        computer_move(game_board)
        if check_win(game_board, print_result=True):
            break
        else:
            print_board(game_board)

    print("Game Over!")


def main():
    print("Welcome to Tic Tac Toe!\n")
    game_type = input("Would you like to play single player (S) or multiplayer (M): ").lower()
    if game_type == 'm':
        multiplayer()
    else:
        single_player()


main()

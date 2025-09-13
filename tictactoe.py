
import os
from colorama import Fore, Style, init

init(autoreset=True)

board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

valid_pos = [i for i in range(1, 10)]

def color(text, win=False):
    text = str(text)

    if text in "1234567890":
        return Style.DIM + Fore.WHITE + text + Style.RESET_ALL
    elif text == "X":
            return Fore.RED + text if win else Fore.RED + text + Style.RESET_ALL
    elif text == "O":
        return Fore.BLUE + text if win else Fore.BLUE + text + Style.RESET_ALL

def print_board():
    for i in range(3):
        print(f" {color(board[i][0])} | {color(board[i][1])} | {color(board[i][2])} ")
        if i != 2:
            print("---|---|---")

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def player_turn(symbol, message=""):
    while True:
        clear_screen()
        print_board()
        print(f"\n{message}")
        draw_check()
        try:
            pos = int(input(f"Enter position for {symbol}: "))
        except ValueError:
            message = "Please enter a valid number!"
            continue
        if pos in valid_pos:
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == pos:
                        board[i][j] = symbol
            valid_pos.remove(pos)
            win_check(symbol)
            break
        else:
            message = "That's not a valid position! Try again."

def draw_check():
    check = True
    for i in board:
        for j in i:
            if isinstance(j, int):
                check = False
    if check:
        clear_screen()
        print_board()
        print(f"\n\n\nIt's a draw!\n")
        play_again()

def win_check(symbol):
    if row_win_check(symbol) or col_win_check(symbol) or diag_win_check(symbol):
        clear_screen()
        print_board()
        print(f"\n\n\n{color(symbol, True)} wins!\n")
        play_again()

def row_win_check(symbol):
    for i in range(len(board)):
        if len(set(board[i])) == 1 and board[i][0] == symbol:
            return True
    return False

def col_win_check(symbol):
    for j in range(3):
        col = [board[i][j] for i in range(3)]
        if len(set(col)) == 1 and col[0] == symbol:
            return True
    return False

def diag_win_check(symbol):
    diag1 = [board[i][i] for i in range(3)]
    diag2 = [board[i][2 - i] for i in range(3)]
    if len(set(diag1)) == 1 and diag1[0] == symbol:
        return True
    if len(set(diag2)) == 1 and diag2[0] == symbol:
        return True
    return False


def play_again():
    choice = input("Do you want to play again? (y/n): ").strip().lower()
    if choice == 'y':
        reset_game()
        main()
    else:
        print("Thanks for playing!")
        exit()

def reset_game():
    global board, valid_pos
    board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    valid_pos = [i for i in range(1, 10)]

def main():
    while True:
        player_turn("X")
        player_turn("O")

if __name__ == "__main__":
    main()
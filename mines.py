import argparse
import random

board_height = 0
board_width = 0
mines = 0
board = []


def _argsHandler():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mode",type=str,  default="Easy", metavar="", help="Chose mode: Easy, Intermediate, Expert or Custom")
    args = parser.parse_args()
    setBoard(args.mode)
    run()

def setBoard(mode):
    print("You chose", mode, "!")
    global board_height 
    global board_width
    global mines
    match mode:
        case "Easy":
            board_height = 9
            board_width = 9
            mines = 10
        case "Intermediate":
            board_height = 16
            board_width = 16
            mines = 40
        case "Expert":
            board_height = 16
            board_width = 30
            mines = 99
        case "Custom":
            board_height = int(input("Choose height: "))
            board_width = int(input("Choose width: "))
            mines = int(input("Choose number of mines: "))
        case _:
            print("Something went wrong! Exiting")
            exit()

def generate_board():
    global board
    board = [[" " for _ in range(board_width)] for _ in range(board_height)]
    for _ in range(mines):
        mh = random.randrange(board_height)
        mw = random.randrange(board_width)
        board[mh][mw] = "X"

def print_board():
    print("Printing board")
    for line in board:
        print(line)



def run():
    generate_board()
    print_board()
    print(board_height, board_width)

if __name__ == "__main__":
    _argsHandler()
    

#!/usr/bin/env python

import argparse
from ast import BitOr
import random

board_height = 0
board_width = 0
mines = 0
board = []
test = False
play_board = []
won = False


def _argsHandler():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mode",type=str,  default="Easy", metavar="", help="Chose mode: Easy, Intermediate, Expert or Custom")
    parser.add_argument("-t", "--test", action='store_true', help="Set in test mode")
    args = parser.parse_args()
    global test
    test = args.test
    setBoard(args.mode)
    run()

def setBoard(mode):
    print("You chose", mode, "!")
    print()
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

def generate_mines():
    global board
    global test
    global mines
    global play_board
    board = [[0 for _ in range(board_width)] for _ in range(board_height)]
    play_board = [[" " for _ in range(board_width)] for _ in range(board_height)]
    added_mines = 0
    while added_mines < mines:
        mh = random.randrange(board_height)
        mw = random.randrange(board_width)
        if board[mh][mw] == "X":
            continue
        board[mh][mw] = "X"
        added_mines += 1
        for i in range(-1,2):
            for j in range(-1,2):
                if i == 0 and j == 0:
                    continue
                increment_square(mh-i,mw-j)
        if test:
            print("Mine added at ", mh, "x", mw)
            print_test_board()

def increment_square(h, w):
    if h < 0 or w < 0 or h >= board_height or w >= board_width:
        return
    elif board[h][w] == "X":
        return
    else:
        board[h][w] += 1

def generate_board():
    generate_mines()

def print_test_board():
    print("Printing board")
    for line in board:
        print("|",end="")
        for l in line:
            if l == 0:
                print(" ", end="|")
            else:
                print(str(l), end="|")
        print("")

def print_play_board():
    global won
    won = True
    print("Printing board")
    x = 0
    print("__|0_|1_|2_|3_|4_|5_|6_|7_|8_|")
    for line in play_board:
        print("|"+str(x),end="|")
        for l in line:
            if l == " ":
                won = False
            print("["+l, end="]")
        print("")
        x += 1

def flag(x,y):
    global play_board
    play_board[y][x] = 'F'
    print_play_board()

def next_move():
    move = input("What is your next move? Ex. (1x2): ")
    if move[0] == 'f':
        x = int(move[1:].split("x")[0])
        y = int(move[1:].split("x")[1])
        flag(x,y)
        return
    x = int(move.split("x")[0])
    y = int(move.split("x")[1])
    print("x:",x,"y:",y)
    if x < 0 or y < 0 or x >= board_width or y >= board_height:
        print("Illeagal move, try again!")
        next_move()
        return
    next_play_board(x,y)

def next_play_board(x,y):
    global board
    global play_board
    if x < 0 or y < 0 or x >= board_width or y >= board_height or play_board[y][x] != " ":
        return
    play_board[y][x] = str(board[y][x])
    print_play_board()
    if board[y][x] == "X":
        print("Game over! Better luck next time!")
        exit()
    elif board[y][x] == 0:
        for i in range(-1,2):
            for j in range(-1,2):
                if i == 0 and j == 0:
                    continue
                print("trying x+j",x+j,"and y+i",y+i, "with j",j,"i",i)
                next_play_board(x+j,y+i)
    else:
        return

    
def run():
    global won
    global test
    generate_board()
    print_play_board()
    while True:
        next_move()
        if test:
            print_test_board()
        if won == True:
            break
    print("Congratulations you have won!")

if __name__ == "__main__":
    _argsHandler()
    

# Four-In-A-Row (a Connect Four clone)
# http://inventwithpython.com/blog
# By Al Sweigart al@inventwithpython.com
# Modified by Chris Farris

import random
import copy
import sys
from A3 import *


def main():
    print('Four-In-A-Row')
    
    #-----------#
    # MAIN LOOP #
    #-----------#
    while True:
        #Decide which player uses which tile and who goes first
        humanTile, computerTile = enterHumanTile()
        turn = whoGoesFirst()
        print('The %s player will go first.' % (turn))
        mainBoard = getNewBoard()

        #-----------#
        # GAME LOOP #
        #-----------#
        while True:
            #------------#
            # HUMAN TURN #
            #------------#
            if turn == 'human':
                drawBoard(mainBoard)
                move = getHumanMove(mainBoard)
                makeMove(mainBoard, humanTile, move)
                if isWinner(mainBoard, humanTile):
                    winner = 'human'
                    break
                turn = 'computer'
            #---------------#
            # COMPUTER TURN #
            #---------------#
            else:
                drawBoard(mainBoard)
                print('The computer is thinking...')
                move = getComputerMove(mainBoard, computerTile)
                if move is None:
                    print 'Move is none-Type. getComputerMove should return a column index'
                    return 
        
                    
                makeMove(mainBoard, computerTile, move)
                if isWinner(mainBoard, computerTile):
                    winner = 'computer'
                    break
                turn = 'human'

            if isBoardFull(mainBoard):
                winner = 'tie'
                break

        drawBoard(mainBoard)
        print('Winner is: %s' % winner)
        if not playAgain():
            break


def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return raw_input().lower().startswith('y')


def enterHumanTile():
    # Let's the human player type which tile they want to be.
    # Returns a list with the human player's tile as the first item, and the computer's tile as the second.
    tile = ''
    while not (tile == 'X' or tile == 'O'):
        print('Do you want to be X or O?')
        tile = raw_input().upper()

    # the first element in the tuple is the human player's tile, the second is the computer's tile.
    if tile == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'human'


def getHumanMove(board):
    #Prompts the Human player for their move
    while True:
        print('Which column do you want to move on? (1-%s, or "quit" to quit game)' % (BOARDWIDTH))
        move = raw_input()
        if move.lower().startswith('q'):
            sys.exit()
        if not move.isdigit():
            continue
        move = int(move) - 1
        if isValidMove(board, move):
            return move


if __name__ == '__main__':
    main()

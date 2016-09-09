#INFO-I399 Assignment 4
#Younghwan Cha
#Sol Won



#------------------------------------------------------------#
#                 YOUR CODE BELOW                            #
#                                                            #
#                 ONLY MODIFY THIS FILE                      #
#------------------------------------------------------------#

'''
The board is represented as list of list. Something like this for a 5X5 board

row\cols 0 1 2 3 4
0
1
2
3

You can access the element of the board using, board[rowIndex][columnIndex].

Values on the board would be one of the following -

'-' => Indicating empty tile, Chaos can move some piece to this position or order can place the piece it picked randomly
		at this position

'A' => Indicating Red colored tile placed
'B' => Indicating Cyan colored tile placed
'C' => Indicating Green colored tile placed
'D' => Indicating Blue colored tile placed
'E' => Indicating Yellow colored tile placed

Mapping ==> 'A': 'Red', 'B': 'Cyan', 'C': 'Green','D':'Blue', 'E':'Yellow', '-':'-'}
Example -

board[0][0] will give the Piece on the top-left position.

board[1][3] will give the piece in 1st row and 3rd column

board[N - 1][N - 1] will give the piece on the bottom-right position



Read this entire file and understand the comments for the functions and variables

'''

# myAI.py
import sys
from random import random, choice

def printX(*message):
	for msg in message:
		sys.stderr.write(repr(msg) + ' ') 
	sys.stderr.write('\n') 

# boardSize, squared board with N = 5, 7..
N = int(raw_input())

# Current role - ORDER or CHAOS
ROLE = raw_input()

# initializing board with empty tile '-'
board = []
for i in range(0, N):
	boardRow = []
	for j in range(0, N):
		boardRow.append('-')
	board.append(boardRow)

# check if no empty tile left
def isGameOver():
	for i in range(0, N):
		for j in range(0, N):
			if (board[i][j] == '-'):
				return False
	return True



# gets all the possible moves order can make
# this can be used for getting the children from a given state
def getPossibleOrderMoves(x, y):
	possibleMoves = []

	for iterator in range(x-1,-1,-1):
		if board[iterator][y]=='-':
			possibleMoves.append((iterator,y))
		else:
			break

	for iterator in range(y-1,-1,-1):
		if board[x][iterator]=='-':
			possibleMoves.append((x,iterator))
		else:
			break

	for iterator in range(x+1,N):
		if board[iterator][y]=='-':
			possibleMoves.append((iterator,y))
		else:
			break

	for iterator in range(y+1,N):
		if board[x][iterator]=='-':
			possibleMoves.append((x,iterator))
		else:
			break

	return possibleMoves

#------------------------------------------------------------#
#                 MAIN FUNCTION              				 #
#                 FOR CHAOS BOT                      		 #
#------------------------------------------------------------#

# @input: piece, the key to the color picked,
# Example
# piece = 'A', Red tile is randomly drawn from the bag
# piece = 'E', Yellow tile is randome drawn from the bag
#
# @return: tuple of an EMPTY co-ordinate/x,y - position on the board, where you want to place the tile on the board
# Example
# If @input as a piece is 'D'
# @return (2,3)
# Place the Green colored tile ('D' corresponds to Green) in 3rd row and 4th column [Index starting from ZERO!, NOTE]

# currently it naively picks an empty position to place the tile on the board
# make it intelligent!
def chaosAI(piece):
	openSquares=[]
	for x in xrange(N):
		for y in xrange(N):
			if board[x][y]=="-":
				openSquares.append((x,y))
	openSquares
	return choice(openSquares)


#------------------------------------------------------------#
#                 MAIN FUNCTION              				 #
#                 FOR ORDER BOT                      		 #
#------------------------------------------------------------#

# @return: a tuple with 4 values a b c d
# ORDER wants to shift a tile from a non-empty co-ordinate/x-y position, (a, b) to an EMPTY position (c, d)
# CONSTRAINT - the shift can only be done to an EMPTY position in SAME ROW or SAME COLUMN as the current tile position

# currently it naively picks a random tile and tried to move it randomly in the same row or column as the tile
# to place the tile on the board
# make this intelligent too!

def orderAI():
	capturedSquares=[]
	for x in xrange(N):
		for y in xrange(N):
			if board[x][y]!="-":
				capturedSquares.append((x,y,board[x][y]))

	capturedSquares = sorted(capturedSquares, key=lambda t:(t[0],t[1]))

	while(True):
		fromPosition = choice(capturedSquares)
		possibleMoves = getPossibleOrderMoves(fromPosition[0], fromPosition[1])
		if len(possibleMoves)!=0:
			mv = choice(possibleMoves)
			ans = (fromPosition[0], fromPosition[1], mv[0], mv[1])
			break

	return ans

#------------------------------------------------------------#
#                 HELPER FUNCTIONS               		     #
#                   & ADD MORE FUNCTION 					 #
# 						AND									 #
# 						  MODIFY AS YOU FEEL                 #
#------------------------------------------------------------#

# Here are the following list of things that you'll need -
# 1. Finding the scores of the board in terms of palindromes of the board
# 2. Book keeping of the number of tiles of each color on the board, to be used for calculating the probability
# of next tile randomly
# 3. Generating children board for a move to be made by CHAOS & ORDER
# 4. Perform expectiMiniMax with Alph Beta pruning
# 5. Implement a heuristic
# 6. Prove your mettle and win the battle!

#assigning colors 5red, 5blue, 5yellow, 5green, 5cyan
#colors hardcoded since we have to get the random colors
colors = ["r","c","g","b","y",
          "r","c","g","b","y",
          "r","c","g","b","y",
          "r","c","g","b","y",
          "r","c","g","b","y"]

#get score
def getScore(board):
    #set initial score to 0
    score = 0
    #make empty list
    lists = []
    #another list since there should be duplicated values to be included
    listss = []
    #doing the cols and rows of the board
    for i in range(len(board)):
        for j in range(len(board[i])):
            lists.append(board[j][i])
        listss.append(lists)
        lists = []
    for item in board:
        for i in sublist(item):
            #pass since we dont want to count
            if '-' in i:
                pass
            elif palindrome(i) == True:
                score += len(i)
    for item in listss:
         for i in sublist(item):
            #pass since we dont want to count
            if '-' in i:
                pass
            elif palindrome(i) == True:
                score += len(i)
    return score

#check whether i and i-1 has a same value which is palindrome
def palindrome(board):
    tf = False
    for i in range(len(board)):
        if board[i] == board[-i-1]:
            #returning true
            tf = True
        else:
            #returning false
            tf = False
            break
    return tf

#another function since there are lists of lists of lists
def sublist(board):
    #making sublist
    sub = []
    for i in range(len(board)):
        for j in range(i+2, len(board)+1):
            sub.append(board[i:j])
    return sub

#generate children
def generateChildren(board, computerTile):
    #Order Children
    if (computerTile == 'ORDER'):
        color = ""
        #open new text file to store data
        f = open('file.txt','w')
        #len of board
        for i in range(len(board)):
                for j in range(len(board)):
                    if board[i][j] != "-":
                        color = board[i][j]
                        position = getPossibleOrderMoves(i, j)
                        board[i][j] = "-"
                        for item in range(len(position)):
                            #print the board containing those board
                            board[position[item][0]][position[item][1]] = color
                            f.write(str(board))
                            #reset the board
                            board[position[item][0]][position[item][1]] = "-"
                        board[i][j] = color
                #bring data from the text file that we made
                f = open('file.txt','r')
                contents = f.readlines()
                return contents
                #We tried importing and exporting data from and to text file because appending the list of all possible move of the tile did not work for some reason.
                #This method of creating text file and bring the data back to the python does not work either. We choose to upload this codes in order to show the effort to try new way.

    #Chaos Children
    chaos_positions = []
    if (computerTile == 'CHAOS'):        
        for i in range(len(board)):
                for j in range(len(board)):
                    color = random.choice(colors)
                    colors.remove(color)
                    if board[i][j] == "-":
                        chaos_positions.append((i,j))
        for item in range(len(chaos_positions)):
            board[chaos_positions[item][0]][chaos_positions[item][1]] = color
            print board
            board[chaos_positions[item][0]][chaos_positions[item][1]] = "-"
        board[i][j] = color
        
def expectiMiniMax(board, deth, computerTile):
    if (computerTile == 'CHAOS'):
        #list to put all the values and compare
        minmax = []
        #set the count to zero
        count=0
        for i in range(len(board)):
            for j in range(len(board)):
                color = random.choice(colors)
                colors.remove(color)
                #probability when r is picked
                if color == "r":
                    prob_r = float(colors.count("r"))/(25-int(count))
                    red = prob_r*(Heuristic(board)+getScore(board))
                    minmax.append(red)
                    count += 1
                #probability when c is picked
                elif color == "c":
                    prob_c = float(colors.count("r"))/(25-int(count))
                    cyan = prob_c*(Heuristic(board)+getScore(board))
                    minmax.append(cyan)
                    count += 1

                #probability when g is picked
                elif color == "g":
                    prob_g = float(colors.count("r"))/(25-int(count))
                    green = prob_g*(Heuristic(board)+getScore(board))
                    minmax.append(green)
                    count += 1

                #probability when b is picked
                elif color == "b":
                    prob_b = float(colors.count("r"))/(25-int(count))
                    blue = prob_b*(Heuristic(board)+getScore(board))
                    minmax.append(blue)
                    count += 1

                #probability when y is picked
                elif color == "y":
                    prob_y = float(colors.count("r"))/(25-int(count))
                    yellow = prob_y*(Heuristic(board)+getScore(board))
                    minmax.append(yellow)
                    count += 1
        return min(minmax)

    #same thing for the order process, but the only difference is returning max value of the minmax list
    elif (computerTile == 'ORDER'):
        minmax = []
        count=0
        for i in range(len(board)):
            for j in range(len(board)):
                color = random.choice(colors)
                colors.remove(color)
                if color == "r":
                    prob_r = float(colors.count("r"))/(25-int(count))
                    red = prob_r*(Heuristic(board)+getScore(board))
                    minmax.append(red)
                    count += 1

                elif color == "c":
                    prob_c = float(colors.count("r"))/(25-int(count))
                    cyan = prob_c*(Heuristic(board)+getScore(board))
                    minmax.append(cyan)
                    count += 1
 
                elif color == "g":
                    prob_g = float(colors.count("r"))/(25-int(count))
                    green = prob_g*(Heuristic(board)+getScore(board))
                    minmax.append(green)
                    count += 1

                elif color == "b":
                    prob_b = float(colors.count("r"))/(25-int(count))
                    blue = prob_b*(Heuristic(board)+getScore(board))
                    minmax.append(blue)
                    count += 1

                elif color == "y":
                    prob_y = float(colors.count("r"))/(25-int(count))
                    yellow = prob_y*(Heuristic(board)+getScore(board))
                    minmax.append(yellow)
                    count += 1
        return max(minmax)
    # This recursive function will take the initial board state, a depth to go to and alpha and beta value
    # and return back the value

def Heuristic(board):
    #for heuristic, we used scores. we modified the scores and added when "-" is there.
    #for example, a - a - a and a - - - a has different value if we count -. also depend on how many dashes is between, the values will be different.
    #we decided to use that as our heuristic.
    score = 0
    lists = []
    listss = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            lists.append(board[j][i])
        listss.append(lists)
        lists = []
    for item in board:
        for i in sublist(item):
            if '-' in i:
                score += 1
            elif palindrome(i) == True:
                score += len(i)
            else:
                score += 1
    for item in listss:
         for i in sublist(item):
            if '-' in i:
                score += 1
            elif palindrome(i) == True:
                score += len(i)
            else:
                score += 1
    return score

    #Given a board, returns the value of that board when evaluated with a heuristic, evaluation function



#------------------------------------------------------------#
#                 DO NOT CHANGE THE               		     #
#                    CODE BELOW                    		     #
#------------------------------------------------------------#

## --------------------
import os, sys
sys.path.insert(0, os.path.realpath('../utils'))
from log import *

COLORS = [
	bcolors.OKRED, 
	bcolors.OKCYAN, 
	bcolors.OKGREEN, 
	bcolors.OKBLUE, 
	bcolors.OKYELLOW, 
	bcolors.OKMAGENTA, 
	bcolors.OKCYAN, 
	bcolors.OKWHITE
]

# MAPPING of Piece with Colors

TEXTCONV = {'A': 'R', 'B': 'C', 'C': 'G','D':'B', 'E':'Y', '-':'-'}
def color(tile): # character
	index = ord(tile) - ord('A')
	if (tile == '-'):
		index = -1

	if (N <= 5):
		# Not over riding 5x5's old behaviour
		return COLORS[index] + TEXTCONV[tile] + bcolors.ENDC
	else:
		return COLORS[min(index, len(COLORS)-1)] + tile + bcolors.ENDC

def printBoard():
	for x in xrange(N):
		print >>sys.stderr,  "".join( list( map( lambda x: color(x), board[x] ) ) )
	print >>sys.stderr, '\n'

# returns if the move was successful or not
def makeChaosMove(x, y, color):
	global board
	if (board[x][y] != '-'):
		return False
	board[x][y] = color 
	return True
	
# returns if the move was successful or not
def makeOrderMove(a, b, c, d):
	global board	
	board[c][d] = board[a][b]
	board[a][b] = '-'
	return True

def playAsOrder():
	global board
	printX('ORDER')
	while True:
		printBoard()
		line = raw_input()
		# printX ('LINE:', line)
		(x, y, color) = line.split(' ')
		(x, y) = (int(x), int(y))
		board[x][y] = color
		if (isGameOver()):
			return
	
		(a, b, c, d) = orderAI()
		makeOrderMove(a, b , c, d)
		printBoard()
		print '%d %d %d %d' % (a, b, c, d)
		sys.stdout.flush()

	
def playAsChaos():
	global board
	printX('CHAOS')
	color = raw_input()
	(x, y) = chaosAI(color)
	board[x][y] = color
	print '%d %d' %(x, y)
	printBoard()

	while True:
		if (isGameOver()):
			return

		his_move = raw_input()
		# printX ('his move: %s'%his_move)
		(a, b, c, d) = map(lambda x: int(x), his_move.split(' '))
		makeOrderMove(a, b, c, d)
		color = raw_input()
		(x, y) = chaosAI(color)
		board[x][y] = color
		printBoard()
		print '%d %d' %(x, y)
			

if (ROLE == 'ORDER'):
	playAsOrder()
elif(ROLE == 'CHAOS'):
	playAsChaos()
else:
	print >> sys.stderr, 'I am not intelligent for this role: %s' %ROLE
	
printX ('--graceful exit by myAI--')

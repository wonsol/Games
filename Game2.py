#------------------------------------------------------------#
#                 YOUR CODE BELOW                            #
#------------------------------------------------------------#
'''
The board is represented by a list of lists.
Board[0][0] is the upper left corner of the connect four board.
Board[BOARDWIDTH-1][BOARDHEIGHT-1] is the lower right corner
'''

#Standard connect four is a 7x6 board
BOARDWIDTH = 7
BOARDHEIGHT = 6
import random
import copy

def getComputerMove(board, computerTile):
    #Given a board represented as a list of lists and the computer's tile symbol,
    #returns the column that the computer should play their tile in
    ret = AlphaBeta(board, 1, computerTile)
    return ret

def GenerateChildren(board, computerTile):
    #This function takes a board state and a tile symbol and returns a
    #list of "children" states, i.e., a list of boards which represent possible moves.
    #This function will be helpful to use in your Alpha Beta function
    totalboards = []
    for i in range(BOARDWIDTH):
        totalboards.append(copy.deepcopy(board))
    for i in range(BOARDWIDTH):
        space = True
        for j in range (BOARDHEIGHT):
            if totalboards[i][i][BOARDHEIGHT-1-j] == " " and space != False:
                totalboards[i][i][BOARDHEIGHT-1-j] = computerTile
                space = False
    return totalboards


def AlphaBeta(board, depth, computerTile):
    #Alpha Beta takes an initial board state, a depth to go to, and a the computer's tile symbol.
    #Alpha Beta then performs the alpha-beta search algorithm with pruning to return the best mov
    return AB(board, depth, float("-inf"), float("inf"), True, computerTile)

def AB(board, depth, alpha, beta, maxi, computerTile):
    boards = GenerateChildren(board, computerTile)
    if depth == 0 or isWinner(board, computerTile) == True or isBoardFull(board) == True:
        if computerTile == "X":
            return Heuristic(board, computerTile)
        else:
            return Heuristic(board, computerTile)

    for board in boards:
        value = AB(board, depth-1, alpha, beta, maxi, computerTile)
        if maxi:
            alpha = max(alpha, value)
            if alpha >= beta:
                return alpha
        else:
            beta = min(beta, value)
            if alpha >= beta:
                return beta
    if maxi:
        return alpha
    else:
        return beta


def Heuristic(board, computerTile):
##    sums = 0
##    sums = random.randrange(7)
##    return sums
    
    #Given a board, returns the value of that board when evaluated with a heuristic
    empty_final = []
    empty = []
    comp_count_four = 0
    comp_count_three = 0
    comp_count_two = 0

    human_count_four = 0
    human_count_three = 0
    human_count_two = 0    
    tile = " "
    if computerTile == "O":
        tile = "O"
        for y in range(BOARDHEIGHT):
            for x in range(BOARDWIDTH - 3):
                if board[x][y] == tile and board[x+1][y] == tile and board[x+2][y] == tile and board[x+3][y] == tile:
                    comp_count_four += 1
        for y in range(BOARDHEIGHT):
            for x in range(BOARDWIDTH - 4):
                if board[x][y] == tile and board[x+1][y] == tile and board[x+2][y] == tile:
                    comp_count_three += 1
        for y in range(BOARDHEIGHT):
            for x in range(BOARDWIDTH - 5):
                if board[x][y] == tile and board[x+1][y] == tile:
                    comp_count_two += 1

        for x in range(BOARDWIDTH):
            for y in range(BOARDHEIGHT - 3):
                if board[x][y] == tile and board[x][y+1] == tile and board[x][y+2] == tile and board[x][y+3] == tile:
                    comp_count_four += 1
        for x in range(BOARDWIDTH):
            for y in range(BOARDHEIGHT - 4):
                if board[x][y] == tile and board[x][y+1] == tile and board[x][y+2] == tile:
                    comp_count_three += 1
        for x in range(BOARDWIDTH):
            for y in range(BOARDHEIGHT - 5):
                if board[x][y] == tile and board[x][y+1] == tile:
                    comp_count_two += 1

        for x in range(BOARDWIDTH - 3):
            for y in range(3, BOARDHEIGHT):
                if board[x][y] == tile and board[x+1][y-1] == tile and board[x+2][y-2] == tile and board[x+3][y-3] == tile:
                    comp_count_four += 1
        for x in range(BOARDWIDTH - 4):
            for y in range(4, BOARDHEIGHT):
                if board[x][y] == tile and board[x+1][y-1] == tile and board[x+2][y-2] == tile:
                    comp_count_three += 1
        for x in range(BOARDWIDTH - 5):
            for y in range(5, BOARDHEIGHT):
                if board[x][y] == tile and board[x+1][y-1] == tile:
                    comp_count_two += 1

        for x in range(BOARDWIDTH - 3):
            for y in range(BOARDHEIGHT - 3):
                if board[x][y] == tile and board[x+1][y+1] == tile and board[x+2][y+2] == tile and board[x+3][y+3] == tile:
                    comp_count_four += 1
        for x in range(BOARDWIDTH - 4):
            for y in range(BOARDHEIGHT - 4):
                if board[x][y] == tile and board[x+1][y+1] == tile and board[x+2][y+2] == tile:
                    comp_count_three += 1
        for x in range(BOARDWIDTH - 5):
            for y in range(BOARDHEIGHT - 5):
                if board[x][y] == tile and board[x+1][y+1] == tile:
                    comp_count_two += 1

    if computerTile == "X":
        tile = "X"
        for y in range(BOARDHEIGHT):
            for x in range(BOARDWIDTH - 3):
                if board[x][y] == tile and board[x+1][y] == tile and board[x+2][y] == tile and board[x+3][y] == tile:
                    human_count_four += 1
        for y in range(BOARDHEIGHT):
            for x in range(BOARDWIDTH - 3):
                if board[x][y] == tile and board[x+1][y] == tile and board[x+2][y] == tile:
                    human_count_three += 1
        for y in range(BOARDHEIGHT):
            for x in range(BOARDWIDTH - 3):
                if board[x][y] == tile and board[x+1][y] == tile:
                    human_count_two += 1

        for x in range(BOARDWIDTH):
            for y in range(BOARDHEIGHT - 3):
                if board[x][y] == tile and board[x][y+1] == tile and board[x][y+2] == tile and board[x][y+3] == tile:
                    human_count_four += 1
        for x in range(BOARDWIDTH):
            for y in range(BOARDHEIGHT - 3):
                if board[x][y] == tile and board[x][y+1] == tile and board[x][y+2] == tile:
                    human_count_three += 1
        for x in range(BOARDWIDTH):
            for y in range(BOARDHEIGHT - 3):
                if board[x][y] == tile and board[x][y+1] == tile:
                    human_count_two += 1

        for x in range(BOARDWIDTH - 3):
            for y in range(3, BOARDHEIGHT):
                if board[x][y] == tile and board[x+1][y-1] == tile and board[x+2][y-2] == tile and board[x+3][y-3] == tile:
                    human_count_four += 1
        for x in range(BOARDWIDTH - 3):
            for y in range(3, BOARDHEIGHT):
                if board[x][y] == tile and board[x+1][y-1] == tile and board[x+2][y-2] == tile:
                    human_count_three += 1
        for x in range(BOARDWIDTH - 3):
            for y in range(3, BOARDHEIGHT):
                if board[x][y] == tile and board[x+1][y-1] == tile:
                    human_count_two += 1

        for x in range(BOARDWIDTH - 3):
            for y in range(BOARDHEIGHT - 3):
                if board[x][y] == tile and board[x+1][y+1] == tile and board[x+2][y+2] == tile and board[x+3][y+3] == tile:
                    human_count_four += 1
        for x in range(BOARDWIDTH - 3):
            for y in range(BOARDHEIGHT - 3):
                if board[x][y] == tile and board[x+1][y+1] == tile and board[x+2][y+2] == tile:
                    human_count_three += 1
        for x in range(BOARDWIDTH - 3):
            for y in range(BOARDHEIGHT - 3):
                if board[x][y] == tile and board[x+1][y+1] == tile:
                    human_count_two += 1

    number = (comp_count_four*1000 + comp_count_three*100 + comp_count_two*10) - (human_count_four*1000 + human_count_three*100 + human_count_two*10)
    empty.append(abs(number))
    for i in range(len(empty)):
        empty_final.append(i)
        if max(empty_final) == empty_final[i]:
            return i            




#---------------------------------------------------------------#
#                      END STUDENT CODE                         #
#---------------------------------------------------------------#


#----------------------------#
#       HELPER FUNCTIONS     #
#         DO NOT TOUCH       #
#----------------------------#
'''
These functions are used in the game logic and may be useful for you
to use in your own code. DO NOT MODIFY these functions or else
the game may not work properly
'''

def drawBoard(board):
    #Prints out the board for visual play
    print ""
    print "+"+"---+"*BOARDWIDTH
    for i in range(BOARDHEIGHT):
        print "|"+"   |"*BOARDWIDTH
        row="|"
        for j in range(BOARDWIDTH):
            row += " " + board[j][i] + " |"
        print row
        print "|"+"   |"*BOARDWIDTH
        print "+"+"---+"*BOARDWIDTH
    
    
def getNewBoard():
    #Creates a fresh board
    board = []
    for x in range(BOARDWIDTH):
        board.append([' '] * BOARDHEIGHT)
    return board

def makeMove(board, player, column):
    #Modifies the board when given a legal move
    #"player" is a symbol identifying a specific player
    for y in range(BOARDHEIGHT-1, -1, -1):
        if board[column][y] == ' ':
            board[column][y] = player
            return


def isValidMove(board, move):
    #checks  the legality of a move
    if move < 0 or move >= (BOARDWIDTH):
        return False

    if board[move][0] != ' ':
        return False

    return True


def isBoardFull(board):
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            if board[x][y] == ' ':
                return False
    return True


def isWinner(board, tile):
    # check horizontal spaces
    for y in range(BOARDHEIGHT):
        for x in range(BOARDWIDTH - 3):
            if board[x][y] == tile and board[x+1][y] == tile and board[x+2][y] == tile and board[x+3][y] == tile:
                return True

    # check vertical spaces
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT - 3):
            if board[x][y] == tile and board[x][y+1] == tile and board[x][y+2] == tile and board[x][y+3] == tile:
                return True

    # check / diagonal spaces
    for x in range(BOARDWIDTH - 3):
        for y in range(3, BOARDHEIGHT):
            if board[x][y] == tile and board[x+1][y-1] == tile and board[x+2][y-2] == tile and board[x+3][y-3] == tile:
                return True

    # check \ diagonal spaces
    for x in range(BOARDWIDTH - 3):
        for y in range(BOARDHEIGHT - 3):
            if board[x][y] == tile and board[x+1][y+1] == tile and board[x+2][y+2] == tile and board[x+3][y+3] == tile:
                return True

    return False

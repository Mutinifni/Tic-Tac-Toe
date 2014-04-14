import random

#variables to decide how the AI should change strategies according to player move  
global firstTurn, secondTurn, nofturns

def gameBoard(board): 
    print("\n %s| %s| %s" % (board[7],board[8],board[9]))
    print("__|__|__")
    print(" %s| %s| %s" % (board[4],board[5],board[6]))
    print("__|__|__")
    print(" %s| %s| %s\n" % (board[1],board[2],board[3]))

def first(): #for choosing who will go first
    if random.randint(0, 1) == 0:
        return 0
    else:
        return 1
    
def makeMove(board, letter, move):
    board[move] = letter

def checkWin(board, letter): #check winning conditions
    return ((board[1] == letter and board[2] == letter and board[3] == letter) or 
    (board[4] == letter and board[5] == letter and board[6] == letter) or 
    (board[7] == letter and board[8] == letter and board[9] == letter) or 
    (board[1] == letter and board[4] == letter and board[7] == letter) or 
    (board[2] == letter and board[5] == letter and board[8] == letter) or 
    (board[3] == letter and board[6] == letter and board[9] == letter) or 
    (board[7] == letter and board[5] == letter and board[3] == letter) or 
    (board[9] == letter and board[5] == letter and board[1] == letter)) 

def getBoard(board): #returns a board to test winning conditions in
    board1 = []
    for x in board:
        board1.append(x)
    return board1

def isFree(board, move): #check whether space is free
    return board[move] == ' '

def randomMove(board, movesList): #random move which arises due to symmetry of tic tac toe board
    moves = []
    for x in movesList:
        if isFree(board, x):
            moves.append(x)

    if len(moves) != 0:
        return random.choice(moves)
    else:
        return None

def getPlayerMove(board): #input from player
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isFree(board, int(move)):
        print('What is your move? : ')
        move = input()
    return int(move)

def getComputerMove(board, cletter): #the AI part!
    cletter == 'O'
    pletter = 'X'
    global firstTurn, secondTurn, initurn, nofturns
    moved = list()
    possible = list()
    # priority order - 1)see if computer can win 2)see if player can win next turn 3) player first turn condition 4) corners > center > edges
    for i in [1,2,3,4,5,6,7,8,9]:
        if not(isFree(board,i)):
            moved.append(i)
            continue
        possible.append(i)
        continue
    if len(possible) == 1:
        return possible[0]

    for x in range(1, 10):
        copy = getBoard(board)
        if isFree(copy, x):
            makeMove(copy, cletter, x)
            if checkWin(copy, cletter):
                return x
    
    for y in range(1, 10):
        copy = getBoard(board)
        if isFree(copy, y):
            makeMove(copy, pletter, y)
            if checkWin(copy, pletter):
                return y
    
    cornerMove = not(isFree(board,1) and isFree(board,3) and isFree(board,7) and isFree(board,9))
    edgeMove = not(isFree(board,2) and isFree(board,4) and isFree(board,8) and isFree(board,6))
    cornerMove2 = (not(isFree(board,1) or isFree(board,9))) or (not(isFree(board,3) or isFree(board,7)))
    if firstTurn == 3 and initurn == 1 and nofturns <= 5:
        for i in [1,3,7,9]:
           for j in [2,4,6,8]:
                if not(isFree(board,i)):
                    if not(isFree(board,j)):
                        if j == 2:
                            return randomMove(board, [1,3])
                        if j == 4:
                            return randomMove(board, [1,7])
                        if j == 6:
                            return randomMove(board, [3,9])
                        if j == 8:
                            return randomMove(board, [7,9])
        for i in [2,8]:
            for j in [4,6]:
                if not(isFree(board,i)):
                    if not(isFree(board,j)):
                        if j == 4:
                            return randomMove(board, [1,7])
                        if j == 6:
                            return randomMove(board, [3,9])
    if firstTurn==0 and cornerMove:
        firstTurn=3
        secondTurn=1
        return 5
    if firstTurn==0 and edgeMove:
        firstTurn=3
        return 5
    firstTurn=3   #Single line change.
    if secondTurn==1 and cornerMove2:
        secondTurn=2
        return randomMove(board, [2,4,8,6])
    move = randomMove(board, [1, 3, 7, 9])
    if move != None:
        return move
    if isFree(board, 5):
        return 5
    return randomMove(board, [2, 4, 8, 6])

def isFull(board): #checks whether board is filled at end of the game
    for x in range(1, 10):
        if isFree(board, x):
            return False
    return True

print("\nTIC TAC TOE!")
print("Instructions : You are X, computer is O. Please follow numeric keypad layout to select your move.")

while True:
    firstTurn = 0
    secondTurn = 0
    nofturns = 0
    board = [' '] * 10
    pletter = 'X'
    cletter = 'O'
    initurn = first()
    game = True
    turn = initurn
    while game: #and it begins!
        nofturns = nofturns + 1
        if turn == 1:
            #player's turn
            gameBoard(board)
            move = getPlayerMove(board)
            makeMove(board, pletter, move)

            if checkWin(board, pletter):
                gameBoard(board)
                print("Congratulations! You win!\n\n New game")
                game = False
                firstTurn=0
            else:
                if isFull(board):
                    gameBoard(board)
                    print("It's a draw!\n\n New game")
                    break
                else:
                    turn = 0

        else:
            #computer's turn
            move = getComputerMove(board, cletter)
            makeMove(board, cletter, move)

            if checkWin(board, cletter):
                gameBoard(board)
                print("The computer wins!\n\n New game")
                game = False
                firstTurn = 0
            else:
                if isFull(board):
                    gameBoard(board)
                    print("It's a draw!\n\n New game")
                    break
                else:
                    turn = 1

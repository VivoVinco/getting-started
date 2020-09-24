# tic tac toe

import random, copy

def drawBoard(board):
    # print out the board that it was passed
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def inputPlayerLetter():
    # player type which letter they want to be
    # returns a list with the player's letter as the first item, and the computer's letter as the second

    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

        if letter == 'X':
            return['X','O']
        else:
            return['O','X']

def whoGoesFirst():
    # Randomly choose which player goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    # returns true if the player wants to play again, otherwise false
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(board, letter):
    # given a board and a player's letter, function return true if player has won
    return ((board['top-L']==letter and board['top-M']==letter and board['top-R']==letter) or # across the top
            (board['mid-L']==letter and board['mid-M']==letter and board['mid-R']==letter) or # across the middle
            (board['low-L']==letter and board['low-M']==letter and board['low-R']==letter) or # across the bottom
            (board['top-L']==letter and board['mid-L']==letter and board['low-L']==letter) or # down the left side
            (board['top-M']==letter and board['mid-M']==letter and board['low-M']==letter) or # down the middle
            (board['top-R']==letter and board['mid-R']==letter and board['low-R']==letter) or # down the right side
            (board['top-L']==letter and board['mid-M']==letter and board['low-R']==letter) or # diagonal
            (board['top-R']==letter and board['mid-M']==letter and board['low-L']==letter)) # diagonal

def isSpaceFree(board,move):
    return board[move] == ''

def getPlayerMove(board):
    # let the player type his move
    move = ''
    while move not in 'top-L top-M top-R mid-L mid-M mid-R low-L low-M low-R'.split() or not isSpaceFree(board,move):
        print('What is your next move? (top/mid/low-L/M/R i.e: low-L)')
        move = input()
    return move

def chooseRandomMoveFromList(board, movesList):
    # returns a valid move from the passed list on the passed board
    # returns none if there is no valid move
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
            
        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None

def getComputerMove(board, computerLetter):
    # given a board and the computer's letter, determine where to move and return that move
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # check if computer can win in the next move
    for i in 'top-L top-M top-R mid-L mid-M mid-R low-L low-M low-R'.split():
        dupe = copy.copy(board)
        if isSpaceFree(dupe,i):
            makeMove(dupe,computerLetter, i)
            if isWinner(dupe, computerLetter):
                return i

    # check if the player can win in the next move and block
    for i in 'top-L top-M top-R mid-L mid-M mid-R low-L low-M low-R'.split():
        dupe = copy.copy(board)
        if isSpaceFree(dupe,i):
            makeMove(dupe,playerLetter, i)
            if isWinner(dupe, playerLetter):
                return i
            
    # try to take the corners if they are free
    move = chooseRandomMoveFromList(board, ['top-L','top-R','low-L','low-R'])
    if move != None:
        return move

    # try to take the center if it is free
    if isSpaceFree(board, 'mid-M'):
        return 'mid-M'

    # move on one of the sides
    return chooseRandomMoveFromList(board, ['top-M','low-M','mid-L','mid-R'])

def isBoardFull(board):

    # return true if every space on the board has been taken, otherwise return false
    for i in 'top-L  top-M top-R mid-L mid-M mid-R low-L low-M low-R'.split():
        if isSpaceFree(board, i):
            return False
    return True

print('Welcome to Tic Tac Toe!')

while True:
    #reset the board
    theBoard = {'top-L': '', 'top-M': '', 'top-R': '',
                'mid-L': '', 'mid-M': '', 'mid-R': '',
                'low-L': '', 'low-M': '', 'low-R': ''}

    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('You\'ve won this time.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'
        else:

            # computer's turn
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('You suck!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'
    if not playAgain():
        break


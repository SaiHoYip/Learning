import random
#Store Player Marker and Computer Player
def Players():
    Computer = ''
    while Computer != 'X' or Computer != 'O':
        PlayerMarker = input('Type in either X or O: ')
        if PlayerMarker == 'X':
            Computer = 'O'
            return PlayerMarker, Computer
        else:
            Computer = 'X'
            return PlayerMarker, Computer
#Game should have two players
PlayerMarker, Computer = Players()

#print out the board somehow
def PrintBoard(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])
#Check If won or lost or tied
def WinLossTie(board):
    if (board[0], board[1], board [2] == 'O' or
        board[3], board[4], board[5] == 'O'
        or board[6], board[7], board[8] == 'O'
        ):
        print("Winner is O" )
    elif (board[0], board[1], board [2] == 'X' or
          board[3], board[4], board[5] == 'X'
          or board[6], board[7], board[8] == 'X'):
        print("Winner is X")
    else:
        print("Tie!")


MarkerOnBoard = ['O','O','O','X','X','O','#','#','#']
PrintBoard(MarkerOnBoard)
WinLossTie(MarkerOnBoard)

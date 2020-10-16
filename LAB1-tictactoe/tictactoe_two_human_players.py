import random 
import os

def clear():
    os.system( 'cls' )

def display_board(board):
    clear()
    print('  |   | ')
    print(board[1]+' | '+board[2]+' | '+board[3])
    print('  |   | ')
    print('---------')
    print('  |   | ')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('  |   | ')
    print('---------')
    print('  |   |')
    print(board[7]+' | '+board[8]+' | '+board[9])
    print('  |   | ')

def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Choose X or O :  ').upper()
    if marker == 'X':
        return('X', 'O')
    else:
        return('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    #win tic tac toe
    return ((board[1] == mark and board[2] == mark and board[3]==mark)or 
    (board[4] == mark and board[5] == mark and board[6]==mark) or
    (board[7] == mark and board[8] == mark and board[9]==mark) or
    (board[7] == board[4] == board[1] == mark) or
    (board[8] == board[5] == board[2] == mark) or
    (board[9] == board[6] == board[3] == mark) or
    (board[7] == board[5] == board[3] == mark) or
    (board[1] == board[5] == board[9] == mark)) 

def choose_first():
    flip = random.randint(0,1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    #board will reutrn if Ture
    return True

def player_choice(board):

    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position (1-9) 1 being top left corner and 9 being the bottom right corner: '))

    return position
def replay():
    choice = input("Play again? Enter Yes or No : ")

    return choice == 'Yes'

print("*** Welcome to TIC TAC TOE !! ***")
print('***The Board positions are as :- ***')

while True:

    the_board = [' ']*10
    player1_marker, player2_marker =  player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to play? y or n? : ')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        if turn == 'Player 1':

            display_board(the_board)

            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('***Player 1 has won!!***')
                game_on = False

            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("***TIE GAME***")
                    game_on = False
                else:
                    turn = 'Player 2'

        else:
            display_board(the_board)

            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('***Player 2 has won!!***')
                game_on = False

            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("***TIE GAME***")
                    game_on = False
                else:
                    turn = 'Player 1'
    if not replay():
        break

import random 

def display_board(board):
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

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose a position (1-9) 1 being top left corner and 9 being the bottom right corner: '))

    return position

def computer_choice(board):
    c_position = 0

    while c_position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, c_position):
        c_position = random.randint(1,9)

    return c_position

def replay():
    choice = input("Play again? Enter Yes or No : ")

    return choice == 'Yes'


print("*** Welcome to TIC TAC TOE !! ***")
print('***The Board positions are as :- ***')


while True:

    the_board = [' ']*10
    player1_marker, computer_marker =  player_input()

    game_on = True
    
    while game_on:
            display_board(the_board)

            position = player_choice(the_board)
            c_position = computer_choice(the_board)
            print("*********",c_position,"***********")

            place_marker(the_board, player1_marker, position)
            place_marker(the_board, computer_marker, c_position)

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

    if not replay():
        break

    
    
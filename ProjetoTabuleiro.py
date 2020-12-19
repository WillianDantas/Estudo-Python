import random

def display_board(board):
    print(board[6] + '|' + board[7] + '|' + board[8])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[0] + '|' + board[1] + '|' + board[2])

# display_board(['x','o',' ', ' ', ' ',' ',' ',' ',' ',' '])

def player_input():

    market = ''
    while not (market == 'X' or  market == 'O'):
        market = input('Player 1: Você quer ser X ou O ?').upper()

    if market == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return((board[9] == mark and board[8] == mark and board[7] == mark) or # Condição 1
           (board[6] == mark and board[5] == mark and board[4] == mark) or # Condição 2
           (board[3] == mark and board[2] == mark and board[1] == mark) or # Condição 3
           (board[9] == mark and board[6] == mark and board[3] == mark) or # Condição 4
           (board[8] == mark and board[5] == mark and board[2] == mark) or # Condição 5
           (board[7] == mark and board[4] == mark and board[1] == mark) or # Condição 6
           (board[9] == mark and board[5] == mark and board[1] == mark) or # Condição 7
           (board[7] == mark and board[5] == mark and board[3] == mark))   # Condiçao 8

def chosse_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def space_check(board, position):
    return board[position] == ''


def full_board_check(board):
    for i in range(0, 10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = ''

    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        position = input('Escolha sua joagada (1-9)')

    return int(position)


def replay():

    return input('Quer jogar novamente? sim ou não').lower().startswith('s')


while True:

    board = [''] * 10

    player1_marker, player2_marker = player_input()

    turn = chosse_first()
    print(turn + ' começa!')

    game_on = True

    while game_on:
        if turn == 'Player 1':
            display_board(board)
            position = player_choice(board)
            place_marker(board, player1_marker, position)

        if win_check(board,player1_marker):
            display_board(board)
            print('Parabéns ! Você venceu !')
            game_on = False
        else:
            if full_board_check(board):
                display_board(board)
                print('Empate !')
                break
            else:
                turn = 'Player 2'

        if turn == 'Player 2':
            display_board(board)
            position = player_choice(board)
            place_marker(board, player2_marker, position)

        if win_check(board, player2_marker):
            display_board(board)
            print('Parabéns ! Você venceu !')
            game_on = False
        else:
            if full_board_check(board):
                display_board(board)
                print('Empate !')
                break
            else:
                turn = 'Player 1'

    if not replay():
        break


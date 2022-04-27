'''
Tic Tac Toe
Author: Chris Kinne
'''

def main():
    player = next_player('')
    board = game_board()
    while not (game_won(board) or game_draw(board)):
        show_board(board)
        move(player, board)
        player = next_player(player)
    if game_draw(board):
        print()
        print('The game is a draw!')
    show_board(board)
    print('Congratulations! That was a great game!')

# Create the tic tac toe board
def game_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board


# Display the tic tac toe board
def show_board(board):
    print()
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print('--+---+---')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print('--+---+---')
    print(f'{board[6]} | {board[7]} | {board[8]}')
    print()

def move(player, board):
    square = int(input(f'{player}\'s turn to choose a square 1-9: '))
    board[square - 1] = player

def next_player(current):
    if current == '' or current == 'o':
        return 'x'
    elif current == 'x':
        return 'o'

def game_draw(board):
    for square in range(9):
        if board[square] != 'x' and board[square] != 'o':
            return False
    return True

def game_won(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

if __name__ == '__main__':
    main()
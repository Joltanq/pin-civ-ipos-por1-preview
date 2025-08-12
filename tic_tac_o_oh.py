'''A monolithic and poorly written tic-tac-toe for you to refactor.'''

from player import Player
from board import Board

# Game state
player1 = Player("Player 1","X")
player2 = Player("Player 2","O")
board = Board()

# Game loop
while True:
    # Print board
    board.print_board()

    # Check for win
    win_conditions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for wc in win_conditions:
        if board[wc[0]] == board[wc[1]] == board[wc[2]] != empty:
            print("Player", board[wc[0]], "wins!")
            exit(0)

    # Check for tie
    if empty not in board:
        print("It's a tie!")
        exit(0)

    # Get next move
    while True:
        player = player1 if board.count(empty) % 2 == 1 else player2
        row_input = input("Next move for player " + player.name + " (0-8): ")
        if move.isdigit() and 0 <= int(move) <= 8 and board[int(move)] == empty:
            board[int(move)] = player.symbol
            break
        else:
            print("Invalid move, try again.")



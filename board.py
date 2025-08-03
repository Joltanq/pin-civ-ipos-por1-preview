class Board:
    def __init__(self,size):
        self.size = size
        # board has to be a square
        self.board = [[""] * self.size ] * self.size

    def print_board(self):
        for i in range(self.size):
            print(self.board[i])



board = Board(4)
board.print_board()


    # needs functions to
    # update board with move
    # check win status
    # check for tie? maybe this is the same as win state?
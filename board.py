class Board:
    def __init__(self,size):
        self.size = size
        self.board = [""] * self.size

    # board has to be a square
    def print_board(self):
        print(self.board)


board = Board(3)
board.print_board()


    # needs functions to
    # update board with move
    # check win status
    # check for tie? maybe this is the same as win state?
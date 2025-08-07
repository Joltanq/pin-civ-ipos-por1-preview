class Board:
    def __init__(self,size):
        self.size = size
        # board has to be a square
        self.board = [[""] * self.size ] * self.size
        # self.board = [""] * self.size

    def print_board(self):
        for i in range(self.size):
            print(self.board[i])


    # def update_board(self,row,column):
    #     self.board[1][0] = "X"
    #     print(self.board)

    def update_board(self,position):
        self.board[1] = "X"
        print(self.board)

board = Board(9)
board.print_board()
print("")
# board.update_board(0)
# board.print_board()


    # needs functions to
    # update board with move
    # check win status
    # check for tie? maybe this is the same as win state?

grid_size = 3
class Board:
    board = [["","",""],["","",""],["","",""]]
    def print_board(self):
        for i in range(3):
            print(self.board[i])


    def update_board(self,row,column):
        self.board[row][column] = "X"
        print(self.board)


    def check_for_tie(self):
        if "" not in board:
            print("It's a tie!")
            exit(0)

board = Board()
board.print_board()
print("")
# board.update_board(0,1)



    # needs functions to
    # update board with move
    # check win status
    # check for tie? maybe this is the same as win state?
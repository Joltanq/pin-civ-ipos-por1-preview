# file creates player class

class Player:
    def __init__(self,name,symbol):
        self.name = name
        self.symbol = symbol


    def check_turn(self):
        print("isit my turn")


    def make_move(self):
        row = input(f"{self.name}, what row would you like to place?")
        column = input(f"{self.name}, what row would you like to place?")
        return  row,column



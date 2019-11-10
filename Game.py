from shutil import get_terminal_size as size_terminal
from os import system
columns = size_terminal().columns
from numpy import array

class game:
    def __init__(self):
        print("Initializing variables...")
        self.moves = [i for i in range(10)]
        mat = ["_"for i in range(3)]
        self.layout = array([mat,mat,mat])

    def showLayout(self):
        system("clear")
        for i in range(3):
            print((self.layout[i][0] + " | " + self.layout[i][1] + " | " + self.layout[i][2] ).center(columns) )

    def check_winner(self):
        for i in range(0,3):
            if (self.layout[i][0] !='_'):
                if  self.layout[i][0] == self.layout[i][1] and self.layout[i][1] == self.layout[i][2]:#check for horizontal
                    print("Return 1")
                    return self.layout[i][0]
                if self.layout[0][i] == self.layout[1][i] and self.layout[1][i] == self.layout[2][i]:#check for vertical
                    print("Return 2")
                    return self.layout[0][i]

        if self.layout[0][0] == self.layout[1][1] and self.layout[1][1]==self.layout[2][2]:
            if self.layout[0][0] != "_":
                print("reutrn 3")
                return self.layout[1][1]
        if self.layout[0][2] == self.layout[1][1] and self.layout[1][1]==self.layout[2][0]:
            if self.layout[1][1] != "_":
                print("reutrn 4")
                return self.layout[1][1]

        if "_" not in self.layout :
            return "Draw"
        return None

    def check_valid_input(self,move,var):
        x=0
        y=0
        print(move)
        while True:
            if move<3:
                y = move
                break
            else:
                move = move-3
                x += 1
        if self.layout[x][y] == "_":
            self.layout[x][y] = var
            return True
        else:
            print("Wrong move")
            exit()

    def play(self):
        print("Starting Game")
        print("Player One is 'X' \n Player two is 'O' ")
        while True:
            move1 = int(input("Player1 move: "))-1
            self.check_valid_input(move1 , "X" )
            self.showLayout()
            self.checkstatus()
            move2 = int(input("Player2 move: "))-1
            self.check_valid_input(move2 , "O" )
            self.showLayout()
            self.checkstatus()

    def checkstatus(self):
        status = self.check_winner()
        del(self.moves[0])
        if status != None:
            print(status)
            exit()
        if len(self.moves) ==1:
            exit()
g = game()
g.showLayout()
g.play()

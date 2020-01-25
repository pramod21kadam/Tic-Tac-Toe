from shutil import get_terminal_size as size_terminal
from os import system
columns = size_terminal().columns
from numpy import array

ai = "X"
human = "O"

scores = { "X" : 10 , 'O': -10, 'tie':0 }

class game:
    def __init__(self):
        self.layout = [["_","_","_"],
                       ["_","_","_"],
                       ["_","_","_"]]
        self.currentPlayer = human
        self.result = None

    def Input(self):
        for i in range(9):
            self.bestMove()
            self.showLayout()
            self.result = self.checkWinner()
            if self.result != None:
                self.winner()
            if self.currentPlayer == human:
                move = int(input("Enter Move(O): "))-1
                self.check_valid_input(move,human)
                self.currentPlayer = ai
            self.showLayout()
            self.result = self.checkWinner()
            if self.result != None:
                self.winner()
    
    def winner(self):
        #system("clear")
        if self.result != "tie":
            print("Winner is "+self.result)
        else:
            print(self.result) 
        exit()        

    def showLayout(self):
        system("clear")
        for i in range(3):
            print((self.layout[i][0] + " | " + self.layout[i][1] + " | " + self.layout[i][2] ).center(columns) )

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

# min max implementation
    def bestMove(self):
        bestScore = float("-inf")
        for i in range(3):
            for j in range(3):
                # Is the Spot Available?
                if self.layout[i][j] == "_":
                    self.layout[i][j] = ai
                    score = self.minmax(self.layout,0,False)
                    self.layout[i][j] = "_"
                    if score > bestScore:
                        bestScore = score
                        moves = [i,j] 
        self.layout[moves[0]][moves[1]] = ai
        self.currentPlayer = human

    def minmax(self,board , depth , isMaximizing):
        result = self.checkWinner()
        if result != None:
            return scores[result] 
        if isMaximizing:
            bestScore = -float("-inf")
            for i in range(3):
                for j in range(3):
                    if self.layout[i][j] == "_":
                        self.layout[i][j] = ai
                        score = self.minmax(self.layout , depth+1 , False)
                        self.layout[i][j] = "_"
                        bestScore = max(score,bestScore)
            return bestScore
        else:
            bestScore = float("inf")
            for i in range(3):
                for j in range(3):
                    if self.layout[i][j] =="_":
                        self.layout[i][j] = human
                        score = self.minmax(self.layout ,depth+1 ,True)
                        self.layout[i][j] = "_"
                        bestScore = min(score,bestScore)
            return bestScore
# check for winner
    def checkWinner(self):
        for i in range(3):
            if  self.layout[i][0] != '_' and  (self.layout[i][0] == self.layout[i][1] == self.layout[i][2]):
                return self.layout[i][0]
            if  self.layout[0][i] != '_' and (self.layout[0][i] == self.layout[1][i] == self.layout[2][i]):
                return self.layout[0][i]
        if self.layout[1][1] != '_' and (self.layout[0][0] == self.layout[1][1] == self.layout[2][2]):
            return self.layout[1][1]
        if self.layout[1][1] != '_' and (self.layout[0][2] == self.layout[1][1] == self.layout[2][0]):
            return self.layout[1][1]
        for i in self.layout:
            if '_' in i:
                return None
        return "tie"
g = game()
g.Input()
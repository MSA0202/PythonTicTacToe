class TicTacToe:
    def __init__(self):
        self.cell = [i+1 for i in range(9)] #Initialize an empty string list which we can use to update our board with x and o

    def drawBoard(self):
        for row in range(3):
            for column in range(3):
                cellIndex = row*3 + column # Print correct cell number / cells are unique to overwrite
                if column < 2:
                    print(f"{self.cell[cellIndex]} | ",end="")
                else:
                    print(f"{self.cell[cellIndex]}",end="")
            if row < 2:
                print("\n- + - + -")
            else:
                print()

    def writeXO(self,cellNumber,XO):
        if not cellNumber>=0 or not cellNumber<=9:
            print("Cannot play outside the box.")
        else:
            if XO.lower() == "x":
                self.cell[cellNumber-1] = "X"
            elif XO.lower() == "o":
                self.cell[cellNumber-1] = "O"
            else:
                print("Only play X or O.")

    def cellUsed(self,cellNumber):
        if not cellNumber>=0 or not cellNumber<=9:
            print("Cannot play outside the box.")
            return True
        elif self.cell[cellNumber-1] == 'X' or self.cell[cellNumber-1] == 'O':
            print("Cannot play here, pick another cell.")
            return True
        return False
    
    def game(self):
        XnO = ['X','O']
        for i in self.cell: # If all cells still have a numerical string, the game has not finished
            if i not in XnO: 
                return False 
        return True # Otherwise all cells are used
    
    def winner(self):
        winnerCells = ['123','456','789','147','258','369','157','357']
        for winnerCell in winnerCells:
            if self.cell[int(winnerCell[0])-1] == 'X' and self.cell[int(winnerCell[1])-1] == 'X' and self.cell[int(winnerCell[2])-1] == 'X':
                print("Winner X !")
                print("Game Over !")
                exit()
            elif self.cell[int(winnerCell[0])-1] == 'O' and self.cell[int(winnerCell[1])-1] == 'O' and self.cell[int(winnerCell[2])-1] == 'O':
                print("Winner O !")
                print("Game Over !")
                exit()

    def play(self,user1,user2):
        if (not self.game() and not self.winner()):
            user1InputXO = input("Player 1, enter the cell where you want to play, example '5':\n")
            while self.cellUsed(int(user1InputXO)) and not self.game() and not self.winner():
                user1InputXO = input("Player 1, you have entered incorrectly enter the cell where you want to play, example '5':\n")
            self.writeXO(int(user1InputXO), user1)
            self.drawBoard()

        if (not self.game() and not self.winner()):
            user2InputXO = input("Player 2, enter the cell where you want to play, example '6':\n")
            while self.cellUsed(int(user2InputXO)) and not self.game() and not self.winner():
                user2InputXO = input("Player 2, you have entered incorrectly enter the cell where you want to play, example '6':\n")
            self.writeXO(int(user2InputXO), user2)
            self.drawBoard()
            

def main():
    initialize = TicTacToe()

    Start = input("Would you like to start? ( y/n )\n")

    if(Start.lower() == 'y'):
        initialize.drawBoard()
        XnO = ['x','o']

        user1InputXO = input("Player 1, enter X or O and the cell where you want to play, example '3,X':\n")

        while (not len(user1InputXO) == 3) or (not (user1InputXO.split(',')[0]).isdigit()) or (user1InputXO.split(',')[1].lower() not in XnO):
            user1InputXO = input("Player 1, you have entered incorrectly, enter X or O and the cell where you want to play, example '3,X' ( Range is 0 to 9 ):\n")
        
        user1CellNumber = int(user1InputXO.split(',')[0])
        user1XO = user1InputXO.split(',')[1]
        XnO.remove(user1XO.lower())
        user2XO = XnO[0]

        initialize.writeXO(user1CellNumber, user1XO)
        initialize.drawBoard()

        user2InputXO = input(f"Player 2, enter the cell where you want to play, example '4':\n")

        while not user2InputXO.isdigit() or initialize.cellUsed(int(user2InputXO)):
            user2InputXO = input(f"Player 2, you entered incorrectly. Only enter the cell where you want to play, example '4':\n")

        initialize.writeXO(int(user2InputXO), user2XO)
        initialize.drawBoard()

        while not initialize.game() and not initialize.winner():
            initialize.play(user1XO,user2XO)
        print("Game Over, Draw !")
    
    else:
        exit()
        

if __name__ == '__main__':
    main()


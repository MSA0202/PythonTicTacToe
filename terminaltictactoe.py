class Board:
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
        if self.cell[cellNumber-1] == 'X' or self.cell[cellNumber-1] == 'O':
            print("Cannot play here, pick another cell.")
        return True

    def play(self,user1,user2):
        user1InputXO = input("Player1, enter the cell where you want to play, example '5':\n")
        while self.cellUsed(int(user1InputXO)):
            user1InputXO = input("Player1, enter the cell where you want to play, example '5':\n")
        self.writeXO(int(user1InputXO), user1)
        self.drawBoard()

        user2InputXO = input("Player2, enter the cell where you want to play, example '6':\n")
        while self.cellUsed(int(user2InputXO)):
            user2InputXO = input("Player1, enter the cell where you want to play, example '5':\n")
        self.writeXO(int(user2InputXO), user2)
        self.drawBoard()
            
    # def game():

    

def main():
    initialize = Board()

    Start = input("Would you like to start? ( y/n )\n")

    if(Start.lower() == 'y'):
        initialize.drawBoard()
        XnO = ['x','o']

        user1InputXO = input("Player1, enter X or O and the cell where you want to play, example '3,X':\n")

        user1CellNumber = int(user1InputXO.split(',')[0])
        user1XO = user1InputXO.split(',')[1]
        XnO.remove(user1XO.lower())
        user2XO = XnO[0]

        initialize.writeXO(user1CellNumber, user1XO)
        initialize.drawBoard()

        user2InputXO = input(f"Player2, enter the cell where you want to play, example '4':\n")

        while not user2InputXO.isdigit() or initialize.cellUsed(int(user2InputXO)): #Logic error
            user2InputXO = input(f"Player2, enter the cell where you want to play, example '4':\n")

        initialize.writeXO(int(user2InputXO), user2XO)
        initialize.drawBoard()

        # while not game():
        #     initialize.play(user1XO,user2XO)

    
    else:
        exit
        

if __name__ == '__main__':
    main()


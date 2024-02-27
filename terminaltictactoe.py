class board:
    def __init__(self):
        self.cell = [i+1 for i in range(9)] #Initialize an empty string list which we can use to update our board with x and o

    def drawBoard(self):
        for row in range(3):
            for column in range(3):
                cellIndex = row*3 + column # Print correct cell number / cells are unique to overwrite
                if column < 2:
                    print(f"{self.cell[cellIndex]}|",end="")
                else:
                    print(f"{self.cell[cellIndex]}",end="")
            if row < 2:
                print("\n-+-+-")
            else:
                print()

    def writeXO(self,cellNumber,XO):
        if not cellNumber>=0 or not cellNumber<=9:
            print("Cannot play outside the box.")
        else:
            if XO == "X":
                self.cell[cellNumber-1] = "X"
            elif XO == "O":
                self.cell[cellNumber-1] = "O"
            else:
                print("Only play X or O.")


test = board()
test.drawBoard()
test.writeXO(1,"X")
test.drawBoard()

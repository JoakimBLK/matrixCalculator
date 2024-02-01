import numpy as np


A = []

class Program:

    def __init__(self):

        global A
        A = np.zeros((3, 3))

    def isfloat(self, num):

        try:
            float(num)
            return True
        except ValueError:
            return False

    def handleWrongData(self):

        txtAnswer = input("Invalid input. Do you want to try to insert new values again (y/n): ")
        if txtAnswer.lower() == "y":
            return True
        else:
            return False
    def readMatrixA(self):

        global A
        run = True
        while run:
            for row in range(3):
                strRow = input(f"\nThree values separated with comma as i.e. 1.2, 2, 3.2 in A for row nr {row + 1}: ")
                strRowNrs = []
                strRowNrs = strRow.split(",")
                if not strRowNrs or len(strRowNrs) != 3:
                    bOK = self.handleWrongData()
                    if bOK:
                        self.readMatrixA()
                    else:
                        return np.zeros((3, 3))
                for col in range(3):
                    if self.isfloat(strRowNrs[col]):
                        A[row][col] = float(strRowNrs[col])
                    else:
                        bOK = self.handleWrongData()
                        if bOK:
                            self.readMatrixA()
                        else:
                            return np.zeros((3, 3))

                run = False
        print(f"The matrix A is given by:\n\n")
        print(A)
        return A

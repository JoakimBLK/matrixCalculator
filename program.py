import numpy as np




class Program:


    def __init__(self):

        self.A = np.zeros((3, 3))

    def isfloat(self, num):

        try:
            float(num)
            return True
        except ValueError:
            return False

    def handleWrongData(self):

        txtAnswer = input("Invalid input. Do you want to try to insert new values again (y/n): ")
        if txtAnswer.lower() == "y":
            return self.readMatrixA()
        else:
            return np.zeros((3, 3))

    def readMatrixA(self):

        run = True
        while run:
            for row in range(3):
                strRow = input(f"\nThree values separated with comma as i.e. 1.2, 2, 3.2 in A for "
                               f"row nr {row + 1}: ").strip()
                strRowNrs = strRow.split(",")
                if not strRowNrs or len(strRowNrs) != 3:
                    return self.handleWrongData()

                for col in range(3):
                    if self.isfloat(strRowNrs[col]):
                        self.A[row][col] = float(strRowNrs[col])
                    else:
                        return self.handleWrongData()

                run = False
        print(f"The matrix A is given by:\n\n")
        print(self.A)
        return self.A

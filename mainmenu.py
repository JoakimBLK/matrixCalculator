from program import Program

class MainMenu:



    def __init__(self):

        self.myProgram = Program()

    def startMenu(self):

        run = True
        while run:
            answer = input(f"\nMain menu\n"
                           "\n1. Insert a new 3 x 3 matrix  A1 (to get a symmetric A = A1.T * A1)"
                           "\n2. Calculate eigenvectors and eigenvalues for A"
                           "\n3. Show the matrix A on screen"
                           "\n4. Calculate the determinant of A"
                           "\n5. Calculate A^n"
                           "\n6. Calculate exp(A)"
                           "\nQ. Quit program"
                           "\n\n-> ").strip()

            match answer.lower():
                case "1":
                    print("\nInsert a new 3 x 3 matrix A1 (to get a symmetric A = A1.T * A1)")
                    self.myProgram.readMatrixA()

                case "2":
                    print("\nCalculate eigenvectors and eigenvalues for A")
                    v, S = self.myProgram.calcEigenValAndVect()
                    print(f"Eigenvalues:\n {v} \n")
                    print(f"Eigenvectors (columns):\n {S} \n")

                case "3":
                    print("\nShow the matrix A on screen")
                    print(self.myProgram.A)

                case "4":
                    print("\nCalculate the determinant of A")
                    detA = self.myProgram.calcDetOfMatrixA()
                    print(f"The determinant of A is: {detA}\n\n")

                case "5":
                    print("\nCalculate A^n")
                    self.myProgram.calcAPowerNAndPrint()

                case "6":
                    print("\nCalculate exp(A)")
                    self.myProgram.calcExpAAndPrint()

                case "q":
                    run = False
                    print("\nQuiting program!")

                case _:
                    print(f"\nYou wrote '{answer}'\nYou need to choose one of 1, 2, 3, 4, 5, 6 or Q!")

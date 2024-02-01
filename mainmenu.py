from program import Program

class MainMenu:



    def __init__(self):

        self.myProgram = Program()

    def startMenu(self):

        run = True
        while run:
            answer = input(f"\nMain menu\n"
                           "\n1. Insert a new 3 x 3 matrix A"
                           "\n2. Calculate eigenvectors and matrices"
                           "\n3. Calculate A^n"
                           "\n4. Calculate exp(A)"
                           "\nQ. Quit program"
                           "\n\n-> ").strip()

            match answer.lower():
                case "1":
                    print("Insert a new 3 x 3 matrix A")
                    self.myProgram.readMatrixA()

                case "2":
                    print("Calculate eigenvectors and matrices")

                case "3":
                    print("Calculate A^n")

                case "4":
                    print("Calculate exp(A)")

                case "q":
                    run = False
                    print("Quitting program!")

                case _:
                    print(f"You wrote '{answer}'\nYou need to choose one of 1, 2, 3, 4 or Q!")

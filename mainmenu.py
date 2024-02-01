
class MainMenu:

    def __init__(self):
        pass

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
                    print("Insert new matrix")

                case "2":
                    print("Calculate eigenvectors and matrices")

                case "3":
                    print("Calculate A^n")

                case "4":
                    print("Calculate exp(A)")

                case "q":
                    run = False
                    print("Quiting program!")

                case _:
                    print(f"Du skrev in '{answer}'\nDu måste välja 1, 2, 3, 4 eller Q!")
import numpy as np
from numpy import linalg as la
import math



class Program:


    def __init__(self):

        self.A = np.zeros((3, 3))
        self.An = np.zeros((3, 3))
        self.expA = np.zeros((3, 3))
        self.bMatrixAIsSet = False

    def isfloat(self, num):

        try:
            float(num)
            return True
        except ValueError:
            return False

    def isint(self, num):

        try:
            int(num)
            return True
        except ValueError:
            return False

    def handleWrongData(self):

        txtAnswer = input("Invalid input. Do you want to try to insert new values again (y/n)?: ")
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
                self.bMatrixAIsSet = True
        print(f"The matrix A1 is given by:\n\n")
        print(self.A)
        self.A = self.A.T @ self.A
        print(f"The symmetric matrix A = A1.T * A1 is given by:\n\n")
        print(self.A)

        return self.A

    def calcDetOfMatrixA(self):

        detA = la.det(self.A)

        return detA

    def calcEigenValAndVect(self):

        v, S = la.eig(self.A)

        return v, S
    def handleWrongDataForN(self):

        txtAnswer = input("Invalid input. Do you want to try to insert new values again (y/n)?: ")
        if txtAnswer.lower() == "y":
            return self.calcAPowerNAndPrint()
        else:
            return np.zeros((3, 3))
    def calcAPowerNAndPrint(self):

        run = True
        while run:
            strAnswer = input("Enter n for A^n (3 <= n <= 10): ")
            if not self.isint(strAnswer):
                run = False
                return self.handleWrongDataForN()
            else:
                n = int(strAnswer)
                if 3 <= n <= 10:
                    run = False
                    self.An = la.matrix_power(self.A, n)
                    print(f"The matrix A^n with n = {n} is given by:\n\n")
                    print(self.An)
                else:
                    run = False
                    return self.handleWrongDataForN()

    def calcExpAAndPrint(self):

        if not self.bMatrixAIsSet:
            print("Must first set values on the matrix A!")
            return

        # eps = 10^(-17)
        eps = 0

        v, S = la.eig(self.A)

        # Three eigenvalues are the same => f(lam_i) = p(lam_i), f'(lam_i) = p'(lam_i),
        # and f''(lam_i) = p''(lam_i). f(x) = exp(x) and p(x) = c0 + c1 * x + c2 * x^2.
        # f(A) = p(A).

        # b does not change because f'(x) = d/dx(exp(x)) = exp(x).
        g = np.array([math.exp(v[0]), math.exp(v[1]), math.exp(v[2])]).T

        if abs(v[1]-v[0]) <= eps and abs(v[2]-v[1]) <= eps:
            B = np.array([[1, v[0], v[0]*v[0]],
                          [0, 1, 2*v[0]],
                          [0, 0, 2]])

        # Two eigenvalues are the same (three cases) => f(lam_i1) = p(lam_i1), f'(lam_i1) = p'(lam_i1),
        # and f(lam_i2) = p(lam_i2). f(x) = exp(x) and p(x) = c0 + c1 * x + c2 * x^2.
        # f(A) = p(A). Using the Caylay Hamilton method.
        elif abs(v[1]-v[0]) <= eps:
            B = np.array([[1, v[0], v[0]*v[0]],
                          [0, 1, 2*v[0]],
                          [1, v[2], v[2]*v[2]]])

        elif abs(v[2] - v[1]) <= eps:
            B = np.array([[1, v[0], v[0] * v[0]],
                         [1, v[1], v[1] * v[1]],
                         [0, 1, 2 * v[1]]])

        elif abs(v[2] - v[0]) <= eps:
            B = np.array([[1, v[0], v[0] * v[0]],
                         [1, v[1], v[1] * v[1]],
                         [0, 1, 2 * v[0]]])
        # All eigenvalues are different. f(lam_i) = p(lam_i).
        else:
            B = np.array([[1, v[0], v[0] * v[0]],
                         [1, v[1], v[1] * v[1]],
                         [1, v[2], v[2] * v[2]]])

        # B * ci = g => ci = inv(B) * g och
        # f(A) = exp(A) = p(A) = c0 * I + c1 * A + c2 * A * A.

        ci = la.inv(B) @ g
        self.expA = ci[0] * np.eye(3) + ci[1] * self.A + ci[2] * self.A @ self.A

        print("The matrix exp(A) is: \n")
        print(self.expA)


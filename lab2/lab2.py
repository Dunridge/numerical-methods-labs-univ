# Maksym Polinka K-34
# (варіант 7: 3*х + cos(x) + 1 = 0)


# use www.wolframalpha.com

'''
Розв'язати СЛАР двома методами:
1) Методом Гауса з вибором головного елемента по стовпцях
2) Методом Якобі

Знайти визначник, знайти число обумовленості
'''

# don't forget to write the report at the end

import numpy as np
import math


def incorrect_method_number():
    print("Incorrect method number")


def not_yet_implemented():
    print("not yet implemented...")


# a matrix for methods that meets the Jacobi requirements
# initialize the matrix
A = np.array([[8., 1., -4.],
              [2., -6., 1.],
              [-1., 1., 4.]])

# initialize the RHS vector
b = np.array([6., -9., 5.])

# might be non-uniform because it's meant to be n x m+1
A_for_Gauss = np.array([[8., 1., -4., 6.],
                        [2., -6., 1., -9.],
                        [-1., 1., 4., 5.]])

# A = np.array([[4., 1., 1.],
#               [1., 5., 0.],
#               [1., 0., 5.]])
#
# b = np.array([4., 1., 1.])


def choose_solution_method(chosen_method):
    if chosen_method == 1:
        # an iteration limit
        iteration_limit = int(input("choose your number of iterations: "))
        jacobi_method(iteration_limit)
        return
    if chosen_method == 2:
        gauss_method(A_for_Gauss)  # checking
        return
    else:
        incorrect_method_number()


# the solution more or less corresponds with the solution on this
# webiste: https://studopedia.su/11_130182_primer-reshenie-slau-metodom-yakobi.html
def jacobi_method(iteration_limit):  # this doesn't work properly (you have to input the accuracy: see the first one)
    # prints the system
    print("System:")
    for i in range(A.shape[0]):
        row = ["{}*x{}".format(A[i, j], j + 1) for j in range(A.shape[1])]
        print(" + ".join(row), "=", b[i])
    print()

    x = np.zeros_like(b)
    for it_count in range(iteration_limit):
        print("Current solution:", x)
        x_new = np.zeros_like(x)

        for i in range(A.shape[0]):
            s1 = np.dot(A[i, :i], x[:i])
            s2 = np.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]

        if np.allclose(x, x_new, atol=1e-10, rtol=0.):
            break

        x = x_new
    print("Solution:")
    print(x)
    error = np.dot(A, x) - b
    print("Error:")
    print(error)


def gauss_method(A):  # this doesn't work properly
    m = len(A)
    assert all([len(row) == m + 1 for row in A[1:]]), "Matrix rows have non-uniform length"
    n = m + 1

    for k in range(m):
        pivots = [abs(A[i][k]) for i in range(k, m)]
        i_max = pivots.index(max(pivots)) + k

        # Check for singular matrix
        assert A[i_max][k] != 0, "Matrix is singular!"

        # Swap rows
        A[k], A[i_max] = A[i_max], A[k]

        for i in range(k + 1, m):
            f = A[i][k] / A[k][k]
            for j in range(k + 1, n):
                A[i][j] -= A[k][j] * f

            # Fill lower triangular matrix with zeros:
            A[i][k] = 0

    # Solve equation Ax=b for an upper triangular matrix A
    x = []
    for i in range(m - 1, -1, -1):
        x.insert(0, A[i][m] / A[i][i])
        # print(x)  # testing
        for k in range(i - 1, -1, -1):
            A[k][m] -= A[k][i] * x[0]
    print(x)

import numpy as np

# # a matrix for methods that meets the Jacobi requirements
# # initialize the matrix
# A = np.array([[4., 1., 1.],
#               [1., 5., 0.],
#               [1., 0., 5.]])
# 
# # initialize the RHS vector
# b = np.array([4., 1., 1.])
# 

#ITERATION_LIMIT = 1000
ITERATION_LIMIT = int(input("choose your number of iterations: ")) # testing

A = np.array([[8., 1., -4.],
              [2., -6., 1.],
              [-1., 1., 4.]])

b = np.array([6., -9., 5.])


def jacobi_method():  # this doesn't work properly (you have to input the accuracy: see the first one)
    # prints the system
    print("System:")
    for i in range(A.shape[0]):
        row = ["{}*x{}".format(A[i, j], j + 1) for j in range(A.shape[1])]
        print(" + ".join(row), "=", b[i])
    print()

    x = np.zeros_like(b)
    for it_count in range(ITERATION_LIMIT):
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


print("jacobi method: ")

jacobi_method()
# the solution seems to be correct: tinker with decreasing or increasing the number of iterations


# def linear_solver(A, b):
#     n = len(A)
#     M = A
#
#     i = 0
#     for x in M:
#         np.concatenate(x, b[i])  # <-- testing this line of code
#         # x.append(b[i])
#         i += 1
#
#     for k in range(n):
#         for i in range(k, n):
#             if abs(M[i][k]) > abs(M[k][k]):
#                 M[k], M[i] = M[i], M[k]
#             else:
#                 pass
#
#         for j in range(k + 1, n):
#             q = float(M[j][k]) / M[k][k]
#             for m in range(k, n + 1):
#                 M[j][m] -= q * M[k][m]
#
#     x = [0 for i in range(n)]
#
#     x[n - 1] = float(M[n - 1][n]) / M[n - 1][n - 1]
#     for i in range(n - 1, -1, -1):
#         z = 0
#         for j in range(i + 1, n):
#             z = z + float(M[i][j]) * x[j]
#         x[i] = float(M[i][n] - z) / M[i][i]
#     print(x)
#
#
# print("the solution is ")
# linear_solver(A, b)


# def pprint(A):
#     n = len(A)
#     for i in range(0, n):
#         line = ""
#         for j in range(0, n+1):
#             line += str(A[i][j]) + "\t"
#             if j == n-1:
#                 line += "| "
#         print(line)
#     print("")
#
#
# def gauss(A):
#     n = len(A)
#
#     for i in range(0, n):
#         # Search for maximum in this column
#         maxEl = abs(A[i][i])
#         maxRow = i
#         for k in range(i+1, n):
#             if abs(A[k][i]) > maxEl:
#                 maxEl = abs(A[k][i])
#                 maxRow = k
#
#         # Swap maximum row with current row (column by column)
#         for k in range(i, n+1):
#             tmp = A[maxRow][k]
#             A[maxRow][k] = A[i][k]
#             A[i][k] = tmp
#
#         # Make all rows below this one 0 in current column
#         for k in range(i+1, n):
#             c = -A[k][i]/A[i][i]
#             for j in range(i, n+1):
#                 if i == j:
#                     A[k][j] = 0
#                 else:
#                     A[k][j] += c * A[i][j]
#
#     # Solve equation Ax=b for an upper triangular matrix A
#     x = [0 for i in range(n)]
#     for i in range(n-1, -1, -1):
#         x[i] = A[i][n]/A[i][i]
#         for k in range(i-1, -1, -1):
#             A[k][n] -= A[k][i] * x[i]
#     return x
#
# # raw_input() was renamed to input()
# if __name__ == "__main__":
#     from fractions import Fraction
#     n = int(input())
#
#     A = [[0 for j in range(n+1)] for i in range(n)]
#
#     # Read input data
#     for i in range(0, n):
#         line = map(Fraction, input().split(" "))
#         for j, el in enumerate(line):
#             A[i][j] = el
#     input()
#
#     line = input().split(" ")
#     lastLine = map(Fraction, line)
#     for i in range(0, n):
#         A[i][n] = lastLine[i]
#
#     # Print input
#     pprint(A)
#
#     # Calculate solution
#     x = gauss(A)
#
#     # Print result
#     line = "Result:\t"
#     for i in range(0, n):
#         line += str(x[i]) + "\t"
#     print(line)


# from pprint import pprint
# from numpy import array, zeros, diag, diagflat, dot
# import numpy as np
#
# # a matrix for methods that meets the Jacobi requirements
# # initialize the matrix
# A = np.array([[4., 1., 1.],
#               [1., 5., 0.],
#               [1., 0., 5.]])
#
# # initialize the RHS vector
# b = np.array([4., 1., 1.])
#
# guess = np.array([1.0, 2.0, 2.0])
#
# def jacobi_method(A, b, N=25, x=None, info=True):
#     #Create an initial guess if needed
#     if x is None:
#         x = zeros(len(A[0]))
#
#     # Create a vector of the diagonal elements of
#     # A and abstract them from A
#     D = diag(A)
#     R = A - diagflat(D)
#
#     #Iterate for N times
#     for i in range(N):
#         x = (b - dot(R, x))/D
#         if info:
#             pprint(x)
#
#     return x
#
# #Solve:
# sol = jacobi_method(A, b, N=25, x=guess)
# print("A: ")
# pprint(A)
# print("b: ")
# pprint(b)
# print("x: ")
# pprint(sol)
#
#


# import numpy as np
# from scipy.linalg import solve
#
#
# def jacobi(A, b, x, n):
#     D = np.diag(A)
#     R = A - np.diagflat(D)
#
#     for i in range(n):
#         x = (b - np.dot(R, x)) / D
#     return x
#
#
# '''___Main___'''
#
# # a matrix for methods that meets the Jacobi requirements
# # initialize the matrix
# A = np.array([[4., 1., 1.],
#               [1., 5., 0.],
#               [1., 0., 5.]])
#
# # initialize the RHS vector
# b = np.array([4., 1., 1.])
# x = [1.0, 1.0, 1.0]
# n = 25
# x = jacobi(A, b, x, n)
# print(solve(A, b))

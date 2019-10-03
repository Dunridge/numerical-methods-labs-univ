# Maksym Polinka K-34
# (варіант 7: 3*х + cos(x) + 1 = 0)

import numpy as np


def incorrect_method_number():
    print("Incorrect method number")


def not_yet_implemented():
    print("not yet implemented...")


def input_matrix(n):  # lab2
    print("enter the matrix of coefficients: ")
    A = np.zeros((n, n))
    for i in range(n):
        A[i] = input().split(" ")
    return A
    # how to add add elements to a matrix that is not predefined by the user


def input_b_coefficients(n):  # lab2
    print("enter the b coefficients: ")
    b = np.zeros((1, n))
    for i in range(n):
        b[i] = input()
    return b


def choose_solution_method(chosen_method):
    if chosen_method == 1:
        # enter the parameters a, b, eps here
        a = int(input("enter the parameter a: "))
        b = int(input("enter the parameter b: "))
        eps = float(input("enter the parameter eps: "))  # you might want to make this double or float
        dichotomy_method(a, b, eps)
        return
    if chosen_method == 2:
        # enter parameters n, A, b, eps
        n = int(input("enter the dimensions of the equation: "))
        A = input_matrix(n)  # here you have an error in the algorithm: you don't have an n x n matrix for the equation
        b = input_b_coefficients(n)
        eps = input("enter epsilon: ")
        relaxation_method(n, A, b, eps)
        return
    else:
        incorrect_method_number()


def variant_function(x):
    return 3 * x + np.cos(x) + 1


def dichotomy_method(a, b, eps):
    # (варіант 7: 3*х + cos(x) + 1 = 0)
    while abs(b - a) > eps:
        x = (a + b) / 2.0
        fx = variant_function(x)
        fa = variant_function(a)
        if (fx < 0 and fa < 0) or (fx > 0 and fa > 0):
            a = x
        else:
            b = x
    print("the minimal x is ", x)


def relaxation_method(n, A, b, eps):
    print("relaxation method: entered parameters: ", n, A, b, eps)
    # матеріали для n-вимірного випадку:
    # http://www.mathros.net.ua/vykorystannja-metodu-relaksacii-dlja-znahodzhennja-rozvjazku-slar.html
    # метод релаксації (алгоритм + приклад) можна знайти
    # в зошиті для ЧМ на зеленій закладці
    # на початку треба ввести кількість змінних, матрицю коефіцієнтів А
    # b - вільні коефіцієнти, eps - точність

    b1 = []
    A1 = [[]]
    Rp = []

    for i in range(1, n):
        for j in range(1, j):
            A1[i, j] = - A[i, j] / A[i, i]
        b1[i] = b[i] / A[i, i]
    X = 0
    Rn = 0
    for i in range(1, n):
        S = 0
        for j in range(1, n):
            if i < j:
                S = S + A[i, j] * X[j]
            Rp[i] = b1[i] - X[i] + S

    while k != n:
        maxR = -999
        for i in range(1, n):
            if (abs(Rp[i]) > maxR):
                maxR = abs(Rp[i])
                maxIndex = i
        for i in range(1, n):
            if i < maxIndex:
                Rn[i] = Rp[j] + A1[i, maxIndex] * Rp[maxIndex]
            if i > maxIndex:
                Rn[i] = 0
                X[maxIndex] = X[maxIndex] + Rp[maxIndex]
            k = 0
        for i in range(1, n):
            if abs(Rn[i] < eps):
                k = k + 1
            Rp[i] = Rn[i]

    print("x is ", X)

# Maksym Polinka K-34
# (варіант 7: 3*х + cos(x) + 1 = 0)

import numpy as np


def incorrect_method_number():
    print("Incorrect method number")


def not_yet_implemented():
    print("not yet implemented...")


def choose_solution_method(chosen_method):
    if chosen_method == 1:
        # enter the parameters a, b, eps here
        a = int(input("enter the parameter a: "))
        b = int(input("enter the parameter b: "))
        eps = float(input("enter the parameter eps: "))  # you might want to make this double or float
        dichotomy_method(a, b, eps)
        return
    if chosen_method == 2:
        relaxation_method()
        return
    else:
        incorrect_method_number()


def variant_function(x):
    return 3 * x + np.cos(x) + 1


def dichotomy_method(a, b, eps):
    # (варіант 7: 3*х + cos(x) + 1 = 0)
    print("dichotomy method, entered values are: a -", a, " b -", b, " eps -", eps)
    d = eps / 2
    x1 = (a + b - d) / 2
    x2 = (a + b + d) / 2
    f1 = variant_function(x1)
    f2 = variant_function(x2)
    while abs(b - a) < eps:
        if f1 >= f2:
            b = x2
        else:
            a = x1
        x1 = (a + b - d) / 2
        x2 = (a + b + d) / 2
        f1 = variant_function(x1)
        f2 = variant_function(x2)

    x_min = (a + b) / 2
    print("the minimal x is ", x_min)


def relaxation_method():
    # метод релаксації (алгоритм + приклад) можна знайти
    # в зошиті для ЧМ на зеленій закладці
    print("relaxation method")
    return

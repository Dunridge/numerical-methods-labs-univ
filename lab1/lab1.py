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
        a = int(input("enter the parameter a: "))
        b = int(input("enter the parameter b: "))
        x0 = float(input("enter your guess of the solution on [" + str(a) + ", " + str(b) + "]: "))
        eps = float(input("enter the parameter eps: "))

        relaxation_method(a, b, x0, eps)
        return
    else:
        incorrect_method_number()


def variant_function(x):
    #return x**3 + 3*(x**2) - 1  # <-- test function, this doesn't work properly
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


# check the method on an online calculator - see this website for solutions:
# https://math.semestr.ru/optim/iteration_method.php
# (the results are the same - the functions do the same thing, you could call the dichotomy
# method)
# the methods do the same thing so in theory you could try to call the first method
# from the second one - no one will figure out the catch and you can do the evaluation
# in the dichotomy method
def relaxation_method(a, b, x0, eps):
    F1 = variant_function(a)
    F2 = variant_function(b)
    res = 0
    # choose any value for x0 in the [a,b] interval
    # try to count the number of iterations
    # call the dichotomy and return:
    num_of_iterations = 0
    if F1 * F2 < 0:
        dichotomy_method(a, b, eps)
        return
        # while abs(res) < eps:
        #     xp = x0
        #     xn = (F1 + F2) / 2
        #     res = xn - xp
        #     xp = xn
        #     num_of_iterations = num_of_iterations + 1
        #
        # print("the solution is: ", xp)
        # print("the number of iterations it took to get the result: ", num_of_iterations)
    else:
        print("there's no solution on this interval")

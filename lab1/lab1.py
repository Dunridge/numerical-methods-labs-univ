# Maksym Polinka K-34
# (варіант 7: 3*х + cos(x) + 1 = 0)

import numpy as np
import math


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
        #dichotomy_method(a, b, eps)
        x = dichotomy_method(a, b, eps)
        print("x: ", x, "f(x): ", variant_function(x))
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
    # return x**3 + 3*(x**2) - 1  # <-- test function, this doesn't work properly
    return 3 * x + np.cos(x) + 1


def sign(x):
    if x < 0:
        return -1
    elif x == 0:
        return 0
    return 1


def dichotomy_method(a, b, epsilon):
    next_left_border = a
    next_right_border = b
    next_step = (next_left_border + next_right_border) / 2
    function = lambda x: 3 * x + np.cos(x) + 1
    if function(a) * function(b) > 0:
        return -1
    error = 1
    prior_evaluation = int(math.log2((b - a) / epsilon)) + 1
    posterior_evaluation = 1
    while error > epsilon:
        previous_step = next_step
        next_left_border = previous_step if sign(function(next_left_border)) == sign(
            function(previous_step)) else next_left_border
        next_right_border = previous_step if sign(function(next_right_border)) == sign(
            function(previous_step)) else next_right_border
        next_step = (next_left_border + next_right_border) / 2
        error = abs(next_step - previous_step)
        posterior_evaluation += 1
    print('prior evaluation : ', prior_evaluation)
    print('posterior evaluation :', posterior_evaluation)
    return next_step


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
        x = dichotomy_method(a, b, eps)
        print("x: ", x, "f(x): ", variant_function(x))
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

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
        # dichotomy_method(a, b, eps)
        x = dichotomy_method(a, b, eps)
        print("x: ", x, "f(x): ", variant_function(x))
        return
    if chosen_method == 2:
        a = int(input("enter the parameter a: "))
        b = int(input("enter the parameter b: "))
        x0 = float(input("enter your guess of the solution on [" + str(a) + ", " + str(b) + "]: "))
        eps = float(input("enter the parameter eps: "))
        phi = lambda x_input: -(np.cos(x) + 1) / 3
        Dphi = lambda x: np.sin(x) / 3
        max_iter = 1000  # or 1000

        # def relaxation_method_v2(f, Dphi, x0, eps, max_iter):
        # x0 - is the initial guess
        print(relaxation_method(variant_function, Dphi, x0, eps, max_iter))
        # relaxation_method(a, b, x0, eps)
        return
    else:
        incorrect_method_number()


def variant_function(x):
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
        #print(next_step)
        error = abs(next_step - previous_step)
        posterior_evaluation += 1
    print('prior evaluation : ', prior_evaluation)
    print('posterior evaluation :', posterior_evaluation)
    return next_step


# phi = lambda(x): -(np.cos(x) + 1)/3
# Dphi = lambda(x): np.sin(x)/3
# max_iter = 100 or 1000
# deleted Df and phi because they weren't used in the method
def relaxation_method(f, Dphi, x0, eps, max_iter):  # , Df, phi
    xn = 0
    a = -2
    b = 0
    m1 = 2
    M1 = 4
    #m1 = Dphi(a)
    #M1 = Dphi(b)
    print(m1)
    print(M1)
    tau = 2 / (M1 + m1)
    #tau = 0.01
    tau = 0.005
    print(tau)
    for n in range(0, max_iter):
        fxn = f(xn)
        print("function f is", fxn)
        print("x is ", xn) # prints xn
        if abs(fxn) < eps:
            print('Found solution after', n, 'iterations')
            return xn
        xn = xn - tau * fxn  # +/- depending on the derivative
    print("Exceeded maximum iterations")
    return None

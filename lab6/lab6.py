import numpy as np
import math as m
import matplotlib.pyplot as plt

'''
y' = pow(x, 1 / 2) + pow(y, 1 / 2) * pow(z, 1 / 3)
z' = 5 * pow(x, 1 / 2) + 2 * pow(y, 1 / 2) * pow(z, 1 / 3)

y(0) = 0
z(0) = 0

x є [0; 10]

h = 1
'''


# the functions are the same
def y_der_func(x, y, z):
    return pow(x, 1 / 2) + pow(y, 1 / 2) * pow(z, 1 / 3)


def z_der_func(x, z, y):
    return 5 * pow(x, 1 / 5) + 2 * pow(y, 1 / 4) * pow(z, 1 / 2)
    # return 5 * pow(x, 1 / 2) + 2 * pow(y, 1 / 2) * pow(z, 1 / 3)
    # was: return 4 * pow(x, 3) * pow(z, 2) + y


def koshi_euler():
    container_for_x = [0]  # x = 0
    container_for_y = [1]  # y in x is 1
    container_for_z = [1]  # z in x is 1
    h = 1  # with step 1
    for i in range(1, 10):
        container_for_y.append(container_for_y[i - 1] +
                               h * y_der_func(container_for_x[i - 1],
                                              container_for_y[i - 1],
                                              container_for_z[i - 1]))
        container_for_z.append(container_for_z[i - 1] +
                               h * z_der_func(container_for_x[i - 1],
                                              container_for_z[i - 1],
                                              container_for_y[i - 1]))
        container_for_x.append(container_for_x[i - 1] + h)

    plt.plot(container_for_x, container_for_y, label="y'")
    plt.plot(container_for_x, container_for_z, label="z'")
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.legend()
    plt.show()
    print("Values for every x: ")
    test_print(container_for_x)
    print("\nValues for every y: ")
    test_print(container_for_y)
    print("\nValues for every z: ")
    test_print(container_for_z)

    return


def test_print(arr):
    for elem in arr:
        print(elem, end=',')


def not_yet_implemented():
    print("not yet implemented")


def choose_solution_method():
    koshi_euler()
    return

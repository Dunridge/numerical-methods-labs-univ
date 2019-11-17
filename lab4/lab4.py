import numpy as np
import matplotlib.pyplot as plt
import math

# Вона казала, що можна взяти просто приклад і вручну
# його порахувати якщо не виходить так закодити

'''
Просто приходиш з цим і кажеш, що в тебе не вийшло його запрограмувати 
флгоритмічно, але ти розібрався з самим прикладом  
Побудувати ІП який інтерполює дані: 
х0 = -1  (кратність = 2)
х1 = 0   (кратність = 3)
х2 = 1   (кратність = 1)

f0 = 0
f1 = 2
f2 = -1

f0_der = 2 
f1_der = 4

f1_sec_der = -4
'''


# for debugging
def test_print(arr):
    for elem in arr:
        print(elem)


def calculate_difference(x, f, f_der, f_sec_der):
    x0 = [-1, -1, 0, 0, 0, 1]
    f0 = [0, 0, 2, 2, 2, -1]
    # calculate the differences
    # f1, f2, f3, f4, f5 are working correctly
    f1 = [f_der[0] / math.factorial(1), (f[1] - f[0]) / (x[1] - x[0]), f_der[1] / math.factorial(1),
          f_der[1] / math.factorial(1), (f[2] - f[1]) / (x[2] - x[1])]
    f2 = [(f1[1] - f1[0]) / (x[1] - x[0]), (f1[2] - f1[1]) / (x[1] - x[0]),
          f_sec_der[0] / math.factorial(2), (f1[4] - f1[3]) / (x[2] - x[1])]
    f3 = [(f2[1] - f2[0]) / (x[1] - x[0]), (f2[2] - f2[1]) / (x[1] - x[0]),
          (f2[3] - f2[2]) / (x[2] - x[1])]
    f4 = [(f3[1] - f3[0]) / (x[1] - x[0]), (f3[2] - f3[1]) / (x[2] - x[0])]
    f5 = [(f4[1] - f4[0]) / (x[2] - x[0])]

    print("for the input: ")
    print("of x0: ")
    test_print(x0)
    print("of f0: ")
    test_print(f0)
    # build the polynomial
    # print(f0[0], f1[0], f2[0], f3[0], f4[0], f5[0]) # test
    print("the polynomial is: ")
    print("{} + {} * (x - ({})) + {} * (x - ({}))^2 + {} * (x - ({}))^2*(x - ({}))"
          " + {} * (x - ({}))^2 * (x - ({}))^2 + {} * (x - ({}))^2 * (x - ({}))^3"
          .format(f0[0], f1[0], x0[0], f2[0], x0[0], f3[0], x0[0], x0[2],
                  f4[0], x0[1], x0[2], f5[0], x0[1], x0[2]))


def choose_solution_method():
    x = [-1, 0, 1]
    f = [0, 2, -1]
    f_der = [2, 4]
    f_sec_der = [-4]
    calculate_difference(x, f, f_der, f_sec_der)

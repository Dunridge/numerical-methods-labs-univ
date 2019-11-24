# Polinka Maksym, K - 34

import numpy as np

'''
Умова: 
Інтегрування: знайти наближений інтеграл методом Сімпсона 
використовуючи правило Рунге  (точність довільна)
'''


def simpson_method(f):
    a = 1.2
    b = 2
    eps = 0.001
    division_step = 2  # <--- this is 2n: step n = 1, 2*n = 2
    partition_step = (b - a) / division_step
    # print(partition_step) # must be 0.4 --> correct!
    # (aka h variable from your notes) partition_step = 0.4 <--- that's what we increase by
    x_i = [a, a + partition_step, b]
    test_print(x_i)
    print("\n")
    # TODO: at the end see if this influences the result (see the comment below)
    # for some reason the second element is rounded only to the fifth number
    f_i = [round(f(x_i[0]), 6), round(f(x_i[1]), 5), round(f(x_i[2]), 6)]
    test_print(f_i)
    print("\n")
    # test_print(x_i)  # prints correctly although the precision is off
    # test_print(f_i)
    # write the Simpson equation:
    # TODO: see the above TODO task --> this part influences the precision
    # the precison for I is off, too (I_2)
    # TODO: figure out how to create an array for these I elements
    # this corresponds with your notes
    # I_2 has the division_step variable as it's index
    I_2 = round((partition_step / 3) * (f_i[0] + f_i[2] + 4 * f_i[1]), 6)  # initial result
    print("The value of I_2: ", I_2)
    division_step = 4
    partition_step = (b - a) / division_step  # calculates the partition step correctly
    # this array is being printed correctly
    x_i = [a, a + partition_step, a + 2 * partition_step, a + 3 * partition_step, b]
    test_print(x_i)
    print("\n")
    f_i = [round(f(x_i[0]), 6), round(f(x_i[1]), 6), round(f(x_i[2]), 6), round(f(x_i[3]), 6), round(f(x_i[4]), 6)]
    test_print(f_i)
    print("\n")
    # test_print(x_i)
    # test_print(f_i)
    # this works correctly
    I_4 = round((partition_step / 3) * (f_i[0] + f_i[4] + 2 * f_i[2] + 4 * f_i[1] + 4 * f_i[3]), 6)
    print("The value of I_4: ", I_4)
    # TODO: 0.00216700000000003 not 0.002167 because of the error in calculations (see other TODOs)
    # this prints correctly
    dif = np.abs(I_4 - I_2)  # 0.00216700000000003
    # we use the Runge rule:
    if 1 / 15 * dif < eps:  # eps = 0.001
        print("the answer is: ", round(I_4, 3))

    # TODO: think about how to make this iterative
    # this method is working correctly


# for debugging
def test_print(arr):
    for elem in arr:
        print(elem, end=',')


def choose_solution_method():
    # on the [a, b] interval
    f = lambda x: (1 + 2 * (x ** 2) - x ** 3) ** (1 / 2)  # calculates correctly because f(2) = 1
    simpson_method(f)

    return



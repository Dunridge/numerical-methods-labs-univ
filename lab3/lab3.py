# Maksym Polinka K-34
# варіант 7: choose the example yourself

# use www.wolframalpha.com

# don't forget to write the report at the end

'''
Завдання:
1) Знайти максимальне та мінімальне значення методом скалярних добутків
(aka Find the maximum and the minimum eigenvalues for a matrix by using the method
of scalar products)

Для лабораторної реалізував на репозиторії https://github.com/Dunridge/numerical-methods-lab3-univ
за допомогою do while циклу
'''

import numpy as np

A = np.array([[8., 1., -4.],
              [2., -6., 1.],
              [-1., 1., 4.]])


def incorrect_method_number():
    print("Incorrect method number")


def not_yet_implemented():
    print("not yet implemented...")


def implemented_in_another_language():
    print("this method was implemented in C++ because of the do while functionality,"
          " see this repository with C++ code to see more: https://github.com/Dunridge/numerical-methods-lab3-univ )")


def choose_solution_method(chosen_method):
    if chosen_method == 1:
        # enter input
        max_min_eigenvalue(A)
        return
    else:
        incorrect_method_number()


def max_min_eigenvalue(A):  # метод скалярних добутків
    implemented_in_another_language()
    return

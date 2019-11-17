# Maksym Polinka, K - 34

import lab1.lab1 as lr1
import lab2.lab2 as lr2
import lab3.lab3 as lr3
import lab4.lab4 as lr4


def incorrect_method_number():
    print("Incorrect method number")


def not_yet_implemented():
    print("not yet implemented...")


def choose_lab(lab_number):
    if lab_number == 1:
        lr1.choose_solution_method(int(input("please, choose a solution method (1 - dichotomy, 2 -relaxation): ")))
        return
    if lab_number == 2:
        lr2.choose_solution_method(int(input("please, choose a solution method (1 - Jacobi, 2 - Gauss): ")))
        return
    if lab_number == 3:
        lr3.choose_solution_method(1)
        return
    if lab_number == 4:
        lr4.choose_solution_method()
        return
    else:
        incorrect_method_number()


def main():
    choose_lab(int(input("please, enter the lab number: ")))


if __name__ == "__main__":
    main()
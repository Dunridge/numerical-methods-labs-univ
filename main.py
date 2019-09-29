# Maksym Polinka, K - 34

import lab1.lab1 as lr1
import lab2.lab2 as lr2


def incorrect_method_number():
    print("Incorrect method number")


def not_yet_implemented():
    print("not yet implemented...")


def choose_lab(lab_number):
    if lab_number == 1:
        not_yet_implemented()
        return
    if lab_number == 2:
        not_yet_implemented()
        return
    else:
        incorrect_method_number()


def main():
    choose_lab(int(input("Please, enter the lab number: ")))


if __name__ == "__main__":
    main()
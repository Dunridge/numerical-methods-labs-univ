

import numpy as np


f = lambda x: (1 + 2*(x**2) - x**3)**(1/2)
print(f(2))

# def simpson(f, a, b, n):
#     x = np.linspace(a, b, n + 1)
#     w = 2 * np.ones(n + 1);
#     w[0] = 1.0;
#     w[-1] = 1;
#     for i in range(len(w)):
#         if i % 2 == 1:
#             w[i] = 4
#     width = x[1] - x[0]
#     area = 0.333 * width * np.sum(w * f(x))
#     return area
#
#
# f = lambda x: np.sin(x)
# a = 0.0;
# b = np.pi / 4
#
# areaSim = simpson(f, a, b, 10)
# print(areaSim)

# # np.polynomial.hermite.hermval() <-- you could use this class to
#
# import numpy as np
# import matplotlib.pyplot as plt
# import math
#
# def proterm(i, value, x):
#     pro = 1
#     for j in range(i):
#         pro = pro * (value - x[j])
#     return pro
#
# '''
# f_first_der = [2,4]
# f_second_der = [-4]
# '''
# def dividedDiffTable(x, y, f_first_der, f_second_der,  n): #must receive an array of derivatives
#     for i in range(1, n):
#         for j in range(n - i):
#             if(y[j][i - 1] - y[j + 1][i - 1] == 0 or x[j] - x[i + j] == 0):
#                 #use the formula - як це автоматизувати?
#                 if(j==1):
#                     y[j][i] = f_first_der[i]/math.factorial(1)
#                 if(j==2):
#                     y[j][i] = f_second_der[i]/math.factorial(2)
#             else:
#                 y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) /
#                         (x[j] - x[i + j]))
#     return y
#
#
# def applyFormula(value, x, y, n):
#     sum = y[0][0]
#
#     for i in range(1, n):
#         sum = sum + (proterm(i, value, x) * y[0][i])
#     coef = ["" for j in range(n)]
#     var = ["" for j in range(len(x))]
#     for k in range(0, n):
#         coef[k] = str(round(y[0][k], 2))
#         var[k] = str(x[k])
#     pol = coef[0]
#     for k in range(1, n):
#         pol += "+(" + coef[k] + ")"
#         for m in range(k):
#             pol += "*(x-(" + var[m] + "))"
#     print("The polynomial looks like this: ", pol, "\n")
#     print("0.07 p^4 + 0.29 p^3 + 0.6 p^2 + 1.04 p + 0.99")
#     p = np.linspace(x[0] - 5, x[len(x) - 1] + 5, 1000)  # Create a list of evenly-spaced numbers over the range
#     plt.plot(p, 0.11 + (0.22) * (p - (-2)) + (0.22) * (p - (-2)) * (p - (-1)) + (0.15) * (p - (-2)) * (p - (-1)) * (
#             p - (0)) + (0.07) * (p - (-2)) * (p - (-1)) * (p - (0)) * (p - (1)))
#     plt.plot(p, 2 / 3 * p ** 2 + 3 / 4 * p + 1)
#     for k in range(n):
#         plt.plot(x[k], y[k][0], 'bo')
#     plt.show()
#     return sum
#
#
# # def printDiffTable(x, y, f_first_der, f_second_der, n):
# #     for i in range(n):
# #         print("\n", x[i])
# #         for j in range(n - i):
# #             for k in range(2):
# #                 print(round(y[i][j], 4), f_first_der[k], f_second_der[k], "\t",
# #                      end=" ")
# #
# #         print("")
#
#     # Driver Code
#
#
# n = 5
# y = [[0 for i in range(10)]
#      for j in range(10)]
# f = lambda x: 3 ** x
# # this works fine because it doesn't have 0 in the difference:
# x = [-2, -1, 0, 1, 2] # comment out this x and input the ones in your paperbook
# # x = [-1, -1, 0, 0, 0]
# #experimental:
# f_first_der = [2,4]
# f_second_der = [-4]
# # ----------
#
#
# for i in range(n):
#     y[i][0] = f(x[i])
# # y[0][0] = 1
# # y[1][0] = -2
# # y[2][0] = 5
# # y[3][0] = 7
# # y[4][0] = -10
#
# y = dividedDiffTable(x, y, f_first_der, f_second_der, n)
#
# #printDiffTable(x, y, f_first_der, f_second_der, n)
# #print("\n\n")
#
# value = 7
#
# print("\nValue at", value, "is",
#       round(applyFormula(value, x, y, n), 2))
#

from matplotlib import pyplot as plt
from numpy import sum, matrix
from math import pi, cos


n = 100

def normalize(distr):
    distr *= 1/sum(distr)


def iteration(distr, matrix):
    distr = distr * matrix
    normalize(distr)
    return distr

transition_matrix = matrix([[0, 1] + [0] * (n - 2)] + [[0] * i + [0.5, 0, 0.5] + [0] * (n - i - 3) for i in range(n - 2)] + [[0] * (n - 2) + [0.5, 0]])
distr = matrix([1] + [0] * (n - 1))



for i in range(20000):
    distr = iteration(distr, transition_matrix)
    if (i + 1) % 2000 == 0:
        plt.plot(range(n), distr.tolist()[0], 'bo-')
        plt.plot(range(n), [pi / 2 / n * cos(pi * x / 2 / n) for x in range(n)], 'ro-')
        plt.show()




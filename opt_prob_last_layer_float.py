from numpy import matrix, array
from numpy.linalg import cond
from scipy.misc import comb
from math import factorial, sqrt
from fractions import Fraction
#from sympy import Matrix, ones, symbols
#from sympy.solvers.solveset import linsolve
from sys import argv
from matplotlib import pyplot as plt

if len(argv) < 2:
    n = 100
else:
    n = int(argv[1])
if len(argv) < 3:
    k = 2
else:
    k = int(argv[2])
phi = (3 - sqrt(5)) / 2 # Fraction(34/89) #Fraction((3 - sqrt(5)) / 2)
ones = matrix([[1] for _ in range(k)])

def prob(i, j, lam):
    pr = 0
    if j > i:
        c1 = comb(k - i, j - i)
        c2 = 1
        for m in range(k - j + 1):
            pr += c1 * c2 * (lam / n) ** (j - i + 2 * m) * (1 - lam / n) ** (n - j + i - 2 * m)
            c1 *= k - j - m
            c1 //= j - i + m + 1
            c2 *= n - k + i - m
            c2 //= m + 1
    elif j < i:
        c1 = comb(n - k + i, i - j)
        c2 = 1
        for m in range(k - i + 1):
            pr += c1 * c2 * (lam / n) ** (i - j + 2 * m) * (1 - lam / n) ** (n - i + j - 2 * m)
            c1 *= n - k + j - m
            c1 //= i - j + m + 1
            c2 *= k - i - m
            c2 //= m + 1
    else:
        return 0
    return pr

def expectation(lam):
    try:
        p = matrix([[-prob(i, j, lam) for j in range(k)] for i in range(k)])
        for i in range(k):
            p[i, i] = -sum(array(p[i])[0]) + (lam / n) ** (k - i) * (1 - lam / n) ** (n - k + i)
        return (p.getI() * ones)[0, 0]
    except Exception:
        print(p)
        print(p.getI())
        print(ones)
        exit(0)
    # return next(iter(linsolve((p, ones(k, 1)), symbols(', '.join(['x_{}'.format(i) for i in range(k)])))))[0]
    # return (p ** (-1) * ones(k, 1))[0]




def trenary_min(f, a, b):
    c = a + (b - a) * phi
    d = b - (b - a) * phi
    f_c, f_d = f(c), f(d)
    # arguments, values = [a, b, c, d], [f_a, f_b, f_c, f_d]
    while (b - a) > 0.0001:
        #print(float(a), float(b))
        if f_c > f_d:
            a, c, d = c, d, b - (b - c) * phi
            f_c, f_d = f_d, f(d)
            # arguments.append(d)
            # values.append(f_d)
        elif f_c < f_d:
            b, d, c = d, c, a + (b - c) * phi
            f_d, f_c = f_c, f(c)
            # arguments.append(c)
            # values.append(f_c)
        else:
            a, b = c, d
            c, d = a + (b - a) * phi, b - (b - a) * phi
            f_c, f_d = f(c), f(d)
            # arguments.append(c, d)
            # values.append(f_c, f_d)
    # plt.plot(arguments, values, 'bo')
    # plt.show()
    return (a + b) / 2


# print(float(trenar_min(expectation, 1, k)), factorial(k) ** (1/k))

for k in range(2, 11):
    ones = matrix([[1] for _ in range(k)])
    # print(k)
    # lambdas = [1 + 0.2 * i for i in range(5 * (k - 1) + 1)] #[1 + 0.1 * i for i in range(190)]
    # plt.plot(lambdas, [float(expectation(lam)) for lam in lambdas], 'bo')
    # plt.show()
    print('\\hline\n{} & {:.3f} & {:.3f} \\tabularnewline'.format(k, float(trenary_min(expectation, 1, k)), factorial(k) ** (1 / k)))


from scipy.misc import comb
from math import factorial
from fractions import Fraction
from sympy import Matrix, ones, symbols
from sympy.solvers.solveset import linsolve
from sys import argv


n = int(argv[1])
k = int(argv[2])
phi = Fraction(34/89) #Fraction((3 - sqrt(5)) / 2)

def prob(i, j, lam):
    pr = 0
    if j > i:
        c1 = Fraction(comb(k - i, j - i))
        c2 = 1
        for m in range(k - j + 1):
            pr += c1 * c2 * (Fraction(lam, n)) ** (j - i + 2 * m) * (Fraction(n - lam, n)) ** (n - j + i - 2 * m)
            c1 *= k - j - m
            c1 //= j - i + m + 1
            c2 *= n - k + i - m
            c2 //= m + 1
    elif j < i:
        c1 = Fraction(comb(n - k + i, i - j))
        c2 = 1
        for m in range(k - i + 1):
            pr += c1 * c2 * (Fraction(lam, n)) ** (i - j + 2 * m) * (Fraction(n - lam, n)) ** (n - i + j - 2 * m)
            c1 *= n - k + j - m
            c1 //= i - j + m + 1
            c2 *= k - i - m
            c2 //= m + 1
    else:
        return 0
    return pr

def expectation(lam):
    p = Matrix([[-prob(i, j, lam) for j in range(k)] for i in range(k)])
    for i in range(k):
        p[(k + 1) * i] = -sum(p.row(i)) + (Fraction(lam, n)) ** (k - i) * (Fraction(n - lam, n)) ** (n - k + i)
    return next(iter(linsolve((p, ones(k, 1)), symbols(', '.join(['x_{}'.format(i) for i in range(k)])))))[0]
    # return (p ** (-1) * ones(k, 1))[0]




def trenar_min(f, a, b):
    c = a + (b - a) * phi
    d = b - (b - a) * phi
    f_a, f_b, f_c, f_d = f(a), f(b), f(c), f(d)
    while (b - a) > 0.0001:
        #print(float(a), float(b))
        if f_c > f_d:
            a, c, d = c, d, b - (b - c) * phi
            f_a, f_c, f_d = f_c, f_d, f(d)
        elif f_c < f_d:
            b, d, c = d, c, a + (b - c) * phi
            f_b, f_d, f_c = f_d, f_c, f(c)
        else:
            a, b = c, d
            c, d = a + (b - a) * phi, b - (b - a) * phi
            f_a, f_b = f_c, f_d
            f_c, f_d = f(c), f(d)
    return (a + b) / 2


print(float(trenar_min(expectation, 1, k)), factorial(k) ** (1/k))
# for k in range(2, 11):
#     print(k)
#     # lambdas = [Fraction(5 + i, 5) for i in range(45)] #[1 + 0.1 * i for i in range(190)]
#     # plt.plot(lambdas, [float(expectation(lam)) for lam in lambdas], 'bo')
#     # plt.show()
#     print(float(trenar_min(expectation, 1, k)), ph ** (1/k))
#     ph *= (k + 1)


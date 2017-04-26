from numpy import matrix, sum
from numpy.linalg import det
from scipy.misc import comb
from matplotlib import pyplot as plt
from math import sqrt
from fractions import Fraction
from numpy.linalg.linalg import LinAlgError

n = 1000
k = 2
phi = Fraction((3 - sqrt(5)) / 2)

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
    try:
        p = matrix([[-prob(i, j, lam) for j in range(k)] for i in range(k)])
        for i in range(k):
            p[i, i] = -sum(p[i].tolist()[0]) + (Fraction(lam, n)) ** (k - i) * (Fraction(n - lam, n)) ** (n - k + i)
        for i in range(k):
            for j in range(k):
                p[i, j] = float(p[i, j])
        print(p)
        return (p.getI()
                * matrix([[1] for i in range(k)])).tolist()[0][0]
    except LinAlgError:
        for i in range(k):
            for j in range(k):
                print(p[i, j], end='\t')
            print()
        print(det(p))
        exit(0)



def trenar_min(f, a, b):
    c = a + (b - a) * phi
    d = b - (b - a) * phi
    f_a, f_b, f_c, f_d = f(a), f(b), f(c), f(d)
    while (b - a) > 0.0001:
        print(float(a), float(b))
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


ph = 120

for k in range(8, 11):
    print(k)
    lambdas = [Fraction(10 + i, 10) for i in range(190)]
    plt.plot(lambdas, [float(expectation(lam)) for lam in lambdas], 'bo')
    plt.show()
    #print(float(trenar_min(expectation, 1, 20)), ph ** (1/k))
    ph *= (k + 1)


from numpy import matrix, sum
from numpy.linalg import det
from scipy.misc import comb
from matplotlib import pyplot as plt
from math import sqrt

n = 1000
k = 2
phi = (3 - sqrt(5)) / 2

def prob(i, j, lam):
    pr = 0
    if j > i:
        c1 = comb(k - i, j - i)
        c2 = 1
        for m in range(k - j + 1):
            pr += c1 * c2 * (lam / n) ** (j - i + 2 * m) * (1 - lam/n) ** (n - j + i - 2 * m)
            c1 *= k - j - m
            c1 //= j - i + m + 1
            c2 *= n - k + i - m
            c2 //= m + 1
    elif j < i:
        c1 = comb(n - k + i, i - j)
        c2 = 1
        for m in range(k - i + 1):
            pr += c1 * c2 * (lam / n) ** (i - j + 2 * m) * (1 - lam/n) ** (n - i + j - 2 * m)
            c1 *= n - k + j - m
            c1 //= i - j + m + 1
            c2 *= k - i - m
            c2 //= m + 1
    else:
        return 0
    return pr

def expectation(lam):
    p = matrix([[-prob(i, j, lam) for j in range(k)] for i in range(k)])
    for i in range(k):
        p[i,i] = -sum(p[i].tolist()[0]) + (lam/n) ** (k - i) * (1 - lam/n) ** (n - k + i)
    print(p)
    print(p.getI())
    print(p * p.getI())
    return (p.getI() * matrix([[1] for i in range(k)])).tolist()[0][0]

def trenar_min(f, a, b):
    c = a + (b - a) * phi
    d = b - (b - a) * phi
    f_a, f_b, f_c, f_d = f(a), f(b), f(c), f(d)
    while (b - a) > 0.0001:
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


ph = 2

k = 6
expectation(20)
exit(0)
for k in range(2, 11):
    lambdas = [1 + 0.1 * i for i in range(190)]
    plt.plot(lambdas, [expectation(lam) for lam in lambdas], 'bo')
    plt.show()
    print(trenar_min(expectation, 1, 20), ph ** (1/k))
    ph *= (k + 1)

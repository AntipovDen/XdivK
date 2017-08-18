from scipy.misc import comb, factorial
from numpy import matrix
from numpy.linalg import det, eig
from matplotlib import pyplot as plt
from math import sqrt

for k in range(2, 20):
    n = 100000
    lam = factorial(k) ** (1/k)


    def prob(i, j):
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
        return pr


    probs_to_k = matrix([[prob(i, k)] for i in range(k)])
    x_stable = matrix([(1 - prob(i, k)) * comb(n, k - i) / sum([(1 - prob(i, k)) *comb(n, k - i)  for i in range(k)]) for i in range(k)])

    def p_end(x):
        return float(x * probs_to_k)


    p_end_stable = float(p_end(x_stable))

    x = matrix([1] + [0 for _ in range(k - 1)])
    p = [[prob(i, j) for j in range(k)] for i in range(k)]
    for i in range(k):
        p[i][i] = 1 - sum(p[i]) - prob(i, k)

    for i in range(k):
        for j in range(k):
            p[i][j] /= 1 - prob(i, k)
    p = matrix(p)
    print(1 - sum([min([p[i, j] for i in range(k - 1)]) for j in range(k - 1)]))
exit(0)

res = []
for steps in range(100):
    res.append(x - x_stable)
    x = x * p


for i in range(99):
    print(i, p_end(res[i]) / p_end(res[i + 1]), 1/(eig(p.transpose())[0][1]))
    # print(res[i])

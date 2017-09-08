from scipy.misc import comb, factorial
from matplotlib import pyplot as plt


n = 100
k = 10
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

# returns True if and only if distr1 is dominated by distr2
def check_dominataion(distr1, distr2):
    s1, s2 = 0, 0
    for i in range(len(distr1)):
        s1 += distr1[i]
        s2 += distr2[i]
        if s1 < s2:
            return False
    return True

for i in range(1, k):
    x = range(k + 1)
    y = [prob(i, j) for j in x]
    y_prev = [prob(i - 1, j) for j in x]
    y[i] = 1 - sum(y)
    y_prev[i] = 1 - sum(y_prev)
    print(i, check_dominataion(y_prev, y))

    for j in range(1, k + 1):
        y[j] += y[j - 1]
        y_prev[j] += y_prev[j - 1]

    plt.plot(x, y, 'bo')
    plt.plot(x, y, 'b-')
    plt.plot(x, y_prev, 'ro')
    plt.plot(x, y_prev, 'r-')
    plt.show()

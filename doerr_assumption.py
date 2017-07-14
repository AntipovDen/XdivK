from numpy import matrix, array
from numpy.linalg import cond
from scipy.misc import comb
from math import factorial, sqrt, e
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
if len(argv) < 4:
    lam = factorial(k) ** (1 / k)
phi = (3 - sqrt(5)) / 2 # Fraction(34/89) #Fraction((3 - sqrt(5)) / 2)
ones = matrix([[1] for _ in range(k)])

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

def prob_simplified(i, j):
    if j > i:
        return comb(k - i, j - i) * (lam / n) ** (j - i) * (1 - lam / n) ** (n - j + i)
    elif j < i:
        return comb(n - k + i, i - j) * (lam / n) ** (i - j) * (1 - lam / n) ** (n - i + j)
    return 0

def expectation_original(lamb):
    global lam
    lam = lamb
    try:
        p = [[-prob(i, j) for j in range(k)] for i in range(k)]
        for i in range(k):
            p[i][i] = -sum(p[i]) + (lam / n) ** (k - i) * (1 - lam / n) ** (n - k + i)
        return (matrix(p).getI() * ones)[0, 0]
    except Exception:
        print(p)
        print(matrix(p).getI())
        print(ones)
        exit(0)


def expectation_doerr():
    try:
        p = [[-prob(i, j) for j in range(k)] for i in range(k)]
        for i in range(k):
            for j in range(1, i):
                p[i][0] += p[i][j]
                p[i][j] = 0
        for i in range(k):
            p[i][i] = -sum(p[i]) + (lam / n) ** (k - i) * (1 - lam / n) ** (n - k + i)
        return (matrix(p).getI() * ones)[0, 0]
    except Exception:
        print(p)
        print(matrix(p).getI())
        print(ones)
        exit(0)

def expectation_my_assumption(lam):
    return n ** k * e ** lam / sum([lam ** i * (factorial(k) // factorial(i)) for i in range(1, k + 1)])

def expectation_simplified_probabilities(lamb):
    global lam
    lam = lamb
    try:
        p = [[-prob_simplified(i, j) for j in range(k)] for i in range(k)]
        for i in range(k):
            p[i][i] = -sum(p[i]) + (lam / n) ** (k - i) * (1 - lam / n) ** (n - k + i)
        return (matrix(p).getI() * ones)[0, 0]
    except Exception:
        print(p)
        print(matrix(p).getI())
        print(ones)
        exit(0)

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
    break #TODO: delete it!!!!!!!
    ones = matrix([[1] for _ in range(k)])
    print(k)
    lambdas = [1 + 0.2 * i for i in range(5 * (k - 1) + 1)] #[1 + 0.1 * i for i in range(190)]
    plt.plot(lambdas, [float(expectation_original(lam)) for lam in lambdas], 'bo')
    plt.plot(lambdas, [float(expectation_simplified_probabilities(lam)) for lam in lambdas], 'ro')
    plt.show()
    # print('\\hline\n{} & {:.3f} & {:.3f} \\tabularnewline'.format(k, float(trenary_min(expectation, 1, k)), factorial(k) ** (1 / k)))
    # print('k = {}'.format(k))
    # print(expectation_original())
    # print(expectation_doerr())

# trying to find the distribution of being in every state after n steps


k = 4
n = 50
lam = 1
x = matrix([1] + [0 for _ in range(k - 1)])
print(x)
p = [[prob(i, j) for j in range(k)] for i in range(k)]
for i in range(k):
    p[i][i] = 1 - sum(p[i]) - prob(i, k)

for i in range(k):
    for j in range(k):
        p[i][j] /= 1 - prob(i, k)
p = matrix(p)
print(p)
for _ in range(10000000):
    # print(x, sum([x[0, _] for _ in range(k)]))
    x = x * p
print(x, sum([x[0, _] for _ in range(k)]))
#[[  8.91552912e-01   9.79728475e-02   9.58430029e-03   8.24455939e-04  6.13956550e-05   3.87762028e-06   2.01959356e-07   8.32818763e-09   2.54911779e-10   5.11979754e-12]] 0.999999999349
#[[  8.86252798e-01   9.73904174e-02   9.52732344e-03   8.19554704e-04  6.10306694e-05   3.85456856e-06   2.00758746e-07   8.27867813e-09   2.53396377e-10   5.08936131e-12]] 0.994055188222


#[[  9.48347520e-01   4.93930857e-02   2.03681895e-03   6.23433546e-05  1.25210361e-06]] 0.999841020031
#[[  9.42677753e-01   4.90977855e-02   2.02464167e-03   6.19706302e-05  1.24461781e-06]] 0.993863395622

#[[  9.16892866e-01   7.80331987e-02   4.87635029e-03   1.97585442e-04]] 1.0
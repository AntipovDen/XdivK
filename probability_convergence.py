from scipy.special import comb, factorial
from numpy import matrix
from numpy.linalg import det, eig
from matplotlib import pyplot as plt
from math import sqrt, e, log

def second_max(array):
    max_1 = 0
    max_2 = 0
    for a in array:
        if a >= max_1:
            max_2 = max_1
            max_1 = a
        elif a >= max_2:
            max_2 = a
    return max_2

for k in range(2, 20):
    n = 1000
    alpha = 1# factorial(k) ** (1 / k)


    def prob(i, j):
        pr = 0
        if j > i:
            c1 = comb(k - i, j - i)
            c2 = 1
            for m in range(k - j + 1):
                pr += c1 * c2 * (alpha / n) ** (j - i + 2 * m) * (1 - alpha / n) ** (n - j + i - 2 * m)
                c1 *= k - j - m
                c1 //= j - i + m + 1
                c2 *= n - k + i - m
                c2 //= m + 1
        elif j < i:
            c1 = comb(n - k + i, i - j)
            c2 = 1
            for m in range(k - i + 1):
                pr += c1 * c2 * (alpha / n) ** (i - j + 2 * m) * (1 - alpha / n) ** (n - i + j - 2 * m)
                c1 *= n - k + j - m
                c1 //= i - j + m + 1
                c2 *= k - i - m
                c2 //= m + 1
        return pr


    # init = [prob(-1, i) for i in range(k)]
    # s = sum(init)
    # for i in range(k):
    #     init[i] /= s
    # uniform = [comb(n, k - i) for i in range(k)]
    # s = sum(uniform)
    # for i in range(k):
    #     uniform[i] /= s
    #
    # epsilon = [(init[i] - uniform[i]) / comb(n, k - i) for i in range(k)]
    # print(epsilon)
    # plt.plot(range(k), epsilon, 'bo-')
    # plt.show()
    p = [[prob(i, j) for j in range(k)] for i in range(k)]
    for i in range(k):
        p[i][i] = 1 - sum(p[i]) - prob(i, k)

    eigenvalues, eigenvectors = eig(matrix(p).transpose())

    pi_u = [comb(n, k - i) for i in range(k)]
    s = sum(pi_u)
    for i in range(k):
        pi_u[i] /= s

    eigenvectors = [vector.tolist()[0] for vector in eigenvectors.transpose()]

    # eigenvector = [eigenvectors[0][i] / comb(n ,k - i) for i in range(k)]
    # s = sum(eigenvector)
    # for i in range(k):
    #     eigenvector[i] *= k / s

    # print(eigenvector)

    coordinates = [sum(pi_u[j] * eigenvectors[i][j] for j in range(k)) for i in range(k)]
    print([sum(eigenvectors[i][j] * coordinates[j] for j in range(k)) for i in range(k)])
    print(pi_u)
    # for i in range(k):
    #     print(sum([pi_u[j] * eigenvectors[i][j] for j in range(k)]) / sum([abs(eigenvectors[i][j]) for j in range(k)]), end=' ')
    print()

    #
    #
    # print(k, min(eigenvalues), second_max(eigenvalues))



# plt.plot(range(2, 59), [res[i] / res[i + 1] for i in range(57)], 'bo-')
# plt.plot(range(2, 59), [res[0] / res[1] + 1/(2 + e - 1) - 1/(i + e - 1) for i in range(2, 59)], 'ro-')
# plt.show()
# exit(0)
# plt.semilogy(range(2, 40), res, 'bo-')
# plt.semilogy(range(2, 40), [1/e * (e/2) ** (-k + 2) for k in range(2, 40)], 'ro-')
# plt.show()



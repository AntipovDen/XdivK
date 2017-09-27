from scipy.misc import comb, factorial
from matplotlib import pyplot as plt
from math import ceil, e, sqrt, pi, log
from sympy import zeta, polylog, gamma

n = 10000
k = 15
alpha = k ** (1/k)


def compare_functions(functions, comparation_range, xlabel='', ylabel='', labels=[]):
    values = [[f(i) for i in comparation_range] for f in functions]
    styles = ['o', 'v', '^', '<', '>', '.', ',', '1', '2', '3', '4', '8', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd', '|', '_', 'P', 'X']
    colors = ['r', 'g', 'b', 'y']

    for i in range(len(values)):
        if len(labels) < len(functions):
            plt.plot(comparation_range, values[i], colors[i % 4] + styles[i] + '-', label=functions[i].__name__.replace('_', ' '))
        else:
            plt.plot(comparation_range, values[i], colors[i % 4] + styles[i] + '-', label=labels[i])
        print(values[i][:10])
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    # plt.legend(loc=4)
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2,
           ncol=1, mode="expand", borderaxespad=0.)
    plt.show()


def normalization_constant_opt_mut_rate(k):
    alpha = factorial(k) ** (1/k)
    return sum(comb(n, k - i) * (1 - (alpha/n) ** (k - i) * (1 - alpha/n) ** (n - k + i)) for i in range(k))


def normalization_constant_fea(k):
    beta = 2
    norm_const = normalization_constant_heavy_tailed_distribution(beta)
    p_to_k = [sum(alpha ** (k - i - beta) * (1 - alpha / n) ** (n - k + i) for alpha in range(1, n // 2)) / n ** (k - i) / norm_const for i in range(k)]
    return sum(comb(n, k - i) * (1 - p_to_k[i]) for i in range(k))


def normalization_constant_approx(k):
    return comb(n, k)


def p_end_numerator_opt_rate_exact(k):
    alpha = factorial(k) ** (1 / k)
    return sum(comb(n, k - i) * (1 - (alpha/n) ** (k - i) * (1 - alpha/n) ** (n - k + i)) * (alpha/n) ** (k - i) * (1 - alpha/n) ** (n - k + i) for i in range(k))


def p_end_numerator_opt_rate_approx(k):
    return e ** (-alpha) * sum(alpha ** i / factorial(i) for i in range(1, k + 1))


def normalization_constant_heavy_tailed_distribution(beta):
    return sum(alpha ** (-beta) for alpha in range(1, n // 2))


def upper_bound_on_zeta(beta):
    return beta / (beta - 1)


def upper_bound_on_normalization_constant_for_htm(beta):
    return (beta - (n // 2) ** (1 - beta))/ (beta - 1)


def partial_polylog(beta, i):
    return sum(e ** (-alpha) * alpha ** (k - i - beta) for alpha in range(1, n // 2))


def p_end_numerator_fea_exact(k, beta):
    norm_const = normalization_constant_heavy_tailed_distribution(beta)
    p_to_k = [sum(alpha ** (k - i - beta) * (1 - alpha/n) ** (n - k + i) for alpha in range(1, n // 2)) / n ** (k - i) / norm_const for i in range(k)]
    return sum(p_to_k[i] * (1 - p_to_k[i]) * comb(n, k - i) for i in range(k))


def p_end_numerator_fea_approx(k, beta):
    return sum(polylog(beta - i, 1/e) / factorial(i) for i in range(1, k + 1)) / normalization_constant_heavy_tailed_distribution(beta)


# 1 < beta <= 2
def worst_constant_fea_1_2(k):
    return (-log(1 - 1 / e) + 1 / (2 * (e - 1)) + (1 - 1 / sqrt(2 * pi)) * (1 / 2 - 1 / k)) / upper_bound_on_normalization_constant_for_htm(2)


# 2 < beta <= 3
def worst_constant_fea_2_3(k):
    if k == 2:
        return 1 / e + 1 / (4 * e ** 2) - 0.5 * log(1 - 1/e)
    return 1 / e + 1 / (4 * e ** 2) - 0.5 * log(1 - 1/e) + 1 / (6 * (e - 1)) + (1 - 1 / sqrt(2 * pi)) * 0.5 * (1 / 6 - 1 / (k * (k - 1))) / upper_bound_on_normalization_constant_for_htm(3)


def best_constant_opt_mut_rate(k):
    alpha = factorial(k) ** (1/k)
    return e ** (-alpha) * sum([alpha ** i / factorial(i) for i in range(1, k + 1)])


def exact_runtime_opt_mut_rate(n_, k_):
    global n
    n = n_
    return normalization_constant_opt_mut_rate(k_) / p_end_numerator_opt_rate_exact(k_)


#for beta = 2
def exact_runtime_fea(n_, k_):
    global n
    n = n_
    return normalization_constant_fea(k_) / p_end_numerator_fea_exact(k_, 2)


def lower_bound_constant_opt_mut_rate(k):
    return (1 - e ** (-factorial(k) ** (1/k))) ** (-1)

def upper_bound_constant_fea(k, beta):
    return beta / (beta - 1) / (-log(1 - 1/e) + 1 / (2 * (e - 1)) + (1 - 1/sqrt(2 * pi)) * (1/2 - 1/k))


comapration_range = range(2, 21)
# this is for polylogarithm and gamma function [0.5 * i for i in range(200)]
# this is for k: range(2, 20)
# this is for beta: [1 + 0.01 * i for i in range(1, 200)]

compare_functions([lambda k: upper_bound_constant_fea(k, 2),
                   lambda k: exact_runtime_fea(1000, k) / comb(1000, k),
                   lambda k: exact_runtime_opt_mut_rate(1000, k) / comb(1000, k),
                   lambda k: lower_bound_constant_opt_mut_rate(k)], comapration_range, xlabel='$k$', labels=['Upper bound for Fast EA', 'Fast EA', 'Optimal Rate', 'Lower bound for Optimal Rate'])


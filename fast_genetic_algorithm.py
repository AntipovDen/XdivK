from math import factorial
from random import random
from sys import argv

from scipy.stats import rv_discrete
from numpy import arange, mean
# from matplotlib import pyplot as plt

RUNS = 100
run_number = 0
logfile = None

def get_statistics_fga(n, k, beta):
    global run_number
    probabilities = 1 / arange(1, (n + 1) // 2) ** beta
    probabilities /= probabilities.sum()
    dist = rv_discrete(values=(range(1, (n + 1) // 2), probabilities)).rvs
    run_number = 1
    return mean([run(n, k, dist) for _ in range(RUNS)])


def get_statistics_opo(n, k):
    global run_number
    opt_prob = factorial(k) ** (1/k)
    run_number = 1
    return mean([run(n, k, lambda: opt_prob) for _ in range(RUNS)])


def run(n, k, dist): #seems like it works
    global logfile, run_number
    iterations = 0
    sum_x = n - k
    logfile.write('run {}\n'.format(run_number))
    logfile.flush()
    run_number += 1
    while sum_x < n:
        iterations += 1
        logfile.write('{}\n'.format(iterations))
        logfile.flush()
        alpha = dist()
        mutation = 0
        for i in range(n - sum_x): # flipping zeros
            if random() < alpha / n:
                mutation += 1
        for i in range(sum_x):
            if random() < alpha / n: # flipping ones
                mutation -= 1
        if sum_x + mutation >= n - k:
            sum_x += mutation
    return iterations

n = int(argv[1])

for beta in 1, 1.1, 1.5, 2, 3:
    with open('fga_{}_{:1.1f}.out'.format(n, beta), 'w') as f:
        logfile = open('fga_{}_{:1.1f}.log'.format(n, beta), 'w')
        for k in 2, 3, 5, 10:
            logfile.write('k = {}\n'.format(k))
            logfile.flush()
            f.write(str(get_statistics_fga(n, k, beta)))
            f.write(' ')
        logfile.close()

with open('opo_{}.out'.format(n), 'w') as f:
    logfile = open('opo_{}.log'.format(n), 'w')
    for k in 2, 3, 5, 10:
        logfile.write('k = {}\n'.format(k))
        logfile.flush()
        f.write((get_statistics_opo(n, k)))
        f.write(' ')
        f.flush()
    logfile.close()



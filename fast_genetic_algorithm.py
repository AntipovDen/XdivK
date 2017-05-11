from scipy.stats import rv_discrete
from numpy import arange

def power_law(beta, n):
    x = arange(1, n + 1)
    probabilities = 1 / x ** beta
    probabilities /= probabilities.sum()
    return rv_discrete(values=(range(1, n + 1), probabilities))

print(power_law(1.5, 100).rvs(size = 30))
n = 100
k = 10



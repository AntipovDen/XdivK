from numpy import matrix
from matplotlib import pyplot as plt
from random import randint


# actually the argument is (n + 1) / 2
def run(n):
    x = 0
    iters = 0
    while abs(x) < n:
        iters += 1
        x += -1 + 2 * randint(0, 1)
    return iters

runs = 1000

ns = range(11, 112, 10)
runtimes = []

for n in ns:
    runtimes.append(sum([run((n + 1) // 2) for _ in range(runs)]) / runs)

plt.plot(ns, runtimes, 'bo-')
plt.plot(ns, [((n + 1) // 2) ** 2 for n in ns], 'ro-')
plt.show()


from numpy import matrix
from scipy.misc import comb


n = 10
k = 4

individuals = []

def next(bit_vector):
    res = bit_vector.copy()
    ones = sum(bit_vector)
    i = 0
    while bit_vector[i] == 0:
        i += 1
    if i == len(bit_vector) - ones:
        return None
    j = i
    while bit_vector[j] == 1:
        j += 1
    res[j] = 1
    res[0:j] = [0] * j
    res[0:(j - i - 1)] = [1] * (j - i - 1)
    return res


for i in range(k):
    individual = [1] * (n - k + i) + [0] * (k - i)
    while individual is not None:
        individuals.append(individual)
        individual = next(individual)

def d(i, j):
    return sum([1 for _ in range(n) if individuals[i][_] != individuals[j][_]])

def level(i):
    return n - sum(individuals[i])

nn = n ** n
P_array = [[(n - 1) ** d(i, j) / nn * (i != j)for i in range(len(individuals))] for j in range(len(individuals))]
for i in range(len(P_array)):
    P_array[i][i] = 1 - sum(P_array[i]) - (n - 1) ** level(i) / nn

P = matrix(P_array)

def normalize(vector):
    s = sum(vector)
    for i in range(len(vector)):
        vector[i] /= s
    return vector


pi = [1/len(individuals)] * len(individuals)
for t in range(100):
    pi = normalize((pi * P).tolist()[0])

print(pi)
print([pi_i * len(individuals) for pi_i in pi])



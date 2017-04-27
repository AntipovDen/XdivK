from math import ceil, floor, sqrt

x = (3 - sqrt(5)) / 2
distance = [0] * 1001

for m in range(1, 1001):
    distance[m] = (min(x - floor(x * m) / m, ceil(m * x) / m - x), m)

distance = distance[1:]
distance.sort()

for d in distance:
    print(d)
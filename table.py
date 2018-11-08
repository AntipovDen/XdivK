from math import e, factorial

def c_bitwise(gamma, k):
    return e ** gamma / sum([gamma ** i / factorial(i) for i in range(1, k + 1)])


def harmonic_number(beta, k):
    return sum([i ** (-beta) for i in range(1, k + 1)])


print('{:.3f} & {:.3f} & {:.3f}'.format(c_bitwise(1, 2), c_bitwise(1, 5), c_bitwise(1, 10)))

print('{:.3f} & {:.3f} & {:.3f}'.format(c_bitwise(2/e, 2), c_bitwise(5/e, 5), c_bitwise(10/e, 10)))

n = 10 ** 6

for beta in 1.5, 2:
    for k in 2, 5, 10:
        print('${:.3f}$'.format(harmonic_number(beta, n//2) / harmonic_number(beta, k)), end='')
        if k != 10:
            print(' & ', end='')
        else:
            print()


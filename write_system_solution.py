# this script has an input system of n - 1 linear equations with n variables. All the eqations has a following form:
# sum a_i^j x_i = 0
# we want to receive n -1 equations that look like x_i = c_i x_{i + 1}

from scipy.misc import comb, factorial

def mul_equation(eq, exp):
    return ['{} \\cdot {}'.format(s, exp) for s in eq]

def substract_equations(eq1, eq2):
    return ['({} - {})'.format(eq1[i], eq2[i]) for i in range(len(eq1))]

k = 4

def prob(i, j):
    if j > i:
        s = ''
        if j != k:
            s = str(int(comb(k - i, j - i)))
        return s + '\\left( \\frac{{\\lambda}}{{n}}\\right)^{{{}}} e^{{-\\lambda}}'.format(j - i)
    else:
        s = ''
        if (i - j) < 2:
            s = ''.join(['(n - {})'.format(_) for _ in range(k - i, k - j)])
        else:
            s = '\\frac{' + ''.join(['(n - {})'.format(_) for _ in range(k - i, k - j)]) + '}}{{{}}}'.format(int(factorial(i - j)))
        return  s + '\\left(\\frac{{\\lambda}}{{n}}\\right)^{{{}}} e^{{-\\lambda}}'.format(i - j)

def system_cell(i, j):
    if i == j:
        return '(-\\frac{{{}}}{{1 - {}}})'.format(' + '.join([prob(i, m) for m in range(k) if m != i]), prob(i, k))
    else:
        return '\\frac{{{}}}{{1 - {}}}'.format(prob(j, i), prob(j, k))

original_system = [[system_cell(i, j) for j in range(k)] for i in range(k)]

# n = k - 1
# original_system = [['' for _ in range(n + 1)] for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             original_system[i][j] = '\\left(-1 + \\frac{{p_{}^{}}}{{1 - p_{}^{}}}\\right)'.format(j, i, j, n + 1)
#         else:
#             original_system[i][j] = '\\frac{{p_{}^{}}}{{1 - p_{}^{}}}'.format(j, i, j, n + 1)
#         original_system[i][-1] = '\\left(-\\frac{{p_{}^{}}}{{1 - p_{}^{}}}\\right)'.format(n - 1, i, n - 1, n)


# with open('matrix.in', 'r') as f:
#     for line in f.readlines():
#         system.append([s.strip() for s in line.split('&')])

answer = []
for i in range(0, k - 1):
    system = [line[0:i] + line[i + 2:k] + line[i:i + 2] for line in original_system]
    tmp = system[i]
    system[i:k - 2] = system[i + 2:k]
    system[k - 2] = tmp
    system.pop()
    for j in range(0, k):
        for i in range(j + 1, k - 1):
            system[i][j + 1:] = substract_equations(mul_equation(system[i][j + 1:], system[j][j]), mul_equation(system[j][j + 1:], system[i][j]))
            system[i][j] = '0'
    answer.append((system[-1][-2], system[-1][-1]))

# for exact but complicated solution

# for j in reversed(range(0, n)):
#     for i in range(0, j):
#         system[i][i:j] = mul_equation(system[i][i:j], system[j][j])
#         system[i][-1] = '({} \\cdot {} - {} \\cdot {})'.format(system[i][-1], system[j][j], system[j][-1], system[i][j])
#         system[i][j] = '0'


with open('solution.tex', 'w') as f:
    f.write('\\documentclass[russian]{article}\n')
    f.write('\\usepackage[T2A,T1]{fontenc}\n')
    f.write('\\usepackage[utf8]{inputenc}\n')
    f.write('\\usepackage[a4paper]{geometry}\n')
    f.write('\\geometry{verbose,tmargin=1cm,bmargin=0cm,lmargin=0cm,rmargin=0cm}\n')
    f.write('\\usepackage{amsmath}\n')
    f.write('\\usepackage{amsfonts}\n')
    f.write('\n')
    f.write('\\makeatletter\n')
    f.write('\n')
    f.write('\\DeclareRobustCommand{\\cyrtext}{%\n')
    f.write('  \\fontencoding{T2A}\\selectfont\\def\\encodingdefault{T2A}}\n')
    f.write('\\DeclareRobustCommand{\\textcyr}[1]{\\leavevmode{\\cyrtext #1}}\n')
    f.write('\\AtBeginDocument{\\DeclareFontEncoding{T2A}{}{}}\n')
    f.write('\n')
    f.write('\\newcommand{\\dx}{\\text{d}x}\n')
    f.write('\\makeatother\n')
    f.write('\n')
    f.write('\\usepackage[russian]{babel}\n')
    f.write('\\begin{document}\n')

    f.write('\\begin{tabular}{ccc}')
    for i in range(k - 1):
        f.write('$x_{} =$ &\n'.format(i))
        f.write('\\begin{tabular}{p{15cm}}\n')
        f.write('${}$\n\\tabularnewline\n\\hline\n${}$\n\\tabularnewline\n'.format(answer[i][1], answer[i][0]))
        f.write('\\end{tabular} &\n')
        f.write('$x_{}$\n'.format(i + 1))
        f.write('\\tabularnewline\n')
        f.write('\\tabularnewline\n')
    f.write('\\end{tabular}')


    f.write('\\end{document}\n')
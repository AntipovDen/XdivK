def mul_equation(eq, exp):
    return ['{} \\cdot {}'.format(s, exp) for s in eq]

def substract_equations(eq1, eq2):
    return ['({} - {})'.format(eq1[i], eq2[i]) for i in range(len(eq1))]

k = 4
def prob(i, j):
    s = ''
    if i > j:
        for m in range(k - j + 1):
            pass
    else:
        for m in range(k - i + 1):
            pass
    return s


n = k - 1
system = [['' for _ in range(n + 1)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            system[i][j] = '-1 + \\frac{{p_{}^{}}}{{1 - p_{}^{}}}'.format(j, i, j, n + 1)
        else:
            system[i][j] = '\\frac{{p_{}^{}}}{{1 - p_{}^{}}}'.format(j, i, j, n + 1)
    system[i][-1] = '-\\frac{{p_{}^{}}}{{1 - p_{}^{}}}'.format(n - 1, i, n - 1, n)


# with open('matrix.in', 'r') as f:
#     for line in f.readlines():
#         system.append([s.strip() for s in line.split('&')])

for j in range(0, n):
    for i in range(j + 1, n):
        system[i][j + 1:] = substract_equations(mul_equation(system[i][j + 1:], system[j][j]), mul_equation(system[j][j + 1:], system[i][j]))
        system[i][j] = '0'


for j in reversed(range(0, n)):
    for i in range(0, j):
        system[i][i:j] = mul_equation(system[i][i:j], system[j][j])
        system[i][-1] = '({} \\cdot {} - {} \\cdot {})'.format(system[i][-1], system[j][j], system[j][-1], system[i][j])
        system[i][j] = '0'


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
    for i in range(n):
        f.write('$x_{} =$ &\n'.format(n))
        f.write('\\begin{tabular}{p{15cm}}\n')
        f.write('${}$\n\\tabularnewline\n\\hline\n${}$\n\\tabularnewline\n'.format(system[i][i], system[i][-1]))
        f.write('\\end{tabular} &\n')
        f.write('$x_{}$\n'.format(i))
        f.write('\\tabularnewline\n')
        f.write('\\tabularnewline\n')
    f.write('\\end{tabular}')


    f.write('\\end{document}\n')
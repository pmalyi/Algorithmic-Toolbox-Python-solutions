import math


def calc(a, b, op):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
def MinAndMax(Operators, m, M, paren_min, paren_max, i, j):
    min_v = math.inf
    max_v = -math.inf
    paren_min_v = ""
    paren_max_v = ""
    for k in range(i, j):
        a = calc(M[i][k], M[k + 1][j], Operators[k])
        if a < min_v:
            min_v = a
            paren_min_v = f"({paren_max[i][k]} {Operators[k]} {paren_max[k + 1][j]})"
        if a > max_v:
            max_v = a
            paren_max_v = f"({paren_max[i][k]} {Operators[k]} {paren_max[k + 1][j]})"
        b = calc(M[i][k], m[k + 1][j], Operators[k])
        if b < min_v:
            min_v = b
            paren_min_v = f"({paren_max[i][k]} {Operators[k]} {paren_min[k + 1][j]})"
        if b > max_v:
            max_v = b
            paren_max_v = f"({paren_max[i][k]} {Operators[k]} {paren_min[k + 1][j]})"
        c = calc(m[i][k], M[k + 1][j], Operators[k])
        if c < min_v:
            min_v = c
            paren_min_v = f"({paren_min[i][k]} {Operators[k]} {paren_max[k + 1][j]})"
        if c > max_v:
            max_v = c
            paren_max_v = f"({paren_min[i][k]} {Operators[k]} {paren_max[k + 1][j]})"
        d = calc(m[i][k], m[k + 1][j], Operators[k])
        if d < min_v:
            min_v = d
            paren_min_v = f"({paren_min[i][k]} {Operators[k]} {paren_min[k + 1][j]})"
        if d > max_v:
            max_v = d
            paren_max_v = f"({paren_min[i][k]} {Operators[k]} {paren_min[k + 1][j]})"
    return min_v, max_v, paren_min_v, paren_max_v


def Parentheses(Operands, Oherators):
    n = len(Operands)
    m = [[0] * n for _ in range(n)]
    M = [[0] * n for _ in range(n)]
    paren_max = [[""] * n for _ in range(n)]
    paren_min = [[""] * n for _ in range(n)]
    for i in range(n):
        m[i][i] = Operands[i]
        M[i][i] = Operands[i]
        paren_max[i][i] = str(Operands[i])
        paren_min[i][i] = str(Operands[i])
    for s in range(1, n):
        for i in range(0, n - s):
            j = i + s
            m[i][j], M[i][j], paren_min[i][j], paren_max[i][j] = MinAndMax(Oherators, m, M, paren_min, paren_max, i, j)
    return M[0][n - 1], paren_max[0][n - 1]


Expression = input()
# Expression = "5-8+7*4-8+9"
Operands = tuple(map(int, tuple(Expression[::2])))
Operators = Expression[1::2]
res, express_res = Parentheses(Operands, Operators)
print(f'{express_res} = {res}')

import math


def calc(a, b, op):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
def MinAndMax(Operators, m, M, i, j):
    min_v = math.inf
    max_v = -math.inf
    for k in range(i, j):
        a = calc(M[i][k], M[k + 1][j], Operators[k])
        b = calc(M[i][k], m[k + 1][j], Operators[k])
        c = calc(m[i][k], M[k + 1][j], Operators[k])
        d = calc(m[i][k], m[k + 1][j], Operators[k])
        min_v = min(min_v, a, b, c, d)
        max_v = max(max_v, a, b, c, d)
    return min_v, max_v


def Parentheses(Operands, Oherators):
    n = len(Operands)
    m = [[0] * n for _ in range(n)]
    M = [[0] * n for _ in range(n)]
    for i in range(n):
        m[i][i] = Operands[i]
        M[i][i] = Operands[i]
    for s in range(1, n):
        for i in range(0, n - s):
            j = i + s
            m[i][j], M[i][j] = MinAndMax(Oherators, m, M, i, j)
    return M[0][n - 1], m, M


Expression = input()
Operands = tuple(map(int, tuple(Expression[::2])))
Operators = Expression[1::2]
res, arr1, arr2 = Parentheses(Operands, Operators)
print(res)
'''for row in arr1:
    print(*row)
print()
for row in arr2:
    print(*row)'''

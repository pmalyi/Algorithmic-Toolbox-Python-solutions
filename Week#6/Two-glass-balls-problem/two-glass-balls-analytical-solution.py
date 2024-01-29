from math import sqrt, ceil
def calcMinThrows(floors):
    return ceil(sqrt(2 * floors - 1.75) - 0.5)


n = int(input())
ans = calcMinThrows(n)
print(ans)

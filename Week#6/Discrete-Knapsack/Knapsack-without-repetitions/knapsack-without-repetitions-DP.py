def knapsackWithOutRep(n, W, w, v):
    value = [[0] * (W + 1) for _ in range(n + 1)]
    prev = []
    for i in range(1, n + 1):
        for u in range(1, W + 1):
            value[i][u] = value[i - 1][u]
            if w[i - 1] <= u:
                val = value[i - 1][u - w[i - 1]] + v[i - 1]
                if val > value[i][u]:
                    value[i][u] = val
        if value[i - 1][W] == value[i][W]:
            prev.append(value[i - 1][W])
        else:
            prev.append(value[i - 1][W - w[i]])
    prev.append(value[n][W])
    tracing = [True] * n
    current = n
    while current > 0:
        if prev[current] == prev[current - 1]:
            tracing[current - 1] = False
        current -= 1
    return value[n][W], value, tracing


def traicing(value, w, n, W, ans):
    if value[n][W] == 0:
        return
    if value[n - 1][W] == value[n][W]:
        traicing(value, w, n - 1, W, ans)
    else:
        traicing(value, w, n - 1, W - w[n], ans)
        ans.append(n - 1)


inFile = open('input.txt', 'r')
n, W = map(int, inFile.readline().split())
w = tuple(map(int, inFile.readline().split()))
v = tuple(map(int, inFile.readline().split()))
inFile.close()
result, arr, tracing = knapsackWithOutRep(n, W, w, v)
things = []
traicing(arr, w, n, W, things)
print(result)
for i in range(n):
    if tracing[i]:
        print(v[i], end=' ')
print()
for i in things:
    print(v[i], end=' ')
print()
for row in arr:
    for item in row:
        print(f'{item:2d}', end=' ')
    print()
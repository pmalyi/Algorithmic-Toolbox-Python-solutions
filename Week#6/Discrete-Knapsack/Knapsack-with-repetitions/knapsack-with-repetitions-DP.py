# Максимізація вартості наповненого рюкзака з повтореннями
def knapsackWithRep(n, W, w, v):
    value = [0] * (W + 1)
    prev = [-1] * (W + 1)
    TakeItem = [-1] * (W + 1)
    for u in range(1, W + 1):
        for i in range(n):
            if w[i] <= u:
                val = value[u - w[i]] + v[i]
                if val > value[u]:
                    value[u] = val
                    prev[u] = u - w[i]
                    TakeItem[u] = i
    tracing = []
    current = W
    while current > 0:
        tracing.append(TakeItem[current])
        current = prev[current]

    return value[W], tracing


n, W = map(int, input().split())
w = tuple(map(int, input().split()))
v = tuple(map(int, input().split()))
res1, res2 = knapsackWithRep(n, W, w, v)
print(f'${res1}')
for i in res2:
    print(f'${v[i]}', end=' ')
print()
for i in res2:
    print(f'{w[i]}kg', end=' ')

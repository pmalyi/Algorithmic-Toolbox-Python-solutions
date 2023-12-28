def MAG(G, W, n):
    T = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for u in range(1, W + 1):
            T[i][u] = T[i - 1][u]
            if G[i - 1] <= u:
                val = T[i - 1][u - G[i - 1]] + G[i - 1]
                if val > T[i][u]:
                    T[i][u] = val
    return T[n][W]

W, n = map(int, input().split())
G = list(map(int, input().split()))
ans = MAG(G, W, n)
print(ans)

# не проходить усі тести
def solve(A, W, n):
    T = [[0] * (W + 1) for _ in range(n + 1)]
    count = 0
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            T[i][j] = T[i - 1][j]
            if A[i - 1] <= j:
                val = T[i - 1][j - A[i - 1]] + A[i - 1]
                if val > T[i][j]:
                    T[i][j] = val
            if T[i][j] == W:
                count += 1
    if count < 3:
        return 0
    return 1
    #return 1, count, T


n = int(input())
A = tuple(map(int, input().split()))
sum_A = sum(A)
if n < 3 or sum_A % 3 != 0:
    ans = 0
else:
    part = sum_A // 3
    ans = solve(A, part, n)
    '''ans, count, arr = solve(A, part, n)
    print(part)
    print(count)
    for row in arr:
        print(*row)'''
print(ans)
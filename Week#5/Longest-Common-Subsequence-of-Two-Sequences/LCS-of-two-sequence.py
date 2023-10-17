def LCS(A, B, n, m):
    DP = [[0] * (m + 1) for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            diff = 1 if A[i - 1] == B[j - 1] else 0
            DP[i][j] = max(DP[i - 1][j], DP[i][j - 1], DP[i - 1][j - 1] + diff)
    return DP[n][m]


n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
print(LCS(A,B, n, m))

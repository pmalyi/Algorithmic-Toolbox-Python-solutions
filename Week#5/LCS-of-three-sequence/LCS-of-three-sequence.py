def LCS(A, B, C, n, m, l):
    DP = [[[0] * (l + 1) for i in range(m + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for q in range(1, l + 1):
                diff = 1 if A[i - 1] == B[j - 1] == C[q - 1] else 0
                DP[i][j][q] = max(DP[i - 1][j][q], DP[i][j - 1][q], DP[i][j][q - 1], DP[i - 1][j - 1][q - 1] + diff)
    return DP[n][m][l]


n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
l = int(input())
C = list(map(int, input().split()))
print(LCS(A,B, C, n, m, l))

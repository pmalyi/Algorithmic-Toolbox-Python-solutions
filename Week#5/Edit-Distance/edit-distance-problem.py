def edit_distance(A, B, n, m):
    DP = [[0] * (m + 1) for i in range(n + 1)]
    for i in range(n + 1):
        DP[i][0] = i
    for j in range(m + 1):
        DP[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            diff = 0 if A[i - 1] == B[j - 1] else 1
            insertion = DP[i][j - 1] + 1
            deletion = DP[i - 1][j] + 1
            math_mismath = DP[i - 1][j - 1] + diff
            DP[i][j] = min(insertion, deletion, math_mismath)
    return DP[n][m]


str1 = input()
str2 = input()
n = len(str1)
m = len(str2)
ED = edit_distance(str1, str2, n, m)
print(ED)

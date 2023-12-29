# https://education.yandex.ru/handbook/algorithms/article/zadacha-suveniry
def split(A, n):
    sum_A = sum(A)
    if sum_A % 3 != 0:
        return False
    V = sum_A // 3
    T = [[[False] * (V + 1) for _ in range(V + 1)] for __ in range(n + 1)]
    T[0][0][0] = True
    for i in range(1, n + 1):
        for s1 in range(V + 1):
            for s2 in range(V + 1):
                T[i][s1][s2] = T[i - 1][s1][s2]
                if s1 >= A[i - 1]:
                    T[i][s1][s2] = T[i][s1][s2] or T[i - 1][s1 - A[i - 1]][s2]
                if s2 >= A[i - 1]:
                    T[i][s1][s2] = T[i][s1][s2] or T[i - 1][s1][s2 - A[i - 1]]
    return T[n][V][V]


n = int(input())
A = tuple(map(int, input().split()))
res = split(A, n)
if res:
    print(1)
else:
    print(0)
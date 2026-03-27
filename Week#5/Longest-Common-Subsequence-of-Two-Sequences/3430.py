# https://cses.fi/problemset/task/3403

import sys


def solve(a, b, n, m):

    # dp[i][j] зберігає довжину LCS для a[:i] та b[:j]
    # Розмір (n+1) x (m+1)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Заповнення таблиці DP
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                # Якщо числа збігаються, збільшуємо довжину на 1
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # Якщо ні, вибираємо найкращий результат з попередніх станів
                #  беремо максимум з двох варіантів: dp[i][j] = max(dp[i-1][j], dp[i][j-1]).
                if dp[i - 1][j] >= dp[i][j - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - 1]

    # Виводимо довжину LCS
    ans_length = dp[n][m]
    print(ans_length)

    # Відновлення самої послідовності (йдемо з кінця таблиці)
    lcs = []
    curr_i, curr_j = n, m
    while curr_i > 0 and curr_j > 0:
        if a[curr_i - 1] == b[curr_j - 1]:
            # Елемент входить у LCS
            lcs.append(a[curr_i - 1])
            curr_i -= 1
            curr_j -= 1
        elif dp[curr_i - 1][curr_j] >= dp[curr_i][curr_j - 1]:
            # Рухаємося в сторону більшого значення
            curr_i -= 1
        else:
            curr_j -= 1

    # Оскільки ми збирали елементи з кінця, їх треба розвернути
    if lcs:
        print(*(lcs[::-1]))


if __name__ == "__main__":
    # Читання вхідних даних
    n, m = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    solve(a, b, n, m)
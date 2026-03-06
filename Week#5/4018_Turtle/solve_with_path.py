def min_acid_path_with_route():
    # Зчитуємо розміри таблиці
    n, m = map(int, input().split())

    # Зчитуємо таблицю з кислотою
    acid = []
    for _ in range(n):
        acid.append(list(map(int, input().split())))

    # Створюємо DP-таблицю
    dp = [[0] * m for _ in range(n)]

    # Заповнюємо DP-таблицю (прямий хід)
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                dp[i][j] = acid[i][j]
            elif i == 0:
                dp[i][j] = dp[i][j - 1] + acid[i][j]
            elif j == 0:
                dp[i][j] = dp[i - 1][j] + acid[i][j]
            else:
                dp[i][j] = acid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

    # Виводимо мінімальну шкоду
    print(f"Мінімальна шкода: {dp[n - 1][m - 1]}")

    # Відновлення шляху (зворотний хід)
    path = []
    curr_i, curr_j = n - 1, m - 1

    while curr_i > 0 or curr_j > 0:
        if curr_i == 0:  # Ми в першому рядку, шлях тільки зліва
            path.append("R")
            curr_j -= 1
        elif curr_j == 0:  # Ми в першому стовпчику, шлях тільки зверху
            path.append("D")
            curr_i -= 1
        else:
            # Порівнюємо значення в сусідніх клітинках DP-таблиці
            if dp[curr_i - 1][curr_j] < dp[curr_i][curr_j - 1]:
                path.append("D")
                curr_i -= 1
            else:
                path.append("R")
                curr_j -= 1

    # Оскільки ми йшли з кінця в початок, список треба розвернути
    print("Шлях:", "".join(path[::-1]))


min_acid_path_with_route()
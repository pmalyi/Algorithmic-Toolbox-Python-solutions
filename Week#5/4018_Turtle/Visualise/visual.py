import matplotlib.pyplot as plt
import numpy as np


def visualize_turtle_path():
    # Вхідні дані
    acid = np.array([
        [5, 9, 4, 3],
        [3, 1, 6, 9],
        [8, 6, 8, 12]
    ])
    n, m = acid.shape

    # 1. Розрахунок DP-таблиці
    dp = np.zeros((n, m))
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

    # 2. Відновлення шляху (Backtracking)
    path = []
    curr_i, curr_j = n - 1, m - 1
    path.append((curr_i, curr_j))

    while curr_i > 0 or curr_j > 0:
        if curr_i == 0:
            curr_j -= 1
        elif curr_j == 0:
            curr_i -= 1
        else:
            if dp[curr_i - 1][curr_j] < dp[curr_i][curr_j - 1]:
                curr_i -= 1
            else:
                curr_j -= 1
        path.append((curr_i, curr_j))
    path.reverse()

    # 3. Візуалізація
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_xlim(-0.5, m - 0.5)
    ax.set_ylim(n - 0.5, -0.5)  # Перевертаємо вісь Y для вигляду таблиці

    # Малюємо сітку та числа
    for i in range(n):
        for j in range(m):
            # Малюємо клітинку
            rect = plt.Rectangle((j - 0.5, i - 0.5), 1, 1, fill=False, color='black', lw=1)
            ax.add_patch(rect)

            # Текст: значення кислоти та DP (накопичена шкода)
            ax.text(j, i, f'Data: {acid[i, j]}\nDP: {int(dp[i, j])}',
                    ha='center', va='center', fontweight='bold')

    # Малюємо стрілки шляху
    for k in range(len(path) - 1):
        y1, x1 = path[k]
        y2, x2 = path[k + 1]

        # Малюємо стрілку від поточної до наступної клітинки
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color='red', lw=3, mutation_scale=20))

    # Налаштування вигляду
    plt.title(f"Мінімальний шлях черепашки (Сума: {int(dp[n - 1, m - 1])})", fontsize=14)
    plt.xticks(range(m))
    plt.yticks(range(n))
    plt.grid(False)
    plt.show()


if __name__ == "__main__":
    visualize_turtle_path()

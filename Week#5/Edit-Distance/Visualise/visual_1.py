import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


def animate_levenshtein(word1, word2):
    word1 = "#" + word1
    word2 = "#" + word2
    n, m = len(word1), len(word2)

    # Ініціалізація матриці
    dp = np.zeros((n, m))

    fig, ax = plt.subplots(figsize=(8, 6))

    def update(frame):
        ax.clear()
        i = frame // m
        j = frame % m

        # Розрахунок значення для поточної клітинки
        if i == 0:
            dp[i, j] = j
        elif j == 0:
            dp[i, j] = i
        else:
            cost = 0 if word1[i] == word2[j] else 1
            dp[i, j] = min(dp[i - 1, j] + 1,  # Видалення
                           dp[i, j - 1] + 1,  # Вставка
                           dp[i - 1, j - 1] + cost)  # Заміна

        # Малювання таблиці
        ax.matshow(np.ones_like(dp), cmap="Blues", alpha=0.1)  # Світла сітка

        for r in range(n):
            for c in range(m):
                val = dp[r, c] if (r * m + c) <= frame else ""
                color = "red" if (r == i and c == j) else "black"
                ax.text(c, r, f"{int(val) if val != '' else ''}",
                        va='center', ha='center', fontsize=14, color=color)

        # Налаштування осей
        ax.set_xticks(range(m))
        ax.set_xticklabels(list(word2))
        ax.set_yticks(range(n))
        ax.set_yticklabels(list(word1))
        ax.set_title(f"Крок {frame + 1}: Заповнення клітинки ({i}, {j})", pad=20)

    ani = animation.FuncAnimation(fig, update, frames=n * m, interval=500, repeat=False)
    plt.show()


# Запуск для прикладу horse -> ros
animate_levenshtein("edit", "distance")
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import numpy as np


def visualize_levenshtein_interactive(word1_raw, word2_raw):
    # Додаємо символ порожнього рядка
    w1 = "#" + word1_raw
    w2 = "#" + word2_raw
    n, m = len(w1), len(w2)

    dp = np.zeros((n, m))
    mask = np.zeros((n, m), dtype=bool)  # Для відстеження заповнених клітинок
    current_step = [0]  # Використовуємо список для мутації в середині функції

    fig, ax = plt.subplots(figsize=(12, 8))
    plt.subplots_adjust(bottom=0.2)  # Місце для кнопки та тексту

    def update_plot(step):
        ax.clear()
        i, j = divmod(step, m)

        # Обчислення логіки
        explanation = ""
        if i == 0:
            dp[i, j] = j
            explanation = f"Рядок #: word2 порожній. Потрібно {j} вставок."
        elif j == 0:
            dp[i, j] = i
            explanation = f"Стовпчик #: word1 порожній. Потрібно {i} видалень."
        else:
            cost = 0 if w1[i] == w2[j] else 1
            delete = dp[i - 1, j] + 1
            insert = dp[i, j - 1] + 1
            replace = dp[i - 1, j - 1] + cost

            dp[i, j] = min(delete, insert, replace)

            if w1[i] == w2[j]:
                explanation = f"Символи '{w1[i]}' збігаються! Копіюємо діагональ: {int(dp[i - 1, j - 1])}"
            else:
                explanation = f"'{w1[i]}' != '{w2[j]}'. min(Del:{int(delete)}, Ins:{int(insert)}, Rep:{int(replace)}) = {int(dp[i, j])}"

        mask[i, j] = True

        # Візуалізація матриці
        display_data = np.where(mask, dp, np.nan)
        im = ax.matshow(np.ones_like(dp), cmap="Pastel1", alpha=0.3)

        # Малюємо числа та підсвітку
        for r in range(n):
            for c in range(m):
                if mask[r, c]:
                    color = "red" if (r == i and c == j) else "black"
                    weight = "bold" if (r == i and c == j) else "normal"
                    ax.text(c, r, f"{int(dp[r, c])}", va='center', ha='center',
                            fontsize=18, color=color, fontweight=weight)

        # Налаштування осей (збільшені шрифти)
        ax.set_xticks(range(m))
        ax.set_xticklabels(list(w2), fontsize=20, fontweight='bold')
        ax.set_yticks(range(n))
        ax.set_yticklabels(list(w1), fontsize=20, fontweight='bold')

        ax.set_title(f"Крок {step + 1}: Порівнюємо '{w1[i]}' та '{w2[j]}'", fontsize=16, pad=20)
        fig.text(0.5, 0.05, f"Логіка: {explanation}", ha='center', fontsize=12,
                 bbox=dict(facecolor='white', alpha=0.8), wrap=True)

        plt.draw()

    # Початковий стан
    update_plot(0)

    # Додавання кнопки
    ax_button = plt.axes([0.45, 0.1, 0.1, 0.05])
    btn_next = Button(ax_button, 'NEXT', color='lightgreen', hovercolor='green')

    def next_callback(event):
        if current_step[0] < n * m - 1:
            current_step[0] += 1
            # Очищуємо попередній текст пояснення перед оновленням
            for txt in fig.texts: txt.set_visible(False)
            update_plot(current_step[0])

    btn_next.on_clicked(next_callback)
    plt.show()


# Запуск
visualize_levenshtein_interactive("horse", "ros")
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox
import numpy as np


class LevenshteinVisualizer:
    def __init__(self, word1="horse", word2="ros"):
        self.setup_data(word1, word2)
        self.create_ui()

    def setup_data(self, w1_raw, w2_raw):
        self.w1 = "#" + w1_raw
        self.w2 = "#" + w2_raw
        self.n, self.m = len(self.w1), len(self.w2)
        self.dp = np.zeros((self.n, self.m))
        self.mask = np.zeros((self.n, self.m), dtype=bool)
        self.current_step = 0

    def create_ui(self):
        self.fig, self.ax = plt.subplots(figsize=(12, 9))
        plt.subplots_adjust(bottom=0.3)  # Місце для панелі керування

        # Поля для введення слів
        axbox1 = plt.axes([0.15, 0.15, 0.2, 0.05])
        self.text_box1 = TextBox(axbox1, 'Word 1: ', initial=self.w1[1:])

        axbox2 = plt.axes([0.45, 0.15, 0.2, 0.05])
        self.text_box2 = TextBox(axbox2, 'Word 2: ', initial=self.w2[1:])

        # Кнопки
        ax_next = plt.axes([0.7, 0.15, 0.1, 0.05])
        self.btn_next = Button(ax_next, 'NEXT', color='lightgreen')
        self.btn_next.on_clicked(self.next_step)

        ax_reset = plt.axes([0.82, 0.15, 0.1, 0.05])
        self.btn_reset = Button(ax_reset, 'RESET', color='tomato')
        self.btn_reset.on_clicked(self.reset)

        self.update_plot()
        plt.show()

    def update_plot(self):
        self.ax.clear()
        i, j = divmod(self.current_step, self.m)
        self.mask[i, j] = True

        # Логіка обчислень
        cost = 0
        formula_text = ""
        if i == 0:
            self.dp[i, j] = j
        elif j == 0:
            self.dp[i, j] = i
        else:
            cost = 0 if self.w1[i] == self.w2[j] else 1
            left = self.dp[i, j - 1]  # Insertion
            top = self.dp[i - 1, j]  # Deletion
            diag = self.dp[i - 1, j - 1]  # Replacement
            self.dp[i, j] = min(left + 1, top + 1, diag + cost)

            # Динамічне відображення формули
            formula_text = f"min(←{int(left)}+1, ↑{int(top)}+1, ↖{int(diag)}+{cost}) = {int(self.dp[i, j])}"

        # Малювання сітки
        self.ax.matshow(np.ones_like(self.dp), cmap="GnBu", alpha=0.1)

        for r in range(self.n):
            for c in range(self.m):
                if self.mask[r, c]:
                    is_current = (r == i and c == j)
                    self.ax.text(c, r, f"{int(self.dp[r, c])}", va='center', ha='center',
                                 fontsize=20, color="red" if is_current else "black",
                                 fontweight='bold' if is_current else 'normal')

        # Оформлення осей
        self.ax.set_xticks(range(self.m))
        self.ax.set_xticklabels(list(self.w2), fontsize=22, fontweight='bold')
        self.ax.set_yticks(range(self.n))
        self.ax.set_yticklabels(list(self.w1), fontsize=22, fontweight='bold')

        # Вивід формули та стану
        status = f"Порівнюємо: '{self.w1[i]}' vs '{self.w2[j]}'"
        self.ax.set_title(f"{status}\n{formula_text}", fontsize=16, color='darkblue', pad=25)
        plt.draw()

    def next_step(self, event):
        if self.current_step < (self.n * self.m - 1):
            self.current_step += 1
            self.update_plot()

    def reset(self, event):
        # Зчитуємо нові слова з полів введення
        new_w1 = self.text_box1.text if self.text_box1.text else " "
        new_w2 = self.text_box2.text if self.text_box2.text else " "
        self.setup_data(new_w1, new_w2)
        self.update_plot()


if __name__ == "__main__":
    LevenshteinVisualizer()
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
        self.fig = plt.figure(figsize=(15, 10))

        # Створюємо сітку: 0-7 для таблиці, 8-9 для формули під нею
        self.ax = plt.subplot2grid((11, 15), (0, 0), colspan=10, rowspan=8)
        self.ax_info = plt.subplot2grid((11, 15), (0, 11), colspan=4, rowspan=8)
        self.ax_formula = plt.subplot2grid((11, 15), (8, 0), colspan=15, rowspan=1)

        self.ax_formula.axis('off')
        self.ax_info.axis('off')

        plt.subplots_adjust(bottom=0.2, left=0.1, right=0.95, top=0.95)

        # Поля для введення
        self.text_box1 = TextBox(plt.axes([0.15, 0.05, 0.1, 0.04]), 'W1: ', initial=self.w1[1:])
        self.text_box2 = TextBox(plt.axes([0.35, 0.05, 0.1, 0.04]), 'W2: ', initial=self.w2[1:])

        # Кнопки
        self.btn_next = Button(plt.axes([0.55, 0.05, 0.1, 0.04]), 'NEXT STEP', color='lightgreen')
        self.btn_next.on_clicked(self.next_step)

        self.btn_reset = Button(plt.axes([0.7, 0.05, 0.1, 0.04]), 'RESET', color='tomato')
        self.btn_reset.on_clicked(self.reset)

        self.update_plot()
        plt.show()

    def update_plot(self):
        self.ax.clear()
        self.ax_info.clear()
        self.ax_formula.clear()
        self.ax_info.axis('off')
        self.ax_formula.axis('off')

        i, j = divmod(self.current_step, self.m)
        self.mask[i, j] = True

        char1, char2 = self.w1[i], self.w2[j]
        explanation = ""
        formula = ""

        # Обчислення та формування логічного пояснення
        if i == 0 and j == 0:
            self.dp[i, j] = 0
            explanation = "Старт: обидва рядки порожні.\nВартість = 0."
            formula = r"$D[0][0] = 0$"
        elif i == 0:
            self.dp[i, j] = j
            explanation = f"Базовий регістр:\nПеретворюємо '' в '{self.w2[1:j + 1]}'.\nОперація: Вставка '{char2}'.\nСума: {j}"
            formula = fr"$D[0][{j}] = D[0][{j - 1}] + 1 = {int(j - 1)} + 1 = {int(j)}$"
        elif j == 0:
            self.dp[i, j] = i
            explanation = f"Базовий регістр:\nПеретворюємо '{self.w1[1:i + 1]}' в ''.\nОперація: Видалення '{char1}'.\nСума: {i}"
            formula = fr"$D[{i}][0] = D[{i - 1}][0] + 1 = {int(i - 1)} + 1 = {int(i)}$"
        else:
            cost = 0 if char1 == char2 else 1
            left = self.dp[i, j - 1]
            top = self.dp[i - 1, j]
            diag = self.dp[i - 1, j - 1]

            res = min(left + 1, top + 1, diag + cost)
            self.dp[i, j] = res

            formula = (fr"$D[{i}][{j}] = \min("
                       fr"{int(left)}+1, "
                       fr"{int(top)}+1, "
                       fr"{int(diag)}+{cost}"
                       fr") = {int(res)}$")

            if char1 == char2:
                explanation = f"Символи '{char1}' та '{char2}' ОДНАКОВІ.\nБеремо значення по діагоналі (↖).\nНічого не додаємо.\nРезультат: {int(diag)}"
            else:
                op_name = ""
                if res == diag + 1:
                    op_name = f"Заміна '{char1}' на '{char2}' (↖)"
                elif res == top + 1:
                    op_name = f"Видалення '{char1}' (↑)"
                else:
                    op_name = f"Вставка '{char2}' (←)"

                explanation = f"Символи '{char1}' та '{char2}' РІЗНІ.\nОбираємо мінімум з:\n- Вставка (←): {int(left + 1)}\n- Видалення (↑): {int(top + 1)}\n- Заміна (↖): {int(diag + 1)}\n\nРішення: {op_name}"

        # Візуалізація таблиці
        self.ax.matshow(np.ones_like(self.dp), cmap="bone", alpha=0.05)
        for r in range(self.n):
            for c in range(self.m):
                if self.mask[r, c]:
                    is_curr = (r == i and c == j)
                    self.ax.text(c, r, f"{int(self.dp[r, c])}", va='center', ha='center',
                                 fontsize=22, color="red" if is_curr else "black",
                                 fontweight='bold' if is_curr else 'normal')

        # Оформлення
        self.ax.set_xticks(range(self.m))
        self.ax.set_xticklabels(list(self.w2), fontsize=20, fontweight='bold')
        self.ax.set_yticks(range(self.n))
        self.ax.set_yticklabels(list(self.w1), fontsize=20, fontweight='bold')

        # Формула під таблицею
        self.ax_formula.text(0.5, 0.5, formula, fontsize=26, ha='center', va='center',
                             color='darkblue', fontweight='bold',
                             bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))

        # Пояснення праворуч
        self.ax_info.text(0, 0.9, "ЛОГІКА КРОКУ:", fontsize=16, fontweight='bold', color='darkred')
        self.ax_info.text(0, 0.5, explanation, fontsize=14, va='center', linespacing=1.5,
                          bbox=dict(facecolor='wheat', alpha=0.3, boxstyle='round,pad=1'))

        self.ax.set_title(f"Крок {self.current_step + 1}: Порівняння префіксів", fontsize=18, pad=20)
        plt.draw()

    def next_step(self, event):
        if self.current_step < (self.n * self.m - 1):
            self.current_step += 1
            self.update_plot()

    def reset(self, event):
        self.setup_data(self.text_box1.text, self.text_box2.text)
        self.update_plot()


if __name__ == "__main__":
    LevenshteinVisualizer()
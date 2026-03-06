import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox
import numpy as np
import textwrap


class LevenshteinFixedVisualizer:
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
        # Використовуємо constrained_layout для запобігання накладанню
        self.fig = plt.figure(figsize=(15, 9))
        gs = self.fig.add_gridspec(12, 15)

        # Зона 1: Формула (Верхня частина, окремий простір)
        self.ax_formula = self.fig.add_subplot(gs[0:2, :])
        self.ax_formula.axis('off')

        # Зона 2: Таблиця (Центральна ліва частина)
        self.ax = self.fig.add_subplot(gs[2:10, 0:10])

        # Зона 3: Логіка (Права частина)
        self.ax_info = self.fig.add_subplot(gs[2:10, 11:15])
        self.ax_info.axis('off')

        # Поля та кнопки (Нижня частина)
        self.text_box1 = TextBox(plt.axes([0.1, 0.05, 0.1, 0.04]), 'W1: ', initial=self.w1[1:])
        self.text_box2 = TextBox(plt.axes([0.25, 0.05, 0.1, 0.04]), 'W2: ', initial=self.w2[1:])

        self.btn_next = Button(plt.axes([0.45, 0.05, 0.1, 0.04]), 'NEXT STEP', color='lightgreen')
        self.btn_next.on_clicked(self.next_step)

        self.btn_reset = Button(plt.axes([0.57, 0.05, 0.1, 0.04]), 'RESET', color='tomato')
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

        formula_str = ""
        logic_str = ""

        # Обчислення з деталізацією "+"
        if i == 0 and j == 0:
            self.dp[i, j] = 0
            formula_str = r"$D[0][0] = 0$"
            logic_str = "Порожні рядки: 0 операцій."
        elif i == 0:
            self.dp[i, j] = j
            formula_str = fr"$D[0][{j}] = D[0][{j - 1}] + 1 = {j - 1} + 1 = {j}$"
            logic_str = f"Вставка символу '{char2}'."
        elif j == 0:
            self.dp[i, j] = i
            formula_str = fr"$D[{i}][0] = D[{i - 1}][0] + 1 = {i - 1} + 1 = {i}$"
            logic_str = f"Видалення символу '{char1}'."
        else:
            cost = 0 if char1 == char2 else 1
            v_ins = self.dp[i, j - 1]
            v_del = self.dp[i - 1, j]
            v_rep = self.dp[i - 1, j - 1]

            self.dp[i, j] = min(v_ins + 1, v_del + 1, v_rep + cost)

            # Детальна формула з плюсами
            formula_str = (fr"$D[{i}][{j}] = \min("
                           fr"{int(v_ins)} + 1 [Ins], "
                           fr"{int(v_del)} + 1 [Del], "
                           fr"{int(v_rep)} + {cost} [Rep/Match]) = {int(self.dp[i, j])}$")

            if cost == 0:
                logic_str = f"'{char1}' == '{char2}':\nЗбіг! Вартість не зростає."
            else:
                logic_str = f"'{char1}' != '{char2}':\nОбираємо мінімальну дію (+1)."

        # Малювання таблиці
        self.ax.matshow(np.ones_like(self.dp), cmap="GnBu", alpha=0.1)
        for r in range(self.n):
            for c in range(self.m):
                if self.mask[r, c]:
                    is_curr = (r == i and c == j)
                    self.ax.text(c, r, f"{int(self.dp[r, c])}", va='center', ha='center',
                                 fontsize=18, color="red" if is_curr else "black",
                                 fontweight='bold' if is_curr else 'normal')

        # Оформлення осей
        self.ax.set_xticks(range(self.m))
        self.ax.set_xticklabels(list(self.w2), fontsize=20, fontweight='bold')
        self.ax.set_yticks(range(self.n))
        self.ax.set_yticklabels(list(self.w1), fontsize=20, fontweight='bold')

        # Візуалізація формули (тепер вона зверху в окремому полі)
        self.ax_formula.text(0.5, 0.5, formula_str, fontsize=22, ha='center', va='center', color='darkred',
                             bbox=dict(facecolor='white', edgecolor='none', alpha=0.8))

        # Візуалізація логіки
        self.ax_info.text(0, 0.8, "АНАЛІЗ:", fontsize=16, fontweight='bold')
        wrapped_logic = "\n".join([textwrap.fill(line, width=25) for line in logic_str.split("\n")])
        self.ax_info.text(0, 0.4, wrapped_logic, fontsize=13, va='center', linespacing=1.5,
                          bbox=dict(facecolor='ivory', edgecolor='gray', boxstyle='round,pad=1'))

        plt.draw()

    def next_step(self, event):
        if self.current_step < (self.n * self.m - 1):
            self.current_step += 1
            self.update_plot()

    def reset(self, event):
        self.setup_data(self.text_box1.text, self.text_box2.text)
        self.update_plot()


if __name__ == "__main__":
    LevenshteinFixedVisualizer()
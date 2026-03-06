import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox
import numpy as np
import textwrap


class LevenshteinFinalVisualizer:
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
        # Створюємо вікно з фіксованою сіткою (GridSpec)
        self.fig = plt.figure(figsize=(15, 9))
        gs = self.fig.add_gridspec(12, 16)

        # Панель формули (Верх)
        self.ax_formula = self.fig.add_subplot(gs[0:2, :])
        self.ax_formula.axis('off')

        # Таблиця (Центр)
        self.ax = self.fig.add_subplot(gs[2:11, 0:11])

        # Панель логіки (Праворуч)
        self.ax_info = self.fig.add_subplot(gs[2:11, 12:16])
        self.ax_info.axis('off')

        # Контролери (Низ) - використовуються статичні координати для кнопок
        self.text_box1 = TextBox(plt.axes([0.1, 0.04, 0.1, 0.04]), 'W1: ', initial=self.w1[1:])
        self.text_box2 = TextBox(plt.axes([0.25, 0.04, 0.1, 0.04]), 'W2: ', initial=self.w2[1:])

        self.btn_next = Button(plt.axes([0.45, 0.04, 0.1, 0.04]), 'NEXT STEP', color='lightgreen')
        self.btn_next.on_clicked(self.next_step)

        self.btn_reset = Button(plt.axes([0.57, 0.04, 0.1, 0.04]), 'RESET', color='tomato')
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
        c1, c2 = self.w1[i], self.w2[j]

        formula_str = ""
        logic_text = ""

        # --- ЛОГІКА ЗГІДНО З ВАШИМ ЗРАЗКОМ ---
        if i == 0 and j == 0:
            self.dp[0, 0] = 0
            formula_str = r"$D[0][0] = 0$"
            logic_text = ("ОПЕРАЦІЯ: Старт\n"
                          "ПОПЕРЕДНЄ: немає\n"
                          "РОЗРАХУНОК: 0")
        elif i == 0:
            self.dp[i, j] = j
            formula_str = fr"$D[0][{j}] = D[0][{j - 1}] + 1 = {j - 1} + 1 = {j}$"
            logic_text = (f"ОПЕРАЦІЯ: Вставка '{c2}'\n"
                          f"ПОПЕРЕДНЄ (←): {j - 1}\n"
                          f"РОЗРАХУНОК: {j - 1} + 1 = {j}")
        elif j == 0:
            self.dp[i, j] = i
            formula_str = fr"$D[{i}][0] = D[{i - 1}][0] + 1 = {i - 1} + 1 = {i}$"
            logic_text = (f"ОПЕРАЦІЯ: Видалення '{c1}'\n"
                          f"ПОПЕРЕДНЄ (↑): {i - 1}\n"
                          f"РОЗРАХУНОК: {i - 1} + 1 = {i}")
        else:
            cost = 0 if c1 == c2 else 1
            v_ins = self.dp[i, j - 1]
            v_del = self.dp[i - 1, j]
            v_rep = self.dp[i - 1, j - 1]

            res = min(v_ins + 1, v_del + 1, v_rep + cost)
            self.dp[i, j] = res

            # Формула для верхньої панелі (використовуємо raw strings r"" для LaTeX)
            formula_str = (fr"$D[{i}][{j}] = \min({int(v_ins)}+1, {int(v_del)}+1, {int(v_rep)}+{cost}) = {int(res)}$")

            # Логіка для правої панелі
            if c1 == c2:
                op_name = f"Збіг символів '{c1}'"
                prev_val = int(v_rep)
                calc = f"{prev_val} + 0 = {int(res)}"
            else:
                if res == v_rep + 1:
                    op_name = f"Заміна '{c1}' на '{c2}'"
                    prev_val = int(v_rep)
                    calc = f"{prev_val} + 1 = {int(res)}"
                elif res == v_del + 1:
                    op_name = f"Видалення '{c1}'"
                    prev_val = int(v_del)
                    calc = f"{prev_val} + 1 = {int(res)}"
                else:
                    op_name = f"Вставка '{c2}'"
                    prev_val = int(v_ins)
                    calc = f"{prev_val} + 1 = {int(res)}"

            logic_text = (f"ОПЕРАЦІЯ: {op_name}\n"
                          f"ПОПЕРЕДНЄ: {prev_val}\n"
                          f"РОЗРАХУНОК: {calc}")

        # --- ВІЗУАЛІЗАЦІЯ ТАБЛИЦІ ---
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

        # Відображення динамічної функції зверху
        self.ax_formula.text(0.5, 0.5, formula_str, fontsize=22, ha='center', va='center',
                             color='darkred', fontweight='bold')

        # Відображення деталей логіки праворуч
        self.ax_info.text(0, 0.85, "ДЕТАЛІ КРОКУ:", fontsize=15, fontweight='bold', color='black')
        self.ax_info.text(0, 0.45, logic_text, fontsize=13, va='center', linespacing=2.2,
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
    LevenshteinFinalVisualizer()
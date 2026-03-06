import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button


class TurtleAnimator:
    def __init__(self, acid):
        self.acid = acid
        self.n, self.m = acid.shape
        self.dp = np.full((self.n, self.m), np.nan)  # Таблиця заповнена NaN
        self.calc_i, self.calc_j = 0, 0
        self.path = []
        self.current_path_step = 0
        self.phase = "CALCULATING"  # Фази: CALCULATING -> READY_TO_MOVE -> MOVING

        # Налаштування графіка
        self.fig, self.ax = plt.subplots(figsize=(12, 8))
        plt.subplots_adjust(bottom=0.2)

        self._setup_plot()
        self.text_elements = {}  # Для оновлення значень DP в клітинках
        self._draw_initial_grid()

        # Кнопка дії
        ax_button = plt.axes([0.4, 0.05, 0.2, 0.075])
        self.btn = Button(ax_button, 'Calculate Next Cell')
        self.btn.on_clicked(self.process_click)

    def _setup_plot(self):
        self.ax.set_xlim(-0.5, self.m - 0.5)
        self.ax.set_ylim(self.n - 0.5, -0.5)
        self.ax.set_xticks(range(self.m))
        self.ax.set_yticks(range(self.n))
        self.ax.set_title("Крок 1: Заповнення таблиці DP (мінімізація шкоди)", fontsize=14)

    def _draw_initial_grid(self):
        for i in range(self.n):
            for j in range(self.m):
                rect = plt.Rectangle((j - 0.5, i - 0.5), 1, 1, fill=False, color='gray', alpha=0.3)
                self.ax.add_patch(rect)
                # Малюємо вхідні дані (acid), DP поки порожнє
                self.ax.text(j, i - 0.2, f'Acid: {self.acid[i, j]}', ha='center', va='center', color='blue', fontsize=14)
                self.text_elements[(i, j)] = self.ax.text(j, i + 0.2, 'DP: ?', ha='center', va='center', color='black',
                                                          fontweight='bold', fontsize=14)

    def calculate_step(self):
        i, j = self.calc_i, self.calc_j

        # Логіка DP
        if i == 0 and j == 0:
            self.dp[i, j] = self.acid[i, j]
        elif i == 0:
            self.dp[i, j] = self.dp[i, j - 1] + self.acid[i, j]
        elif j == 0:
            self.dp[i, j] = self.dp[i - 1, j] + self.acid[i, j]
        else:
            self.dp[i, j] = self.acid[i, j] + min(self.dp[i - 1, j], self.dp[i, j - 1])

        # Візуальне оновлення
        self.text_elements[(i, j)].set_text(f'DP: {int(self.dp[i, j])}')
        self.text_elements[(i, j)].set_color('red')

        # Підсвітка поточної клітинки
        highlight = plt.Rectangle((j - 0.5, i - 0.5), 1, 1, color='yellow', alpha=0.3)
        self.ax.add_patch(highlight)

        # Перехід до наступної клітинки
        self.calc_j += 1
        if self.calc_j == self.m:
            self.calc_j = 0
            self.calc_i += 1

        if self.calc_i == self.n:
            self.phase = "READY_TO_MOVE"
            self.btn.label.set_text("Start Turtle Path")
            self.ax.set_title("Таблицю заповнено! Натисніть для пошуку шляху", color='green')
            self._precalculate_path()

    def _precalculate_path(self):
        curr_i, curr_j = self.n - 1, self.m - 1
        self.path = [(curr_i, curr_j)]
        while curr_i > 0 or curr_j > 0:
            if curr_i == 0:
                curr_j -= 1
            elif curr_j == 0:
                curr_i -= 1
            else:
                if self.dp[curr_i - 1, curr_j] < self.dp[curr_i, curr_j - 1]:
                    curr_i -= 1
                else:
                    curr_j -= 1
            self.path.append((curr_i, curr_j))
        self.path.reverse()

    def move_step(self):
        if self.current_path_step < len(self.path) - 1:
            y1, x1 = self.path[self.current_path_step]
            y2, x2 = self.path[self.current_path_step + 1]
            self.ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                             arrowprops=dict(arrowstyle='->', color='green', lw=4, mutation_scale=25))
            self.current_path_step += 1
            if self.current_path_step == len(self.path) - 1:
                self.btn.label.set_text("Finished")
                self.ax.set_title(f"Мінімальний шлях знайдено! Сума: {int(self.dp[self.n - 1, self.m - 1])}")

    def process_click(self, event):
        if self.phase == "CALCULATING":
            self.calculate_step()
        elif self.phase == "READY_TO_MOVE":
            self.phase = "MOVING"
            self.btn.label.set_text("Next Path Step")
            self.ax.set_title("Крок 2: Відновлення шляху (Backtracking)")
        elif self.phase == "MOVING":
            self.move_step()

        self.fig.canvas.draw_idle()


if __name__ == "__main__":
    acid_data = np.array([
        [5, 9, 4, 3],
        [3, 1, 6, 9],
        [8, 6, 8, 12]
    ])
    animator = TurtleAnimator(acid_data)
    plt.show()
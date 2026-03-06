import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button

class TurtleAnimator:
    def __init__(self, acid):
        self.acid = acid
        self.n, self.m = acid.shape
        self.dp, self.path = self._calculate_logic()
        self.current_step = 0
        
        # Налаштування графіка
        self.fig, self.ax = plt.subplots(figsize=(10, 8))
        plt.subplots_adjust(bottom=0.2)  # Місце для кнопки
        
        self._setup_plot()
        self._draw_static_grid()
        
        # Додавання кнопки "Next"
        ax_button = plt.axes([0.45, 0.05, 0.1, 0.075])
        self.btn_next = Button(ax_button, 'Next')
        self.btn_next.on_clicked(self.next_step)
        
        # Початкова позиція черепашки
        self.turtle_marker, = self.ax.plot(0, 0, 'ro', markersize=15, label='Черепашка')
        self.arrows = [] # Список для збереження намальованих стрілок

    def _calculate_logic(self):
        # Ваша логіка розрахунку DP
        n, m = self.n, self.m
        dp = np.zeros((n, m))
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0: dp[i][j] = self.acid[i][j]
                elif i == 0: dp[i][j] = dp[i][j - 1] + self.acid[i][j]
                elif j == 0: dp[i][j] = dp[i - 1][j] + self.acid[i][j]
                else: dp[i][j] = self.acid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

        # Відновлення шляху
        path = []
        curr_i, curr_j = n - 1, m - 1
        path.append((curr_i, curr_j))
        while curr_i > 0 or curr_j > 0:
            if curr_i == 0: curr_j -= 1
            elif curr_j == 0: curr_i -= 1
            else:
                if dp[curr_i - 1][curr_j] < dp[curr_i][curr_j - 1]: curr_i -= 1
                else: curr_j -= 1
            path.append((curr_i, curr_j))
        path.reverse()
        return dp, path

    def _setup_plot(self):
        self.ax.set_xlim(-0.5, self.m - 0.5)
        self.ax.set_ylim(self.n - 0.5, -0.5)
        self.ax.set_xticks(range(self.m))
        self.ax.set_yticks(range(self.n))
        self.ax.set_title("Натисніть 'Next', щоб рухати черепашку", fontsize=14)

    def _draw_static_grid(self):
        for i in range(self.n):
            for j in range(self.m):
                rect = plt.Rectangle((j - 0.5, i - 0.5), 1, 1, fill=False, color='gray', alpha=0.3)
                self.ax.add_patch(rect)
                self.ax.text(j, i, f'Acid: {self.acid[i, j]}\nDP: {int(self.dp[i, j])}', 
                             ha='center', va='center', fontsize=9)

    def next_step(self, event):
        if self.current_step < len(self.path) - 1:
            # Отримуємо поточну та наступну точки
            y1, x1 = self.path[self.current_step]
            y2, x2 = self.path[self.current_step + 1]
            
            # Малюємо стрілку
            arrow = self.ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                                     arrowprops=dict(arrowstyle='->', color='red', lw=3, mutation_scale=20))
            self.arrows.append(arrow)
            
            # Оновлюємо маркер черепашки
            self.turtle_marker.set_data([x2], [y2])
            
            self.current_step += 1
            
            if self.current_step == len(self.path) - 1:
                self.ax.set_title(f"Фініш! Мінімальна шкода: {int(self.dp[self.n-1, self.m-1])}", color='green')
            
            self.fig.canvas.draw_idle()

# Запуск програми
if __name__ == "__main__":
    data = np.array([
        [5, 9, 4, 3],
        [3, 1, 6, 9],
        [8, 6, 8, 12]
    ])
    
    animator = TurtleAnimator(data)
    plt.show()

import tkinter as tk
from tkinter import messagebox


class GoldKnapsackVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Візуалізація: Золоті зливки (Subset Sum)")

        # Дані прикладу
        self.S = 20
        self.weights = [5, 7, 12, 18]
        self.n = len(self.weights)

        # Стан DP (одновимірний масив)
        self.dp = [False] * (self.S + 1)
        self.dp[0] = True

        # Індекси для покрокового виконання
        self.item_idx = 0
        self.current_j = self.S
        self.is_running = True

        self.setup_ui()

    def setup_ui(self):
        # Панель інформації
        info_frame = tk.Frame(self.root, pady=10)
        info_frame.pack()

        tk.Label(info_frame, text=f"Місткість (S): {self.S}", font=("Arial", 12, "bold")).pack(side=tk.LEFT, padx=20)
        tk.Label(info_frame, text=f"Зливки: {self.weights}", font=("Arial", 12)).pack(side=tk.LEFT, padx=20)

        # Кнопка кроку
        self.btn_next = tk.Button(self.root, text="Наступний крок (j--)", command=self.next_step,
                                  bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
        self.btn_next.pack(pady=10)

        # Візуалізація масиву DP
        self.canvas = tk.Canvas(self.root, width=850, height=150, bg="white")
        self.canvas.pack(pady=10)
        self.cells = []
        self.draw_dp_array()

        # Поле пояснень
        self.info_text = tk.Text(self.root, height=40, width=90, font=("Consolas", 10))
        self.info_text.pack(padx=20, pady=10)
        self.log(f"Початок: dp[0] = True (вагу 0 можна набрати завжди).")
        self.log(f"Розглядаємо перший зливок вагою {self.weights[0]}.")

    def draw_dp_array(self):
        self.canvas.delete("all")
        cell_width = 35
        start_x = 50
        y = 50

        for i in range(self.S + 1):
            x = start_x + i * cell_width
            color = "#81C784" if self.dp[i] else "white"
            # Малюємо клітинку
            rect = self.canvas.create_rectangle(x, y, x + cell_width, y + 40, fill=color, outline="black")
            # Текст (T/F або 1/0)
            text_val = "T" if self.dp[i] else "F"
            self.canvas.create_text(x + cell_width / 2, y + 20, text=text_val)
            # Індекс ваги
            self.canvas.create_text(x + cell_width / 2, y + 55, text=str(i), font=("Arial", 8))
            self.cells.append(rect)

    def log(self, message):
        self.info_text.insert(tk.END, message + "\n")
        self.info_text.see(tk.END)

    def next_step(self):
        if self.item_idx >= self.n:
            self.finish_visualization()
            return

        w = self.weights[self.item_idx]
        j = self.current_j

        # Підсвічування поточної перевірки
        self.draw_dp_array()
        x_pos = 50 + j * 35
        self.canvas.create_line(x_pos + 17, 20, x_pos + 17, 45, arrow=tk.LAST, fill="red")  # Стрілка на j

        if j >= w:
            check_val = self.dp[j - w]
            explanation = f"Зливок {w}: Перевіряємо вагу j={j}. Чи можна було набрати {j - w}? {'Так' if check_val else 'Ні'}."

            if check_val and not self.dp[j]:
                self.dp[j] = True
                explanation += f" -> Оновлюємо dp[{j}] = True"
                self.log(explanation)
            else:
                # Не логуємо кожен порожній крок, щоб не засмічувати текст, лише важливі
                if j == self.S or j == w: self.log(explanation)

        # Логіка ітератора
        self.current_j -= 1
        if self.current_j < w:
            self.item_idx += 1
            if self.item_idx < self.n:
                self.current_j = self.S
                self.log(f"--- Беремо наступний зливок: {self.weights[self.item_idx]} ---")
            else:
                self.draw_dp_array()
                self.finish_visualization()

    def finish_visualization(self):
        max_w = 0
        for i in range(self.S, -1, -1):
            if self.dp[i]:
                max_w = i
                break
        self.log(f"\nГОТОВО! Найбільша вага, яку можна зібрати: {max_w}")
        self.btn_next.config(state=tk.DISABLED)
        messagebox.showinfo("Результат", f"Максимальна вага: {max_w}")


if __name__ == "__main__":
    root = tk.Tk()
    app = GoldKnapsackVisualizer(root)
    root.mainloop()
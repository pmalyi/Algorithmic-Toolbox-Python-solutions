import tkinter as tk
from tkinter import messagebox


class HouseRobberVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Візуалізація: Максимальна сума (без сусідніх)")

        # Дані з прикладу Eolymp (або довільні)
        #self.lst = [10, 20, 30, 10, 50]

        self.lst = [4, 11, 10, 2, 1, 8, 5]
        self.n = len(self.lst)
        self.dp = []

        # Стан візуалізації
        self.step = 0

        self.setup_ui()

    def setup_ui(self):
        # Панель даних
        header = tk.Frame(self.root, pady=10)
        header.pack()

        tk.Label(header, text=f"Елементи (A): {self.lst}", font=("Arial", 12, "bold")).pack()
        tk.Label(header, text=f"Кількість (n): {self.n}", font=("Arial", 10)).pack()

        # Кнопка кроку
        self.btn_next = tk.Button(self.root, text="Наступний крок", command=self.next_step,
                                  bg="#2196F3", fg="white", font=("Arial", 10, "bold"), pady=5)
        self.btn_next.pack(pady=5)

        # Контейнер для візуалізації масивів
        self.canvas = tk.Canvas(self.root, width=600, height=180, bg="white")
        self.canvas.pack(pady=10)

        self.draw_initial_state()

        # Поле пояснень
        self.info_text = tk.Text(self.root, height=30, width=70, font=("Consolas", 10))
        self.info_text.pack(padx=20, pady=10)
        self.log("Програма готова. Натисніть 'Наступний крок'.")

    def draw_initial_state(self):
        self.canvas.delete("all")
        # Малюємо мітки масивів
        self.canvas.create_text(50, 50, text="Масив A:", font=("Arial", 10, "bold"))
        self.canvas.create_text(50, 120, text="Масив DP:", font=("Arial", 10, "bold"))

        for i in range(self.n):
            # Клітинки масиву A
            x0, y0 = 100 + i * 60, 30
            self.canvas.create_rectangle(x0, y0, x0 + 50, y0 + 40, outline="black", tags=f"a_{i}")
            self.canvas.create_text(x0 + 25, y0 + 20, text=str(self.lst[i]))
            self.canvas.create_text(x0 + 25, y0 + 50, text=f"i={i}", fill="gray")

            # Клітинки масиву DP (порожні)
            x1, y1 = 100 + i * 60, 100
            self.canvas.create_rectangle(x1, y1, x1 + 50, y1 + 40, outline="black", dash=(2, 2), tags=f"dp_{i}")

    def log(self, message):
        self.info_text.insert(tk.END, message + "\n")
        self.info_text.see(tk.END)

    def next_step(self):
        if self.step >= self.n:
            self.log("Обчислення завершено!")
            self.log(f"Максимальна сума: {self.dp[-1]}")
            self.btn_next.config(state=tk.DISABLED)
            messagebox.showinfo("Результат", f"Максимальна сума: {self.dp[-1]}")
            return

        i = self.step
        x, y = 100 + i * 60, 100

        if i == 0:
            val = self.lst[0]
            self.dp.append(val)
            explanation = f"Крок 0: Перший елемент. dp[0] = A[0] = {val}"
            self.highlight_cell(i, "#FFEB3B")  # Жовтий

        elif i == 1:
            val = max(self.lst[0], self.lst[1])
            self.dp.append(val)
            explanation = f"Крок 1: Обираємо максимум між першим та другим. \nmax({self.lst[0]}, {self.lst[1]}) = {val}"
            self.highlight_cell(i, "#FFEB3B")

        else:
            f_yes = self.dp[i - 2] + self.lst[i]
            f_no = self.dp[i - 1]
            val = max(f_yes, f_no)
            self.dp.append(val)
            verdict = f"  A[{i}] беремо" if f_yes > f_no else f"  A[{i}] не беремо"
            explanation = f"Крок {i}: Вибір для елемента A[{i}] ({self.lst[i]}):\n" \
                          f"  - Взяти A[{i}]: dp[{i - 2}]({self.dp[i - 2]}) + {self.lst[i]} = {f_yes}\n" \
                          f"  - Не брати A[{i}]: dp[{i - 1}]({self.dp[i - 1]})\n" \
                          f"  - dp[{i}] = max({f_yes}, {f_no}) = {val}\n" + verdict

            # explanation = f"A[{i}] беремо" if f_yes > f_no else f"A[{i}] не беремо"
            self.highlight_cell(i, "#81C784")  # Зелений

        # Малюємо значення в DP
        self.canvas.create_text(x + 25, y + 20, text=str(val), font=("Arial", 10, "bold"), fill="blue")
        self.log(explanation)
        self.step += 1

    def highlight_cell(self, i, color):
        # Очищення попередніх підсвічувань
        for k in range(self.n):
            self.canvas.itemconfig(f"dp_{k}", fill="white")
        self.canvas.itemconfig(f"dp_{i}", fill=color)


if __name__ == "__main__":
    root = tk.Tk()
    app = HouseRobberVisualizer(root)
    root.mainloop()
import tkinter as tk
from tkinter import messagebox


class KnapsackVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Візуалізація задачі: Дискретний рюкзак")

        # Дані прикладу
        #self.S = 10
        #self.weights = [6, 5, 5, 3, 1]
        #self.costs = [10, 8, 8, 2, 3]
        #self.n = len(self.weights)

        self.S = 6
        self.weights = [2, 4, 1, 2]
        self.costs = [7, 2, 5, 1]
        self.n = len(self.weights)

        # DP таблиця
        self.dp = [[0] * (self.S + 1) for _ in range(self.n + 1)]

        # Стан візуалізації
        self.current_i = 1
        self.current_j = 0
        self.phase = "FILL"  # FILL або BACKTRACK
        self.backtrack_i = self.n
        self.backtrack_j = self.S
        self.selected_items = []

        self.setup_ui()

    def setup_ui(self):
        # Панель керування
        control_frame = tk.Frame(self.root)
        control_frame.pack(pady=10)

        # Загальний контейнер для інформації про рюкзак
        header_frame = tk.Frame(self.root, pady=10)
        header_frame.pack()

        # Напис із місткістю рюкзака
        tk.Label(header_frame, text=f"Місткість рюкзака (S): {self.S}",
                 font=("Arial", 10, "bold"), fg="#2E7D32").pack(side=tk.LEFT, padx=20)

        # Можна також додати інформацію про кількість предметів
        tk.Label(header_frame, text=f"Кількість предметів (n): {self.n}",
                 font=("Arial", 10, "bold"), fg="#2E7D32").pack(side=tk.LEFT, padx=20)

        self.btn_next = tk.Button(control_frame, text="Next Step", command=self.next_step, bg="#4CAF50", fg="white",
                                  font=("Arial", 10, "bold"))
        self.btn_next.pack(side=tk.LEFT, padx=5)

        # Таблиця DP
        self.table_frame = tk.Frame(self.root)
        self.table_frame.pack(padx=20, pady=10)
        self.cells = {}

        # Заголовки стовпців (вага)
        for j in range(self.S + 1):
            lbl = tk.Label(self.table_frame, text=f"вага: {j}", width=8, relief="ridge", bg="#f0f0f0")
            lbl.grid(row=0, column=j + 1)

        # Заголовки рядків (предмети)
        for i in range(self.n + 1):
            prefix = f"Пр. {i} вага: {self.weights[i - 1]}, вартість: {self.costs[i - 1]}" if i > 0 else "0"
            lbl = tk.Label(self.table_frame, text=prefix, width=26, relief="ridge", bg="#f0f0f0")
            lbl.grid(row=i + 1, column=0)

            for j in range(self.S + 1):
                cell = tk.Label(self.table_frame, text="0", width=8, relief="sunken", bg="white")
                cell.grid(row=i + 1, column=j + 1)
                self.cells[(i, j)] = cell

        # Поле пояснень
        self.info_text = tk.Text(self.root, height=40, width=120, font=("Consolas", 10))
        self.info_text.pack(padx=20, pady=10)
        self.log("Програма готова. Натисніть 'Next Step' для початку заповнення таблиці.")

    def log(self, message):
        self.info_text.insert(tk.END, message + "\n")
        self.info_text.see(tk.END)

    def next_step(self):
        if self.phase == "FILL":
            self.step_fill()
        elif self.phase == "BACKTRACK":
            self.step_backtrack()

    def step_fill(self):
        i, j = self.current_i, self.current_j

        # Скидання кольору попередньої клітинки
        if j > 0:
            self.cells[(i, j - 1)].config(bg="white")
        elif i > 1:
            self.cells[(i - 1, self.S)].config(bg="white")

        weight = self.weights[i - 1]
        value = self.costs[i - 1]

        # Логіка обчислення
        self.cells[(i, j)].config(bg="#FFF59D")  # Підсвічуємо поточну

        if weight > j:
            self.dp[i][j] = self.dp[i - 1][j]
            explanation = f"Крок (i = {i}, j = {j}): Предмет {i} (вага {weight}) заважкий для рюкзака {j}. Беремо значення зверху dp[i - 1][j]: {self.dp[i - 1][j]}"
        else:
            val_not_take = self.dp[i - 1][j]
            val_take = value + self.dp[i - 1][j - weight]
            self.dp[i][j] = max(val_not_take, val_take)
            explanation = f"Крок (i = {i}, j = {j}): Предмет {i} (вага {weight}, ціна {value}) вміщується.\n" \
                          f"   - Не беремо dp[i - 1][j]: {val_not_take}\n" \
                          f"   - Беремо вартість[i - 1]({value}) + dp[i - 1][j - вага({weight})]: {value} + dp[{i - 1}][{j - weight}]({self.dp[i - 1][j - weight]}) = {val_take}\n" \
                          f"   - Результат: max({val_not_take}, {val_take}) = {self.dp[i][j]}"

        self.cells[(i, j)].config(text=str(self.dp[i][j]))
        self.log(explanation)

        # Перехід до наступної клітинки
        self.current_j += 1
        if self.current_j > self.S:
            self.current_j = 0
            self.current_i += 1

        if self.current_i > self.n:
            self.phase = "BACKTRACK"
            self.log("\nТаблицю заповнено! Починаємо Backtracking (відновлення шляху)...")
            self.cells[(self.n, self.S)].config(bg="#81C784")

    def step_backtrack(self):
        i, j = self.backtrack_i, self.backtrack_j

        if i <= 0:
            res_select = self.selected_items[::-1]
            self.log(f"\nРезультат: Предмети № {res_select}")
            total_weight = 0
            for item in res_select:
                self.log(f"\tПредмет {item}: вага - {self.weights[item - 1]}, вартість - {self.costs[item - 1]}")
                total_weight += self.weights[item - 1]
            self.log(f"\tСумарна вартість рюкзака: {self.dp[self.n][self.S]}")
            self.log(f"\tСумарна вага рюкзака: {total_weight}")
            self.btn_next.config(state=tk.DISABLED)
            messagebox.showinfo("Готово", f"Оптимальний набір предметів: {self.selected_items[::-1]}")
            return

        current_val = self.dp[i][j]
        prev_val = self.dp[i - 1][j]

        self.cells[(i, j)].config(bg="#81C784")

        if current_val != prev_val:
            self.selected_items.append(i)
            weight_used = self.weights[i - 1]
            self.log(
                f"Backtrack: dp[{i}][{j}] != dp[{i - 1}][{j}]. Предмет {i} БУВ взятий. Вага зменшується: {j} - {weight_used} = {j - weight_used}")
            self.backtrack_j -= weight_used
        else:
            self.log(f"Backtrack: dp[{i}][{j}] == dp[{i - 1}][{j}]. Предмет {i} НЕ брався. Переходимо вгору.")

        self.backtrack_i -= 1


if __name__ == "__main__":
    root = tk.Tk()
    app = KnapsackVisualizer(root)
    root.mainloop()
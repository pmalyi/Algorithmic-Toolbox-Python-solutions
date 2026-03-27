import tkinter as tk
from tkinter import messagebox


class LCSVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Візуалізація: Найдовша спільна підпослідовність (LCS)")

        # Дані прикладу
        self.A = [3, 1, 3, 2, 7, 4, 8, 2]
        self.B = [6, 5, 1, 2, 3, 4]
        self.n = len(self.A)
        self.m = len(self.B)

        # DP таблиця
        self.dp = [[0] * (self.m + 1) for _ in range(self.n + 1)]

        # Стан візуалізації
        self.phase = "FILL"  # FILL або BACKTRACK
        self.curr_i = 1
        self.curr_j = 1
        self.bt_i = self.n
        self.bt_j = self.m
        self.lcs_result = []

        self.setup_ui()

    def setup_ui(self):
        # Панель керування
        control_frame = tk.Frame(self.root, pady=10)
        control_frame.pack()

        self.btn_next = tk.Button(control_frame, text="Наступний крок", command=self.next_step,
                                  bg="#2196F3", fg="white", font=("Arial", 10, "bold"))
        self.btn_next.pack(side=tk.LEFT, padx=10)

        tk.Label(control_frame, text="A: " + str(self.A), fg="blue").pack(side=tk.LEFT)
        tk.Label(control_frame, text="  |  B: " + str(self.B), fg="green").pack(side=tk.LEFT)

        # Таблиця
        self.table_frame = tk.Frame(self.root, padx=20, pady=10)
        self.table_frame.pack()
        self.cells = {}

        # Заголовки (Масив B)
        for j in range(self.m + 1):
            val = self.B[j - 1] if j > 0 else "Ø"
            tk.Label(self.table_frame, text=val, width=4, relief="ridge", bg="#e8f5e9").grid(row=0, column=j + 1)

        # Заголовки (Масив A) та Клітинки
        for i in range(self.n + 1):
            val = self.A[i - 1] if i > 0 else "Ø"
            tk.Label(self.table_frame, text=val, width=4, relief="ridge", bg="#e3f2fd").grid(row=i + 1, column=0)
            for j in range(self.m + 1):
                cell = tk.Label(self.table_frame, text="0", width=4, relief="sunken", bg="white")
                cell.grid(row=i + 1, column=j + 1)
                self.cells[(i, j)] = cell

        # Поле пояснень
        self.info_text = tk.Text(self.root, height=50, width=80, font=("Consolas", 10))
        self.info_text.pack(padx=20, pady=10)
        self.log("Початок: Таблиця ініціалізована нулями. Натисніть 'Наступний крок'.")

    def log(self, message):
        self.info_text.insert(tk.END, message + "\n")
        self.info_text.see(tk.END)

    def next_step(self):
        if self.phase == "FILL":
            self.step_fill()
        elif self.phase == "BACKTRACK":
            self.step_backtrack()

    def step_fill(self):
        i, j = self.curr_i, self.curr_j

        # Скидання кольору попередньої клітинки
        self.cells[(i, j)].config(bg="#fff9c4")  # Жовтий - поточна

        char_a = self.A[i - 1]
        char_b = self.B[j - 1]

        if char_a == char_b:
            self.dp[i][j] = self.dp[i - 1][j - 1] + 1
            expl = f"dp[{i}][{j}]: Елементи збігаються ({char_a} == {char_b}). Беремо діагональ + 1: {self.dp[i - 1][j - 1]} + 1 = {self.dp[i][j]}"
        else:
            if self.dp[i - 1][j] >= self.dp[i][j - 1]:
                self.dp[i][j] = self.dp[i - 1][j]
                expl = f"dp[{i}][{j}]: {char_a} != {char_b}. Беремо максимум зверху: {self.dp[i - 1][j]}"
            else:
                self.dp[i][j] = self.dp[i][j - 1]
                expl = f"dp[{i}][{j}]: {char_a} != {char_b}. Беремо максимум зліва: {self.dp[i][j - 1]}"

        self.cells[(i, j)].config(text=str(self.dp[i][j]))
        self.log(expl)

        # Логіка ітерації
        self.curr_j += 1
        if self.curr_j > self.m:
            self.curr_j = 1
            self.curr_i += 1

        if self.curr_i > self.n:
            self.phase = "BACKTRACK"
            self.log("\nТаблицю заповнено! Починаємо відновлення послідовності (з кінця).")

    def step_backtrack(self):
        i, j = self.bt_i, self.bt_j

        if i == 0 or j == 0:
            result = self.lcs_result[::-1]
            self.log(f"\nГОТОВО! Довжина: {self.dp[self.n][self.m]}. Послідовність: {result}")
            messagebox.showinfo("Результат", f"LCS: {result}")
            self.btn_next.config(state=tk.DISABLED)
            return

        self.cells[(i, j)].config(bg="#c8e6c9")  # Зелений - шлях відновлення

        if self.A[i - 1] == self.B[j - 1]:
            self.lcs_result.append(self.A[i - 1])
            self.log(f"Backtrack: A[{i - 1}] == B[{j - 1}] ({self.A[i - 1]}). Додаємо в результат, йдемо по діагоналі.")
            self.bt_i -= 1
            self.bt_j -= 1
        elif self.dp[i - 1][j] >= self.dp[i][j - 1]:
            self.log(f"Backtrack: Значення зверху ({self.dp[i - 1][j]}) >= значення зліва. Йдемо вгору.")
            self.bt_i -= 1
        else:
            self.log(f"Backtrack: Значення зліва більше. Йдемо вліво.")
            self.bt_j -= 1


if __name__ == "__main__":
    root = tk.Tk()
    app = LCSVisualizer(root)
    root.mainloop()
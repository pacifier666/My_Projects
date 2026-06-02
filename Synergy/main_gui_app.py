import tkinter as tk
from tkinter import messagebox
import random
import math

# ==================== ФАКТОРИАЛ ====================
class FactorialApp:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Вычисление факториала")
        self.window.geometry("400x200")
        self.window.resizable(False, False)

        tk.Label(self.window, text="Введите положительное целое число:", font=("Arial", 12)).pack(pady=10)
        self.entry = tk.Entry(self.window, font=("Arial", 12), width=20)
        self.entry.pack(pady=5)
        self.entry.bind("<Return>", lambda event: self.calculate())

        self.btn_calc = tk.Button(self.window, text="Вычислить факториал", command=self.calculate, bg="lightblue", font=("Arial", 10))
        self.btn_calc.pack(pady=10)

        self.label_result = tk.Label(self.window, text="", font=("Arial", 11), fg="green")
        self.label_result.pack(pady=5)

    def calculate(self):
        value = self.entry.get().strip()
        if not value:
            messagebox.showerror("Ошибка", "Поле не может быть пустым")
            return
        try:
            num = int(value)
        except ValueError:
            messagebox.showerror("Ошибка", "Введите целое число")
            return
        if num < 0:
            messagebox.showerror("Ошибка", "Число должно быть положительным")
            return
        result = math.factorial(num)
        self.label_result.config(text=f"{num}! = {result}")

# ==================== ИГРА "УГАДАЙ ЧИСЛО" ====================
class GuessGame:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Угадай число")
        self.window.geometry("450x350")
        self.window.resizable(False, False)

        self.secret = random.randint(1, 100)
        self.max_attempts = 10
        self.attempts = 0

        # Интерфейс
        tk.Label(self.window, text="Игра «Угадай число»", font=("Arial", 14, "bold")).pack(pady=5)
        tk.Label(self.window, text="Я загадал число от 1 до 100. У вас 10 попыток.", font=("Arial", 10)).pack()
        self.label_status = tk.Label(self.window, text=f"Попытка {self.attempts+1} из {self.max_attempts}", font=("Arial", 10))
        self.label_status.pack(pady=5)

        tk.Label(self.window, text="Ваше предположение:").pack()
        self.entry = tk.Entry(self.window, font=("Arial", 12), width=10)
        self.entry.pack(pady=5)
        self.entry.bind("<Return>", lambda event: self.check_guess())

        self.btn_guess = tk.Button(self.window, text="Угадать", command=self.check_guess, bg="lightgreen")
        self.btn_guess.pack(pady=5)

        self.label_hint = tk.Label(self.window, text="", font=("Arial", 10), fg="blue")
        self.label_hint.pack(pady=5)

        self.label_history = tk.Label(self.window, text="", font=("Arial", 9), justify="left", fg="gray")
        self.label_history.pack(pady=5)

        self.btn_new = tk.Button(self.window, text="Новая игра", command=self.new_game, bg="orange")
        self.btn_new.pack(pady=5)

    def check_guess(self):
        if self.attempts >= self.max_attempts:
            messagebox.showinfo("Игра окончена", f"Попытки закончились. Загаданное число: {self.secret}")
            return

        value = self.entry.get().strip()
        if not value:
            messagebox.showerror("Ошибка", "Введите число")
            return
        try:
            guess = int(value)
        except ValueError:
            messagebox.showerror("Ошибка", "Введите целое число")
            return
        if guess < 1 or guess > 100:
            messagebox.showerror("Ошибка", "Число должно быть от 1 до 100")
            return

        self.attempts += 1
        self.label_status.config(text=f"Попытка {self.attempts} из {self.max_attempts}")

        if guess == self.secret:
            messagebox.showinfo("Победа!", f"Поздравляю! Вы угадали число {self.secret} за {self.attempts} попыток.")
            self.new_game()
        elif guess < self.secret:
            self.label_hint.config(text="Слишком маленькое число", fg="red")
            self.update_history(guess, "мало")
        else:
            self.label_hint.config(text="Слишком большое число", fg="red")
            self.update_history(guess, "много")

        if self.attempts >= self.max_attempts and guess != self.secret:
            messagebox.showinfo("Игра окончена", f"Попытки закончились. Загаданное число: {self.secret}")
            self.new_game()

        self.entry.delete(0, tk.END)
        self.entry.focus()

    def update_history(self, guess, hint):
        current = self.label_history.cget("text")
        if current:
            current += f"\n{guess} – {hint}"
        else:
            current = f"{guess} – {hint}"
        self.label_history.config(text=current)

    def new_game(self):
        self.secret = random.randint(1, 100)
        self.attempts = 0
        self.label_status.config(text=f"Попытка 1 из {self.max_attempts}")
        self.label_hint.config(text="")
        self.label_history.config(text="")
        self.entry.delete(0, tk.END)
        messagebox.showinfo("Новая игра", "Новая игра начата! Загадано новое число.")

# ==================== ГЛАВНОЕ ОКНО ====================
class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Мини-приложения")
        self.root.geometry("350x250")
        self.root.resizable(False, False)

        tk.Label(root, text="Выберите приложение", font=("Arial", 16, "bold")).pack(pady=20)

        btn_fact = tk.Button(root, text="Вычислить факториал", command=self.open_factorial,
                             bg="lightblue", font=("Arial", 12), width=20, height=2)
        btn_fact.pack(pady=10)

        btn_game = tk.Button(root, text="Игра «Угадай число»", command=self.open_game,
                             bg="lightgreen", font=("Arial", 12), width=20, height=2)
        btn_game.pack(pady=10)

        btn_exit = tk.Button(root, text="Выход", command=root.quit,
                             bg="lightcoral", font=("Arial", 12), width=20, height=1)
        btn_exit.pack(pady=20)

    def open_factorial(self):
        FactorialApp(self.root)

    def open_game(self):
        GuessGame(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
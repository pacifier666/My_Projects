import math

def calculate_factorial(n: int) -> int:
    """Вычисляет факториал числа n с использованием math.factorial."""
    return math.factorial(n)

def get_positive_integer() -> int:
    """Запрашивает у пользователя положительное целое число с обработкой ошибок."""
    while True:
        user_input = input("Введите положительное целое число: ").strip()
        try:
            number = int(user_input)
            if number < 0:
                print("Ошибка: число должно быть положительным. Попробуйте снова.")
                continue
            return number
        except ValueError:
            print("Ошибка: введите корректное целое число. Попробуйте снова.")

def main():
    print("=== Вычисление факториала ===")
    number = get_positive_integer()
    result = calculate_factorial(number)
    print(f"Факториал числа {number} равен {result}")

if __name__ == "__main__":
    main()
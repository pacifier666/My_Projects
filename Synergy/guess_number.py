import random
import sys

def get_valid_guess(min_val: int, max_val: int) -> int:
    """Запрашивает у пользователя число в заданном диапазоне с проверкой."""
    while True:
        user_input = input(f"Ваше предположение (от {min_val} до {max_val}): ").strip()
        if user_input.lower() in ('выход', 'quit', 'exit'):
            print("Игра завершена досрочно.")
            sys.exit(0)
        try:
            guess = int(user_input)
            if guess < min_val or guess > max_val:
                print(f"Ошибка: число должно быть в диапазоне [{min_val}, {max_val}].")
                continue
            return guess
        except ValueError:
            print("Ошибка: введите целое число.")

def play_game():
    min_num, max_num = 1, 100
    secret_number = random.randint(min_num, max_num)
    max_attempts = 10
    attempts = 0

    print("\n=== Игра 'Угадай число' ===")
    print(f"Я загадал число от {min_num} до {max_num}. У вас {max_attempts} попыток.")
    print("Введите 'выход' для досрочного завершения.")

    while attempts < max_attempts:
        remaining = max_attempts - attempts
        print(f"\nПопытка {attempts + 1} из {max_attempts}. Осталось попыток: {remaining}")
        guess = get_valid_guess(min_num, max_num)
        attempts += 1

        if guess == secret_number:
            print(f"Поздравляю! Вы угадали число {secret_number} за {attempts} попыток!")
            return
        elif guess < secret_number:
            print("Слишком маленькое число.")
        else:
            print("Слишком большое число.")

    print(f"\nК сожалению, попытки закончились. Загаданное число было {secret_number}.")

def main():
    while True:
        play_game()
        again = input("\nХотите сыграть ещё раз? (да/нет): ").strip().lower()
        if again not in ('да', 'yes', 'д', 'y'):
            print("Спасибо за игру!")
            break

if __name__ == "__main__":
    main()
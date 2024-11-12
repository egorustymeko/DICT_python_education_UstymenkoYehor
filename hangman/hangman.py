import random  # Импорт модуля для случайного выбора

# Список возможных слов для угадывания
WORDS = ['python', 'java', 'javascript', 'php']

# Константа для максимального числа ошибок
MAX_ERRORS = 8

# Приветствие игрока
def greet():
    print("HANGMAN")
    print("The game will be available soon.")

# Функция выбирает случайное слово из списка

def choose_word():
    return random.choice(WORDS)

# Функция отображает подсказку — первые 3 буквы слова, остальные заменены на "-"
def display_hint(word):
    hint = word[:3] + '-' * (len(word) - 3)
    print(f"Guess the word {hint}: ")

# Функция для получения корректной буквы от пользователя, проверяет на длину и уникальность
def get_valid_letter(guessed_letters):
    while True:
        letter = input("Input a letter: ").lower()
        if len(letter) != 1:
            print("You should input a single letter")  # Сообщение об ошибке длины ввода
        elif not letter.isalpha() or not letter.islower():
            print("Please enter a lowercase English letter")  # Проверка на корректность ввода
        elif letter in guessed_letters:
            print("You've already guessed this letter")
        else:
            return letter  # Возвращает валидную букву

# Основная версия игры с использованием максимального количества ошибок
def play_game():
    word = choose_word()
    guessed_letters = set()
    display_word = '-' * len(word)
    errors = 0
    print(display_word)

    # Цикл для угадывания букв с ограничением по числу ошибок
    while errors < MAX_ERRORS and '-' in display_word:
        letter = get_valid_letter(guessed_letters)  # Используем функцию проверки ввода
        if letter in word:
            display_word = ''.join([letter if word[i] == letter else display_word[i] for i in range(len(word))])
            guessed_letters.add(letter)
            print(display_word)
        else:
            print("That letter doesn't appear in the word")
            errors += 1
        print(f"Attempts remaining: {MAX_ERRORS - errors}")

    # Проверка победы или поражения
    if '-' not in display_word:
        print("You survived!")
    else:
        print("You lost!")

# Основное меню, предлагает начать игру или выйти из программы
def mainmenu():
    while True:
        choice = input('Type "play" to play the game, "exit" to quit: ').strip().lower()

        if choice == "play":
            play_game()  # Запуск игры
        elif choice == "exit":
            print("Thanks for playing!")  # Сообщение о завершении игры
            break  # Завершение программы
        else:
            print("Invalid choice. Please type 'play' or 'exit'.")  # Сообщение о некорректном вводе

# Запуск программы
if __name__ == "__main__":
    greet()  # Вывод приветственного сообщения
    mainmenu()  # Переход к главному меню

import random

# Функція для введення кількості олівців з перевіркою правильності
def get_initial_pencils():
    """
    Запитує у користувача кількість олівців.
    Перевіряє, чи введене значення є додатнім числом.
    """
    while True:
        print("How many pencils would you like to use:")
        num = input()
        if not num.isdigit() or int(num) <= 0:
            if not num.isdigit() or (num.startswith('-') and num[1:].isdigit()):
                print("The number of pencils should be numeric")
            else:
                print("The number of pencils should be positive")
        else:
            return int(num)

# Функція для вибору гравця, який ходить першим
def choose_first_player(player1, player2):
    """
    Запитує у користувача, хто ходить першим — один з двох імен.
    """
    print(f"Who will be the first ({player1}, {player2}):")
    while True:
        first = input()
        if first in (player1, player2):
            return first
        else:
            print(f"Choose between '{player1}' and '{player2}'")

# Функція для виводу поточної кількості олівців
def print_pencils(count):
    """
    Виводить вертикальні смужки, що представляють олівці.
    """
    print('|' * count)

def switch_player(current, player1, player2):
    """
    Змінює активного гравця.
    """
    return player2 if current == player1 else player1

def get_player_move(pencils_left):
    """
    Запитує хід користувача.
    Перевіряє, чи введено 1, 2 або 3, і чи можна взяти стільки олівців.
    """
    while True:
        move = input()
        if move not in ['1', '2', '3']:
            print("Possible values: '1', '2' or '3'")
        elif int(move) > pencils_left:
            print("Too many pencils were taken")
        else:
            return int(move)

def bot_move(pencils_left):
    """
    Визначає хід бота згідно з виграшною стратегією:
    - якщо позиція виграшна — бот ставить суперника в програшну;
    - інакше — бере випадкову кількість олівців.
    """
    if pencils_left % 4 == 0:
        return 3
    elif pencils_left % 4 == 3:
        return 2
    elif pencils_left % 4 == 2:
        return 1
    else:
        return random.randint(1, min(3, pencils_left))

# Головна частина програми

# Імена гравців
player1 = "John"
player2 = "Jack"  # бот

# Отримання кількості олівців та першого гравця
pencils = get_initial_pencils()
current_player = choose_first_player(player1, player2)

# Вивід початкового стану гри
print_pencils(pencils)
print(f"{current_player} is going first!")

# Основний цикл гри
while pencils > 0:
    print(f"{current_player}'s turn:")

    if current_player == player2:
        move = bot_move(pencils)
        print(move)
    else:
        move = get_player_move(pencils)

    pencils -= move

    if pencils == 0:
        # Перемога гравця, який не взяв останній олівець
        winner = switch_player(current_player, player1, player2)
        print(f"{winner} won!")
        break
    else:
        print_pencils(pencils)
        current_player = switch_player(current_player, player1, player2)
def show_initial_grid():
    """Виводить початкове ігрове поле без форматування"""
    print("X O X")
    print("O X O")
    print("X X O")

def print_formatted_grid(cells):
    """
    Виводить ігрове поле з форматуванням

    Args:
        cells (str): Рядок з 9 символів (X, O, _)
    """
    print("---------")
    for i in range(0, 9, 3):
        row = cells[i:i + 3]
        print(f"| {' '.join(row.replace('_', ' '))} |")
    print("---------")


def demo_formatted_grid():
    """Демонструє роботу функції форматування поля"""
    cells = input("Enter cells: ")
    print_formatted_grid(cells.upper())

def analyze_game_state(cells):
    """
    Аналізує стан гри

    Returns:
        str: Результат аналізу (X wins, O wins, Draw тощо)
    """
    x_count = cells.count('X')
    o_count = cells.count('O')
    if abs(x_count - o_count) > 1:
        return "Impossible"

    lines = [
        cells[0:3], cells[3:6], cells[6:9],
        cells[0] + cells[3] + cells[6],
        cells[1] + cells[4] + cells[7],
        cells[2] + cells[5] + cells[8],
        cells[0] + cells[4] + cells[8],
        cells[2] + cells[4] + cells[6]
    ]

    x_wins = any(line == "XXX" for line in lines)
    o_wins = any(line == "OOO" for line in lines)

    if x_wins and o_wins:
        return "Impossible"
    elif x_wins:
        return "X wins"
    elif o_wins:
        return "O wins"
    elif '_' in cells:
        return "Game not finished"
    else:
        return "Draw"

def demo_game_analysis():
    """Демонструє аналіз стану гри"""
    cells = input("Enter cells: ")
    print_formatted_grid(cells.upper())
    print(analyze_game_state(cells.upper()))

def get_player_coordinates():
    """
    Отримує координати від гравця з валідацією

    Returns:
        tuple: (x, y) coordinates (1-3)
    """
    while True:
        coords = input("Enter the coordinates: ").split()
        if len(coords) != 2:
            print("You should enter numbers!")
            continue

        x, y = coords
        if not (x.isdigit() and y.isdigit()):
            print("You should enter numbers!")
            continue

        x, y = int(x), int(y)
        if not (1 <= x <= 3 and 1 <= y <= 3):
            print("Coordinates should be from 1 to 3!")
            continue

        return x, y

def demo_player_moves():
    """Демонструє механізм ходів гравця"""
    cells = input("Enter cells: ").upper()
    print_formatted_grid(cells)

    while True:
        x, y = get_player_coordinates()
        index = (x - 1) + (3 - y) * 3

        if cells[index] != '_':
            print("This cell is occupied! Choose another one!")
            continue

        cells = cells[:index] + 'X' + cells[index + 1:]
        print_formatted_grid(cells)
        break

def play_full_game():
    """Запускає повноцінну гру для двох гравців"""
    cells = "_________"
    current_player = 'X'

    print_formatted_grid(cells)

    while True:
        print(f"Player {current_player}'s turn")

        while True:
            try:
                x, y = get_player_coordinates()
                index = (x - 1) + (3 - y) * 3

                if cells[index] != '_':
                    print("This cell is occupied! Choose another one!")
                    continue

                cells = cells[:index] + current_player + cells[index + 1:]
                break
            except IndexError:
                print("Coordinates should be from 1 to 3!")

        print_formatted_grid(cells)

        result = analyze_game_state(cells)
        if result in ["X wins", "O wins", "Draw"]:
            print(result)
            break

        current_player = 'O' if current_player == 'X' else 'X'

def main():
    """Головна функція для запуску різних демонстрацій"""
    print("\nFull Game")
    play_full_game()

if __name__ == "__main__":
    main()
def greet():
    print("*******************")
    print(" Добро пожаловать  ")
    print("      в игру       ")
    print(" КРЕСТИКИ - НОЛИКИ ")
    print("*******************")
    print(" вводим координаты: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")


def show():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()


def ask():
    while True:
        coords = input(" Ваш ход: ").split()

        if len(coords) != 2:
            print(" Введите 2 координаты... ")
            continue

        x, y = coords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа... ")
            continue

        x, y = int(x), int(y)

        if not (0 <= x <= 2 and 0 <= y <= 2):
            print(" Координаты вне диапазона... ")
            continue

        if field[x][y] != " ":
            print(" Выберите другую клетку...")
            continue

        return x, y


def check_win():
    win_coord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                 ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
                 ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)))
    for coord in win_coord:
        symbols = []
        for c in coord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Крестик выиграл!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Нолик выиграл!")
            return True
    return False


greet()
field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print(" Ничья!")

        break

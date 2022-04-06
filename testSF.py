field = [['-'] * 3 for _ in range(3)]
def show():
    print('  0 1 2')
    for i in range(len(field)):
        print(str(i), *field[i])

def ask_input():
    while True:
        cage = input('Введите координаты :').split()
        if len(cage) !=2:
            print('Введите две координаты')
            continue
        if not(cage[0].isdigit() and cage[1].isdigit()):
            print('Введите числа')
            continue
        x, y =map(int,cage)
        if 0 >= x and x > 2 or 0 >= y and y > 2:
            print('Координаты вне диапозона')
            continue
        if field[x][y] != '-':
            print('Клетка занята')
            continue
        break
        return x,y

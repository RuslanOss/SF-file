field = [['-'] * 3 for _ in range(3)]
def show(field):
    print('  0 1 2')
    for i in range(len(field)):
        print(str(i), *field[i])

def ask_input(f,user):
    while True:
        cage = input(f"Ходит {user} .Введите координаты:").split()
        if len(cage) != 2:
            print('Введите две координаты')
            continue
        if not(cage[0].isdigit() and cage[1].isdigit()):
            print('Введите числа')
            continue
        x, y = map(int, cage)
        if 0 >= x and x > 2 or 0 >= y and y > 2:
            print('Координаты вне диапозона')
            continue
        if field[x][y] != '-':
            print('Клетка занята')
            continue
        break
    return x,y

def win_position(f,user):
    f_list = []
    for l in f:
        f_list += l
    positions = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    indices = set([i for i, x in enumerate(f_list) if x == user])
    for p in positions:
        if len(indices.intersection(set(p))) == 3:
            return True
    return False
def start(field):
    count = 0
    while True:
        show(field)
        if count % 2 == 0:
            user = 'x'
        else:
            user = 'o'
        if count < 9:
            x, y = ask_input(field,user)
            field[x][y] = user

        elif count == 9:
            print ('Ничья')
            break
        if win_position(field,user):
            print(f"Выйграл {user}")
            break
        count += 1
start(field)
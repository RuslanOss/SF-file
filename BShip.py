from random import randint


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__ (self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Dot({self.x}, {self.y})"

class BoardException(Exception):
    pass

class BoardOutException(BoardException):
    def __str__(self):
        return "Вы пытаетесь выстрелить за пределы доски"

class BoardUsedException(BoardException):
    def __str__(self):
        return "Вы стреляли в эту точку"

class BoardWrongShipException(BoardException):
    pass

class Ship:
    def __init__(self, bow, l, b):
        self.bow = bow
        self.l = l
        self.b = b
        self.lives = l

    @property
    def dots(self):
        ship_dots = []
        for i in range(self.l):
                cur_x = self.bow.x
                cur_y = self.bow.y
                if self.b == 0:
                    cur_x += i
                elif self.b == 1:
                    cur_y += i
                ship_dots.append(Dot(cur_x, cur_y))
        return ship_dots

    def shooter(self, shot):
        return shot in self.dots


class Board:
    def __init__(self, hid = False, size = 6):
        self.size = size
        self.hid = hid

        self.count = 0

        self.field = [["O"]*size for _ in range(size)]

        self.busy = []
        self.ships = []

    def __str__(self):
       res = " "
       res += " | 1 | 2 | 3 | 4 | 5 | 6 |"
       for i, row in enumerate(self.field):
           res += f"\n{i + 1} | " + " | ".join(row) + " |"
       if self.hid:
           res = res.replace("■", "O")

       return res

    def out(self, d):
        return not ((0 <= d.x < self.size) and (0 <= d.y < self.size))

    def contur(self, ship, verb = False):
      near = [
          (-1, -1), (-1, 0), (-1, 1),
          (0, -1), (0, 0), (0, 1),
          (1,-1), (1, 0), (1, 1)
      ]
      for d in ship.dots:
          for dx, dy in near:
              cur = Dot(d.x + dx, d.y + dy)
              if not(self.out(cur)) and cur not in self.busy:
                 if verb:
                     self.field[cur.x][cur.y] = "-"
                 self.busy.append(cur)

    def add_ship(self, ship):
        for d in ship.dots:
            if self.out(d) or d in self.busy:
                raise BoardWrongShipException()
        for d in ship.dots:
          self.field[d.x][d.y] = "■"
          self.busy.append(d)

        self.ships.append(ship)
        self.contur(ship)

    def shot(self, d):
      if self.out(d):
          raise BoardOutException()

      if d in self.busy:
          raise BoardUsedException()

      self.busy.append(d)

      for ship in self.ships:
          if ship.shooter(d):
              ship.lives -= 1
              self.field[d.x][d.y] = "X"
              if ship.lives == 0:
                  self.count += 1
                  self.contur(ship, verb = True)
                  print("Корабль потоплен")
                  return False
              else:
                  print("Корабль ранен")
                  return True

      self.field[d.x][d.y] = "."
      print("Мимо")
      return False

    def begin(self):
      self.busy = []

class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    def ask(self):
        raise NotImplementedError()

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                return repeat
            except BoardException as e:
                print(e)

class AI(Player):
    def ask(self):
        d = Dot(randint(0, 5), randint(0, 5))
        print(f"Ход компьютера: {d.x+1} {d.y+1}")
        return d

class User(Player):

    def ask(self):

        while True:
            cords = input("Ваш ход: ").split()

            if len(cords) != 2:
                print("Введите две координаты")
                continue
            x, y = cords

            if not (x.isdigit()) or not (y.isdigit()):
                print(" Введите числа! ")
                continue

            x, y = int(x), int(y)

            return Dot(x-1, y-1)

class Game:

    def __init__(self, size = 6):
        self.lens = [3, 2, 2, 1, 1, 1, 1]
        self.size = size
        pl = self.random_board()
        co = self.random_board()
        co.hid = True

        self.ai = AI(co, pl)
        self.us = User(pl, co)

    def greet(self):
        print("---------------------")
        print("  Формат ввода: x  y ")
        print("  x - по вертикали   ")
        print("  y - по горизонтали ")
        print("---------------------")


    def try_board(self):
        board = Board(size = self.size)
        attempts = 0
        for l in self.lens:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(Dot(randint(0, self.size), randint(0, self.size)), l, randint(0,1))
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass

        board.begin()
        return board

    def random_board(self):
        board = None
        while board is None:
            board = self.try_board()
        return board

    def loop(self):
        num = 0
        while True:
            print("-"*20)
            print("Доска пользователя:")
            print(self.us.board)
            print("-" * 20)
            print("Доска компьютера:")
            print(self.ai.board)
            print("-" * 20)
            if num % 2 == 0:
                print("Ходит игрок")
                repeat = self.us.move()
            else:
                print("Ходит компьютер")
                repeat = self.ai.move()
            if repeat:
                num -= 1

            if self.ai.board.count ==7:
                print("-" * 20)
                print("Игрок выйграл!")
                break
            if self.us.board.count == 7:
                print("-" * 20)
                print("Компьютер выйграл!")
                break
            num += 1

    def start(self):
        self.greet()
        self.loop()

g = Game()
g.start()
#Переписал код из вебинара,код красивый понял 30-40% из него# ,но радует что логика понятна,огорчает что путь ее создания еще не дошел до моего базового интелекта,поэтому решил идти путем мышечной памяти и переписывать его из памяти...
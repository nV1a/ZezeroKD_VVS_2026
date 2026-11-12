import random
from copy import deepcopy


class Item:
    def __init__(self, name, item_type, power=0, opens=None):
        self.name = name
        self.item_type = item_type
        self.power = power
        self.opens = opens
        self.en = False

    def __str__(self):
        if self.en:
            return self.name + ' (зачарован)'
        if self.opens:
            return f'{self.name} (от сундука {self.opens[0]} {self.opens[1]})'
        return self.name


class Room:
    def __init__(self, room_type):
        self.room_type = room_type
        self.items = []
        self.v = False
        self.monster_hp = False
        self.hit = False
        self.locked = False
        self.act_trap = True


class Game:
    def __init__(self, size):
        self.size = size
        self.hp = 100
        self.x = 0
        self.y = 0
        self.loot = []
        self.visited_rooms = []
        self.exit_pos = None
        self.running = True
        self.lab = []
        self.generate()

    def generate(self):
        while True:
            self.build_rooms()
            if self.place_items():
                break

    def build_rooms(self):
        room_types = ['empty', 'chest', 'monster', 'trap', 'key', 'portal', 'en', 'finish']
        random_types = ['empty', 'empty', 'empty', 'chest', 'monster', 'trap', 'key', 'portal', 'en']
        coords = [(x, y) for x in range(self.size) for y in range(self.size)]
        coords.remove((0, 0))
        random.shuffle(coords)
        self.lab = [[None for i in range(self.size)] for i in range(self.size)]
        self.lab[0][0] = Room('empty')
        for room_type in room_types[1:]:
            x, y = coords.pop()
            self.lab[x][y] = Room(room_type)
        for x, y in coords:
            self.lab[x][y] = Room(random.choice(random_types))
        for row in self.lab:
            for room in row:
                if room.room_type == 'monster':
                    room.monster_hp = True

    def safe_coords(self):
        found = [(0, 0)]
        queue = [(0, 0)]
        while queue:
            x, y = queue.pop(0)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < self.size and 0 <= ny < self.size:
                    if (nx, ny) not in found and self.lab[nx][ny].room_type != 'monster':
                        found.append((nx, ny))
                        queue.append((nx, ny))
        return found

    def place_items(self):
        safe = self.safe_coords()
        chests = []
        key_rooms = []
        for x in range(self.size):
            for y in range(self.size):
                if self.lab[x][y].room_type == 'chest':
                    chests.append((x, y))
                elif self.lab[x][y].room_type == 'key':
                    key_rooms.append((x, y))
        opened_by = {}
        for key_pos in key_rooms:
            chest_pos = random.choice(chests)
            self.lab[chest_pos[0]][chest_pos[1]].locked = True
            self.lab[key_pos[0]][key_pos[1]].items.append(Item('key', 'key', 0, chest_pos))
            if chest_pos not in opened_by:
                opened_by[chest_pos] = []
            opened_by[chest_pos].append(key_pos)
        good_chests = []
        for chest_pos in chests:
            if chest_pos not in safe:
                continue
            if chest_pos not in opened_by:
                good_chests.append(chest_pos)
            elif any(key_pos in safe for key_pos in opened_by[chest_pos]):
                good_chests.append(chest_pos)
        if not good_chests:
            return False
        possible_items = [Item('potion', 'heal', 30), Item('hint', 'hint')]
        for x, y in chests:
            for i in range(random.randint(0, 3)):
                self.lab[x][y].items.append(deepcopy(random.choice(possible_items)))
        important_items = [
            Item('knife', 'weapon', 5),
            Item('amulet', 'monster_pass'),
            Item('exit_key', 'key'),
            Item('potion', 'heal', 30)
        ]
        for item in important_items:
            x, y = random.choice(good_chests)
            self.lab[x][y].items.append(item)
        return True

    def show_room(self):
        room = self.lab[self.x][self.y]
        print('\n' + '=' * 35)
        print('Комната:', room.room_type)
        print('Координаты:', self.x, self.y)
        print('Здоровье:', self.hp)
        if room.locked:
            print('Сундук заперт.')
        elif room.items:
            print('Предметы в комнате:')
            for i, item in enumerate(room.items):
                print(i, '-', item)
        else:
            print('Предметов в комнате нет.')
        print('=' * 35)

    def find_weapon(self):
        weapons = [item for item in self.loot if item.item_type == 'weapon']
        if not weapons:
            return None
        return min(weapons, key=lambda item: item.power)

    def find_key(self, x, y):
        for item in self.loot:
            if item.opens == (x, y):
                return item
        return None

    def move(self, direction):
        new_x = self.x
        new_y = self.y
        if direction == 'w':
            new_x -= 1
        elif direction == 's':
            new_x += 1
        elif direction == 'a':
            new_y -= 1
        elif direction == 'd':
            new_y += 1
        else:
            print('Неизвестное направление.')
            return
        if new_x < 0 or new_x >= self.size or new_y < 0 or new_y >= self.size:
            print('Нельзя выйти за границу лабиринта!')
            return
        room = self.lab[new_x][new_y]
        if room.room_type == 'monster' and room.monster_hp:
            names = [item.name for item in self.loot]
            weapon = self.find_weapon()
            if 'amulet' in names:
                print('Амулет защищает вас от монстра.')
            elif weapon is None:
                if room.hit:
                    print('Монстр не пускает. Нужен нож или амулет из сундука.')
                else:
                    room.hit = True
                    damage = random.randint(15, 25)
                    self.hp -= damage
                    print('Монстр бьёт вас! Урон:', damage)
                    print('Здоровье:', self.hp)
                    print('Без ножа или амулета сюда не пройти.')
                return
            else:
                self.fight_monster(room, weapon)
                if room.monster_hp or self.hp <= 0:
                    return
        self.x = new_x
        self.y = new_y
        self.enter_room()

    def enter_room(self):
        room = self.lab[self.x][self.y]
        position = (self.x, self.y)
        if position not in self.visited_rooms:
            self.visited_rooms.append(position)
        room.v = True
        print('\nВы вошли в комнату:', room.room_type)
        if room.room_type == 'trap':
            if room.act_trap:
                damage = random.randint(10, 30)
                self.hp -= damage
                room.act_trap = False
                print('Вы попали в ловушку! Урон:', damage)
        elif room.room_type == 'portal':
            self.use_portal()
            return
        elif room.room_type == 'chest':
            self.open_chest(room)
        elif room.room_type == 'key':
            print('Здесь лежит ключ. Нажмите T, чтобы взять его.')
        elif room.room_type == 'en':
            self.enchant_weapon()
        elif room.room_type == 'finish':
            self.try_exit()
            if not self.running:
                return
        self.show_room()

    def open_chest(self, room):
        if room.locked:
            key = self.find_key(self.x, self.y)
            if key is None:
                print('Сундук заперт. Нужен ключ именно от этого сундука.')
                return
            self.loot.remove(key)
            room.locked = False
            print('Вы открыли сундук ключом.')
        if room.items:
            print('В сундуке лежат предметы. Нажмите T, чтобы взять предмет, или G, чтобы взять всё.')
        else:
            print('Сундук пуст.')

    def room_is_closed(self, room):
        if room.room_type == 'chest' and room.locked:
            self.open_chest(room)
            return room.locked
        return False

    def ask_number(self, size):
        answer = input('Введите номер предмета: ')
        if not answer.isdigit():
            print('Нужно ввести номер.')
            return None
        number = int(answer)
        if number >= size:
            print('Такого номера нет.')
            return None
        return number

    def take_item(self):
        room = self.lab[self.x][self.y]
        if self.room_is_closed(room):
            return
        if not room.items:
            print('В комнате нет предметов.')
            return
        print('Предметы в комнате:')
        for i, item in enumerate(room.items):
            print(i, '-', item)
        number = self.ask_number(len(room.items))
        if number is None:
            return
        item = room.items.pop(number)
        self.loot.append(item)
        print('Вы подобрали:', item)

    def take_all(self):
        room = self.lab[self.x][self.y]
        if self.room_is_closed(room):
            return
        if not room.items:
            print('В комнате нет предметов.')
            return
        print('Вы забрали всё:', ', '.join(str(item) for item in room.items))
        self.loot.extend(room.items)
        room.items = []

    def use_portal(self):
        free = []
        for x in range(self.size):
            for y in range(self.size):
                room = self.lab[x][y]
                if (x, y) != (self.x, self.y) and not room.monster_hp and room.room_type != 'portal':
                    free.append((x, y))
        print('Портал переносит вас в случайную комнату.')
        self.x, self.y = random.choice(free)
        self.enter_room()

    def fight_monster(self, room, weapon):
        print('Начинается бой! Нужно ударить:', weapon.power, 'раз.')
        for i in range(weapon.power):
            input('Нажмите Enter, чтобы ударить...')
            print('Удар', i + 1, 'из', weapon.power)
            if not weapon.en:
                damage = random.randint(5, 15)
                self.hp -= damage
                print('Монстр наносит ответный урон:', damage)
                print('Здоровье:', self.hp)
                if self.hp <= 0:
                    return
        room.monster_hp = False
        print('Монстр побеждён!')

    def enchant_weapon(self):
        weapons = [item for item in self.loot if item.item_type == 'weapon' and not item.en]
        if not weapons:
            print('Здесь зачаровывают ножи, но у вас нет незачарованного ножа.')
            return
        print('Можно зачаровать нож.')
        answer = input('Зачаровать? (y/n): ').lower()
        if answer == 'y':
            weapon = weapons[0]
            weapon.en = True
            weapon.power = 3
            print('Нож зачарован! Теперь для победы нужно 3 удара, и монстр не бьёт в ответ.')

    def try_exit(self):
        names = [item.name for item in self.loot]
        if 'exit_key' in names:
            print('У вас есть ключ от выхода!')
            print('ПОБЕДА! Вы выбрались из лабиринта.')
            self.running = False
        else:
            print('Выход заперт. Найдите exit_key.')

    def show_inventory(self):
        print('\n===== ИНВЕНТАРЬ =====')
        if not self.loot:
            print('Инвентарь пуст.')
            return
        for i, item in enumerate(self.loot):
            print(i, '-', item)

    def use_item(self):
        if not self.loot:
            print('Инвентарь пуст.')
            return
        self.show_inventory()
        number = self.ask_number(len(self.loot))
        if number is None:
            return
        item = self.loot[number]
        if item.item_type == 'heal':
            self.hp += item.power
            if self.hp > 100:
                self.hp = 100
            self.loot.remove(item)
            print('Здоровье восстановлено. Сейчас:', self.hp)
        elif item.item_type == 'hint':
            for x in range(self.size):
                for y in range(self.size):
                    if self.lab[x][y].room_type == 'finish':
                        self.exit_pos = (x, y)
            self.loot.remove(item)
            print('Подсказка: выход находится в комнате', self.exit_pos[0], self.exit_pos[1])
            print('Для него нужен exit_key из сундука. Выход отмечен на карте буквой E.')
        else:
            print('Этот предмет сейчас использовать нельзя.')

    def drop_item(self):
        if not self.loot:
            print('Инвентарь пуст.')
            return
        self.show_inventory()
        number = self.ask_number(len(self.loot))
        if number is None:
            return
        item = self.loot.pop(number)
        self.lab[self.x][self.y].items.append(item)
        print('Вы оставили предмет в этой комнате:', item)

    def sort_inventory(self):
        self.loot.sort(key=lambda item: item.name)
        print('Инвентарь отсортирован.')

    def reverse_inventory(self):
        self.loot.reverse()
        print('Порядок предметов изменён на обратный.')

    def search_inventory(self):
        if not self.loot:
            print('Инвентарь пуст.')
            return
        name = input('Введите название предмета: ')
        names = [item.name for item in self.loot]
        if name in names:
            print('Предмет найден. Номер:', names.index(name))
        else:
            print('Такого предмета нет.')

    def copy_inventory(self):
        if not self.loot:
            print('Инвентарь пуст.')
            return
        copied_inventory = self.loot.copy()
        print('Копия инвентаря создана, оригинал не изменится.')
        first_part = copied_inventory[:len(copied_inventory) // 2]
        print('Первая половина копии:')
        for item in first_part:
            print('-', item)

    def show_map(self):
        print('\n========== КАРТА ==========')
        for x in range(self.size):
            for y in range(self.size):
                room = self.lab[x][y]
                if x == self.x and y == self.y:
                    print('P', end=' ')
                elif room.v:
                    print('+', end=' ')
                elif (x, y) == self.exit_pos:
                    print('E', end=' ')
                else:
                    print('#', end=' ')
            print()
        print('P - вы, + - посещённая комната, E - выход, # - неизвестная комната')

    def play(self):
        print('\nВы начинаете в левом верхнем углу.')
        self.visited_rooms.append((0, 0))
        self.lab[0][0].v = True
        self.show_room()
        while self.running and self.hp > 0:
            print('\nЧто хотите сделать?')
            print('W - вверх')
            print('S - вниз')
            print('A - влево')
            print('D - вправо')
            print('T - взять предмет')
            print('G - взять все предметы')
            print('I - инвентарь')
            print('U - использовать предмет')
            print('X - выбросить предмет')
            print('O - сортировать инвентарь')
            print('R - перевернуть инвентарь')
            print('F - найти предмет')
            print('C - копировать инвентарь')
            print('M - карта')
            print('Q - выйти из игры')
            command = input('> ').lower()
            if command in ['w', 'a', 's', 'd']:
                self.move(command)
            elif command == 't':
                self.take_item()
            elif command == 'g':
                self.take_all()
            elif command == 'i':
                self.show_inventory()
            elif command == 'u':
                self.use_item()
            elif command == 'x':
                self.drop_item()
            elif command == 'o':
                self.sort_inventory()
            elif command == 'r':
                self.reverse_inventory()
            elif command == 'f':
                self.search_inventory()
            elif command == 'c':
                self.copy_inventory()
            elif command == 'm':
                self.show_map()
            elif command == 'q':
                print('Вы вышли из игры.')
                self.running = False
            else:
                print('Неизвестная команда.')
        if self.hp <= 0:
            print('\nВы проиграли: здоровье закончилось.')


print('Добро пожаловать в ЛАБИРИНТ!')
while True:
    try:
        size = int(input('Введите размер лабиринта N (минимум 3): '))
        if size >= 3:
            break
        print('Размер должен быть не меньше 3.')
    except ValueError:
        print('Введите целое число.')
game = Game(size)
game.play()

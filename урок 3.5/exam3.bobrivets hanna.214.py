# Задача 1
# def card_hide(card):
#     return '*' * len(card[:-4]) + card[-4:]

# Задача 2
# def palindrome_check(s):
#     for i in range(0, int(len(s)/2)):
#         if s[i] != s[len(s)-i-1]:
#             return "Слово не является палиндромом"
#         return "Слово является палиндромом"
# s = input('Введите слово: ')
# print(palindrome_check(s))

# Задача 3

class Tomato:
    #стадии созревания
    states = {0: 'ничего', 1: 'цветение', 2: 'зеленый', 3: 'красный'}
    def __init__(self, index):
        self._index = index
        self._state = 0

    # Переход к следующей стадии созревания
    def grow(self):
        if self._state < 3:
            self._state += 1

    # Проверка, созрел ли томат
    def is_ripe(self):
        return True if self._state == 3 else False


class TomatoBush:
    # Создаем список из объектов класса Tomato
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(1, num+1)]

    # Переводим все томаты из списка на следующий этап созревания
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    # Проверяем, все ли помидоры созрели
    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    # Собираем урожай
    def give_away_all(self):
        self.tomatoes = []

class Gardener:
    # Выдаем садовнику растение для ухода
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    # Ухаживаем за растением
    def work(self):
        self._plant.grow_all()

    # Собираем урожай
    def harvest(self):
        if self._plant.all_are_ripe():
            print('Урожай собран!')
            self._plant.give_away_all()
        else:
            print('Томаты еще не дозрели')

    # Статический метод

    @staticmethod
    def knowledge_base():
        print('Справка по садоводству:')
        print('1. Не забывайте регулярно поливать и подкармливать растения')
        print('2. Определите правильное расстояние между растениями, чтобы они не мешали друг другу в росте')
        print('3. Удалите поврежденные листья и плоды, чтобы предотвратить распространение болезней')
# Вызов справки по садоводству
Gardener.knowledge_base()
bush = TomatoBush(5)
gardener = Gardener('Jack', bush)
gardener.work()
gardener.work()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
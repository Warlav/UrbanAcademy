import threading
from time import sleep
from random import randint
import queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.queue = queue.Queue(maxsize=len(tables))
        self.tables = [*tables]

    def guest_arrival(self, *guests):
        for table in self.tables:
            for guest in guests:
                if table.guest is None:
                    table.guest = guest
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    guest.run()
                else:
                    self.queue.put(guest)
                    print(f'{guest.name} в очереди')

    def discuss_guests(self):
        for table in self.tables:
            if not self.queue.empty() and table is not None:
                self.guest_arrival()
                if not guest.is_alive():
                    print(f'{table.guest} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
            elif not self.queue.empty() and table is None:
                table = self.queue.get()
                print(f'{table.guest} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')




# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()

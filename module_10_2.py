import threading
from time import sleep


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        enemy_counter = 100
        print(f'{self.name}, на нас напали!')
        day_counter = 1

        def day_ending() -> str:
            if (5 <= day_counter <= 20 or
                    5 <= day_counter % 10 <= 9 or
                    day_counter % 10 == 0):
                day = 'дней'
            elif 2 <= day_counter % 10 <= 4:
                day = 'дня'
            else:
                day = 'день'
            return day

        while enemy_counter:
            sleep(1)
            enemy_counter -= self.power
            print(f'{self.name} сражается {day_counter} {day_ending()}, осталось {enemy_counter} воинов. ')
            day_counter += 1
        print(f'{self.name} одержал победу спустя {day_counter} {day_ending()}!\n')


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()
first_knight.join()

import threading
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        counter = 100
        while counter:
            dep = randint(50, 500)
            self.balance += dep
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {dep}. Баланс: {self.balance}')
            counter -= 1
            sleep(0.001)

    def take(self):
        counter = 100
        while counter:
            tk = randint(50, 500)
            print(f'Запрос на {tk}')
            if tk <= self.balance:
                self.balance -= tk
                print(f'Снятие: {tk}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            counter -= 1


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

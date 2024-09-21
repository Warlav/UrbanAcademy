class User:
    """
    Класс пользователя, содержащий атрибуты: логин и пароль
    """

    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password


class Database:
    """
    База данных логин и пароль
    """

    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


if __name__ == '__main__':
    database = Database()
    while True:
        choice = input('Приветствую! Выберите действие:\n1 - Вход\n2 - Регистрация\n3 - Выход\n')
        # if choice == 1:
        #     login = input("Введите логин: ")
        #     password = input("Введите пароль: ")
        #     if login in database.data:
        #         if password == database.data[login]:
        #             print(f"Вход выполнен, {login}")
        #             break
        #         else:
        #             print("Неверный пароль")
        #     else:
        #         print("Пользователь не найден")
        # elif choice == 2:
        #     user = User(input("Введите логин: "), password := input("Введите пароль: "),
        #                 password2 := input("Повторите пароль: "))
        #     if password != password2:
        #         print("Пароли не совпадают. Попробуйте ещё раз")
        #         continue
        #     database.add_user(user.username, user.password)
        if choice == 3:
            exit()
        print(database.data)

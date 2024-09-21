class Database:
    """
    База данных логин и пароль
    """

    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    """
    Класс пользователя, содержащий атрибуты: логин и пароль
    """

    def __init__(self, username, password, password_confirm):
        self.username = username
        # check = True
        # if len(password) < 8:
        #     check = False
        #     print("Пароль должен быть более 7 символов")
        # for i in password:
        #     if isinstance(i, int):
        #         break
        #     else:
        #         check = False
        #         print("Пароль должен содержать хотя бы одну цифру")
        # for i in password:
        #     if i.isupper():
        #         break
        #     else:
        #         check = False
        #         print("Пароль должен содержать хотя бы одну букву верхнего регистра")
        # if password != password_confirm:
        #     check = False
        #     print("Пароли не совпадают")
        # if check == True:
        #     self.password = password
        # else:
        #     self.password = None
        if password == password_confirm:
            self.password = password


if __name__ == '__main__':
    database = Database()
    while True:
        choice = input('Приветствую! Выберите действие:\n1 - Вход\n2 - Регистрация\n3 - Выход\n')
        if choice == 1:
            login = input("Введите логин: ")
            password = input("Введите пароль: ")
            if login in database.data:
                if password == database.data[login]:
                    print(f"Вход выполнен, {login}")
                else:
                    print("Неверный пароль")
            else:
                print("Пользователь не найден")
        if choice == 2:
            user = User(input("Введите логин: "), password := input("Введите пароль: "),
                    password2 := input("Повторите пароль: "))
            if password != password2:
                print("Пароли не совпадают. Попробуйте ещё раз")
            database.add_user(user.username, user.password)
        if choice == 3:
            exit()
        print(database.data)

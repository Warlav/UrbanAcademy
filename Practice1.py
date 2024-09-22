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
        if password == password_confirm:
            self.password = password


if __name__ == '__main__':
    database = Database()
    while True:
        choice = int(input('Приветствую! Выберите действие:\n1 - Вход\n2 - Регистрация\n3 - Выход\n'))
        if choice == 1:
            login = input("Введите логин: ")
            password = input("Введите пароль: ")
            if login in database.data:
                if password == database.data[login]:
                    print(f"\nВход выполнен, {login}")
                else:
                    print("Неверный пароль")
            else:
                print("\nПользователь не найден")
        if choice == 2:
            user = User(input("Введите логин: "), password := input("Введите пароль: "),
                    password2 := input("Повторите пароль: "))
            check = True
            if len(password) < 8:
                check = False
                print("Пароль должен быть более 7 символов")
            if any(i.isdigit() for i in password):
                pass
            else:
                check = False
                print("Пароль должен содержать хотя бы одну цифру")
            if any(i.isupper() for i in password):
                pass
            else:
                check = False
                print("Пароль должен содержать хотя бы одну букву верхнего регистра")
            if any(i.islower() for i in password):
                pass
            else:
                check = False
                print("Пароль должен содержать хотя бы одну букву нижнего регистра")
            if password != password2:
                check = False
                print("Пароли не совпадают. Попробуйте ещё раз.\n")
            if check == True:
                database.add_user(user.username, user.password)
        if choice == 3:
            exit()
        print(database.data, '\n')

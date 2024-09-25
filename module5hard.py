class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f'{self.nickname}'

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f'{self.title}, {self.duration}, {self.adult_mode}'

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname:
                if hash(password) == user.password:
                    self.current_user = user

    def register(self, nickname, password, age):
        list = []
        for i in self.users:
            list.append(i.nickname)
        if nickname not in list:
           user = User(nickname, hash(password), age)
           self.users.append(user)
           self.log_in(nickname, password)
        else:
           print(f"Пользователь {nickname} уже существует")

    def log_out(self):
        self.current_user = None

    def add(self, *video):
        list = []
        for i in self.videos:
            list.append(i.title)
        for j in video:
            if j.title not in list:
                self.videos.append(j)

    def get_videos(self, search_word):
        list = []
        for i in self.videos:
            if search_word.upper() in i.title.upper():
                list.append(i.title)
        return list

    def watch_video(self, film_name):
        import time
        for film in self.videos:
            if film.title == film_name:
                if self.current_user:
                    if (self.current_user.age < 18 and not film.adult_mode) or self.current_user.age > 18:
                        for i in range(film.time_now, film.duration + 1):
                            print(i)
                            time.sleep(1)
                        print("Конец видео")
                    else:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                else:
                    print("Войдите в аккаунт, чтобы смотреть видео")
                break
            else:
                continue

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

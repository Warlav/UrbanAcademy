class UrTube:
    def __init__(self):
        self.users = {}
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        if nickname in self.users.keys():
            # if hash(password) in self.users.values[0]:
                self.current_user = nickname

    def register(self, nickname, password, age):
        if nickname not in self.users.keys():
            self.users[nickname] = (password, age)
        else:
            print(f"Пользователь {nickname} уже существует")

    def log_out(self):
        self.current_user = None

    def add(self, *Video):
        if Video not in self.videos:
            self.videos.append(Video)

    def get_videos(self, search_word):
        list = []
        for i in self.videos:
            if i.upper() == search_word.upper():
                list.append(i, "\n")
        return list

    def watch_video(self, film_name):
        for i in self.videos:
            if i == film_name:
               if User == self.current_user:
                   Video.time_now += 1
                   # time.sleep(1)
                   print(Video().time_now)



class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
# print(ur.get_videos('лучший'))
# print(ur.get_videos('ПРОГ'))

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
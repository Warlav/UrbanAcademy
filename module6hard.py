from math import pi


class Figure:
    sides_count = 0

    def __init__(self, __color: int, *__sides: int):
        self.__color = []
        self.__sides = []
        self.filled = True
        if len(__sides) == self.sides_count:
            self.__sides = __sides
        elif len(__sides) == 1:
            self.__sides = list(__sides * self.sides_count)
        else:
            for i in range(self.sides_count):
                self.__sides.append(1)
        super().__init__()

    def get_color(self):
        return self.__color

    def __is_valid_color(self, *args):
        if 0 <= all(args) <= 255:
            return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides: int):
        if sides > 0 and len(*sides) == self.__sides:
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = [*new_sides]


class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, *__sides):
        super().__init__(__color, *__sides)
        self.__color = []
        self.__sides = []
        self.__radius = int(*self.__sides) / (2 * pi)

    def get_square(self):
        return pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, *__sides):
        super().__init__(__color, *__sides)
        self.__color = []
        self.__sides = []

    def get_square(self):
        return ((self.sides_count ** 2) * (3 // 2)) / 4


class Cube(Figure):
    sides_count = 12

    def __init__(self, __color, *__sides):
        self.__color = []
        self.__sides = []
        super().__init__(__color, *__sides)

    def get_volume(self):
        if len(self.__sides) > 0:
            return self.__sides[0]**3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

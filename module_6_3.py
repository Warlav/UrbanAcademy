class Horse:
    def __init__(self, x_distance = 0, sound = 'Frrr'):
        self.x_distance = x.distance
        self.sound = sound
       
    def run(self, dx):
        return self.x_distance += dx

       
class Eagle:
    def __init__(self, y_distance = 0, sound = 'I train, eat, sleep, and repeat')

    def fly(self, dy):
        return y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        return super().__init__(Horse, Eagle)

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        pos = (x_distance, y_distance)
        return pos

    def voice(self):
        return f'{self.sound}'

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
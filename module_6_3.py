class Horse:
    def __init__(self, x_distance = 0, sound = 'Frrr'):
       self.x_distance = x.distance
       self.sound = sound
       
    def run(self, dx):
        return self.x_distance += dx
       
class Eagle:
    pass


class Pegasus:
    pass

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
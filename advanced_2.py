import random

list = []
i = 0
while i < 12:
    list.append(random.randint(1, 6))
    i = i + 1
print(f'{list[0]} {list[1]}, {list[2]} {list[3]}, {list[4]} {list[5]}, {list[6]} {list[7]}, {list[8]} {list[9]}, {list[10]} {list[11]}')

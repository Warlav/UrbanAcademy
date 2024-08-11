immutable_var = (1, 2, 3, 4, 5, 'Вышел', 'зайчик', 'погулять')
print(immutable_var)
#immutable_var[0] = 'Раз' # Облом, потому что кортеж является неизменяемым.
mutable_list = ['Вдруг', 0, 'хотник', 'выбегает', 'прямо в', 3, 'айчика', 'стреляет']
mutable_list[1] = 'о'
mutable_list[5] = 'з'
mutable_list[1] = mutable_list[1] + mutable_list[2]
mutable_list[5] = mutable_list[5] + mutable_list[6]
mutable_list.remove('хотник')
mutable_list.remove('айчика')
print(mutable_list)
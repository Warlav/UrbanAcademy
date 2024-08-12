#Словари
my_dict = {'Sasha': 1989, 'Petya': 1993, 'Kolya': 1990}
print(my_dict)
print(my_dict['Petya'])    #Петя есть
print(my_dict.get('Olya')) #А Оля не пришла
my_dict.update({'Masha': 1998, 'Sergey': 1987})    #Но сеньор Серёга привёл малолетку Машу
a = my_dict.pop('Sasha')
print(a)
print(my_dict)

#Множества
my_set = {1, 'четыре', 2, 3, 3, 'четыре', 1, 5.0}
print(my_set)
my_set.add('пять')
my_set.add(4)
my_set.discard(5.0)
print(my_set)
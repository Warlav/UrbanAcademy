#Словари
my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print(my_dict)
print('Existing value: ', my_dict['Vasya'])
print('Not existing value: ', my_dict.get('Sasha'))
my_dict.update({'Sasha': 1986, 'Alex': 1990})
print('Deleted value: ', my_dict.pop('Masha'))
print('Modified dictionary: ', my_dict)
print()

#Множества
my_set = {1, 'Яблоко', 1, 42.314, 'Яблоко'}
print('Set: ', my_set)
my_set.add(13)
my_set.add((5, 6, 1.6))
my_set.remove(1)
print('Modified set: ', my_set)
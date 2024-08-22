calls = 0
str1 = 'uRBan'
str2 = 'siSteR'
checked_list1 = ['Urban', 'ban', 'BaNaN', 'urBAN']
checked_list2 = ['Father', 'Mother', 'Sister', 'Brother']


def count_calls():
  global calls
  calls += 1


def string_info(string):
  count_calls()
  print(len(string), string.upper(), string.lower())


def is_contains(string, list_to_search):
  count_calls()
  lst = []
  for i in list_to_search:
    if i.lower() == string.lower():
      lst.append(i)
  if len(lst) > 0:
    return lst
  else:
    return 'Совпадений нет'


string_info(str1)
string_info(str2)
print(is_contains(str1, checked_list1))
print(is_contains(str1, checked_list2))
print(is_contains(str2, checked_list1))
print(is_contains(str2, checked_list2))
print('Функций задействовано: ', calls)

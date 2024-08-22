calls = 0
string = input('Введите пароль: ').lower()
list_to_search = ['пароль', 'pass', 'password', 'passcode', 'secret']


def count_calls():
  global calls
  calls += 1


def string_info(string):
  count_calls()
  print('Длина пароля: ', len(string))


def is_contains(string, list_to_search):
  count_calls()
  if string in list_to_search:
    print('Вход разрешён')
  else:
    print('Вход запрещён')


string_info(string)
is_contains(string, list_to_search)
print('Функций задействовано: ', calls)


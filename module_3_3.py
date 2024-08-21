def print_params(a=1, b='строка', c=True):
  print(a, b, c)

print('\n#1')
print("print_params(True, 346, 0, 'строка') #выдаёт ошибку")
print_params()
print_params(b=25)
print_params(c=[1,2,3])

print('\n#2')
values_list = ['one', 'two', 'three']
values_dict = {'a': 'Привет', 'b': 28, 'c': False}
print_params(*values_list)
print_params(**values_dict)

print('\n#3')
value_list_2 = [23, True]
print_params(*value_list_2, 42)

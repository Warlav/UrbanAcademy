data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(*data_structure):
  sum = 0
  for i in data_structure:
    if isinstance(i, int) or isinstance(i, float):
      sum += i
    elif isinstance(i, str):
      sum += len(i)
    elif isinstance(i, dict):
      i = list(i.items())
      sum += calculate_structure_sum(*i)
    else:
      sum += calculate_structure_sum(*i)
  #  print(i, type(i), sum) - эта строчка помогла
  # мне отследить последовательность счёта и искать
  # ошибки кода.
  return sum

result = calculate_structure_sum(data_structure)
print(result)

def single_root_words(root_word, *other_words):
  same_words = []
  for i in other_words:
    if root_word.lower() in i.lower():
      same_words.append(i)
    elif i.lower() in root_word.lower():
      same_words.append(i)
  return same_words

result1 = single_root_words('Be', 'baNaNa', 'bEan', 'beeF', 'bOat', 'bEEr')
result2 = single_root_words('BeerLoga', 'BaNana', 'beE', 'beAn', 'BEEF', 'BoaT', 'BEER', 'log')
print(result1)
print(result2)

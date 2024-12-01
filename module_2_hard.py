import random
fst_num = random.randint(3, 20)
snd_num = []
for i in range(1, fst_num):
  for j in range(1, fst_num):
    if fst_num % (i + j) == 0 and i < j:
      snd_num.append(str(i))
      snd_num.append(str(j))
print('Первый камень: ', fst_num)
print('Второй камень: ', ''.join(snd_num))

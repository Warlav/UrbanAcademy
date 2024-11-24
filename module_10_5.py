import time
import multiprocessing


def read_info(name):
  all_data = []
  with open(name, 'r', encoding='utf-8') as file:
    while file.readline() == '':
      all_data.append(file.readline())


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
start_time = time.time()
for file in filenames:
  read_info(file)
print(time.time() - start_time)

# Многопроцессный
if __name__ == '__main__':
  start_time = time.time()
  with multiprocessing.Pool() as pool:
    pool.map(read_info, filenames)
    pool.join()
  print(time.time() - start_time)
  

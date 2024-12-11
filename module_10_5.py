import time
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while file.readline() == '':
            all_data.append(file.readline())


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
line_time = time.time()
for _ in filenames:
    read_info(_)
print(time.time() - line_time)

# Многопроцессный
if __name__ == '__main__':
    proc_time = time.time()
    with multiprocessing.Pool() as pool:
        pool.imap(read_info, filenames)
    print(time.time() - proc_time)

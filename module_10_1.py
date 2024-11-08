import time
import threading


def write_words(word_count: int, file_name: str):
    i = 1
    while i <= word_count:
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(f'Какое-то слово № {i}.\n')
        i += 1
        time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}.')


# Расчёт через функцию
def_start = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
def_end = time.time()
print(def_end - def_start)

# Расчёт через потоки
thread_1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread_2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread_3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread_4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

thread_start = time.time()
thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()
thread_end = time.time()
print(thread_end - thread_start)

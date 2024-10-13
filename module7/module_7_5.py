import os
import time

root = '.'

for root, dirs, files in os.walk(root):
    for dir in dirs:
        for file in files:
            filepath = os.path.join(root, dir, file)
            filetime = os.path.getmtime(file)
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
            filesize = os.path.getsize(file)
            parent_dir = os.path.dirname(dir)
            print(
                f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time},'
                f' Родительская директория: {parent_dir}')

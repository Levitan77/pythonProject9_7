# Домашнее задание по теме "Файлы в операционной системе"

# Цель задания:
#
# Освоить работу с файловой системой в Python, используя модуль os.
# Научиться применять методы os.walk, os.path.join, os.path.getmtime, os.path.dirname, os.path.getsize
# и использование модуля time для корректного отображения времени.
#
# Задание:
#
# Создайте новый проект или продолжите работу в текущем проекте.
# 1. Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
# 2. Примените os.path.join для формирования полного пути к файлам.
# 3. Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
# 4. Используйте os.path.getsize для получения размера файла.
# 5. Используйте os.path.dirname для получения родительской директории файла.

import os, time
from os.path import join, getmtime, getsize, dirname
# directory = "."     # тестировать будем в папке проекта
for root, dirs, files in os.walk(directory):    # 1
    for file in files:
        filepath = os.path.join(root, file)     # 2
        filetime = os.path.getmtime(filepath)   # 3 # Исправлено !!!
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)    # 4 # Исправлено !!!
        parent_dir_ = os.path.dirname(os.path.abspath(filepath))     # полный путь родительского каталога
        parent_dir = os.path.dirname(filepath)  # 5 # Исправлено !!! # относительный путь
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, '
              f'Родительская директория: {parent_dir}')

# Комментарии к заданию:
#
# Ключевая идея – использование вложенного for
#
# for root, dirs, files in os.walk(directory):
#   for file in files:
#     filepath = ?
#     filetime = ?
#     formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
#     filesize = ?
#     parent_dir = ?
#     print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time},
#             Родительская директория: {parent_dir}')
#
#
#
# Так как в разных операционных системах разная схема расположения папок, тестировать проще всего
# в папке проекта (directory = “.”)
# Пример возможного вывода:
# Обнаружен файл: main.py, Путь: ./main.py, Размер: 111 байт, Время изменения: 11.11.1111 11:11,
#   Родительская директория.

# Комментарий преподавателя [Исаев Дмитрий  23.11.2024 02:00]:
# Ваш код требует доработки:
# - Вы верно определили полный путь к файлам с помощью метода`os.path.join`: filepath = os.path.join(root, file)
# - а в методах os.path.getmtime, os.path.getsize, os.path.dirname в качестве аргумента Вам надо
#   передавать filepath (полный путь к файлу), который вы определили ранее.
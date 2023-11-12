"=================Модули и пакеты=================="

# модуль - любой файл с расширением .py
# пакет - набор модулей (обязательно должен быть файл __init__.py(превращает папку в пакет))

# import math -> module
# import random -> module
# import itertools -> module

"================Работа с файлами================="

# file = open("test.txt", 'r')
# print(file.read())
# open - функция, которая открывает файл в определенном режиме

# r - только для чтения(read)
# w - только для записи(write)
# a - только для дозаписиб добавляет в конец(append)
# x - создает файл, но если такой файл существует - выдаст нам ошибку
# b - в бинарном виде выдает информацию (binary)

# ======================READ
# try:
#     file = open('test.txt', 'r')
    # print(dir(file))
    # print(file.read())
#     # print(file.readable()) -> True
#     # print(file.tell()) текущее положение каретки(курсора)
#     file.seek(0)  # управление курсором
#     print(file.readlines())
# finally:
#     file.close() 

# =============WRITE
# try:
#     file = open("test.txt", 'w')
#     file.write('my name is eraaly\n')
#     file.seek(19)
#     file.write('my name is anton\n')
#     file.writelines(['makers\n', 'bootcamp\n'])
# finally:
#     file.close()

# =======================append
# try:
#     file = open('test.txt', 'a')
#     file.write('\nschool')
#     file.seek(250) тут не имеет смысла(все равно добавит в конец)
#     file.write('\nrsghfnd')
# finally:
#     file.close()

"==========Контекстный менеджер=============="

with open('test.txt', 'r') as file:
    print(file.read())

with open('new_file.py', 'x') as file:
    if file.writable():
        file.write('print("hello world")')






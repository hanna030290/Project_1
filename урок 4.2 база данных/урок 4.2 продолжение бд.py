# Задача 1 Создайте новую Базу данных Поля: id, 2 целочисленных поляЦелочисленные поля заполняются рандомно от 0 до 9Выберите случайную запись из БДЕсли каждое число данной записи чётное, то удалите эту запись, если нечётное, то обновите данные в ней на (2,2)
# import random, sqlite3
#
# conn = sqlite3.connect('name.db')
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_2(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INT, col_2 INT)''')
#
# for i in range(3):
#     a = random.randint(0, 9)
#     b = random.randint(0, 9)
#     cursor.execute('''INSERT INTO tab_2(col_1,col_2) VALUES (?,?)''', (a, b))
# # conn.commit()
# cursor.execute('''SELECT * FROM tab_2''')
# k = cursor.fetchall()
# print(k)
# cursor.execute('''SELECT id FROM tab_2''')
# k = cursor.fetchall()
# # print(k)
#
# r = random.choice(k)
# print(r)
#
# cursor.execute('''SELECT col_1, col_2 FROM tab_2 WHERE id=?''', r)
# k2 = cursor.fetchall()
# print(k2)
#
# print(k2[0][0], k2[0][1])
# if k2[0][0] % 2 == 0 and k2[0][1] % 2 == 0:
#     cursor.execute('''DELETE FROM tab_2 WHERE id=?''', r)
# else:
#     cursor.execute('''UPDATE tab_2 SET col_1=2,col_2=2 WHERE id=?''', r)
# conn.commit()
# cursor.execute('''SELECT * FROM tab_2''')
# k = cursor.fetchall()
# print(k)

# Задача 2
# Создайте метод класса для работы с БД.
# Достаточно одной колонки в таблице. Тип INT.
# В БД:Если передан 1 аргумент, вставить в таблицу запись с числом 3.
# Если переданы 2 аргумента: проверить или второй аргумент является числом.
# Если условие верно, то удалить первую запись с БД.
# Если переданы 2 аргумента и их тип значений неизвестен, а 3 аргумент является числом,
# то обновить значение колонки БД на число 77 в 3 записи.


# import sqlite3
#
# conn = sqlite3.connect('name.db')
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_3(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INT)''')
#
#
# class A:
#     def m(self, a=None, b=None, c=None):
#         # В БД:Если передан 1 аргумент, вставить в таблицу запись с числом 3.
#         if a is not None and b is None and c is None:
#             print('INSERT')
#             cursor.execute('''INSERT INTO tab_3(col_1) VALUES (3)''')
#             conn.commit()
#         # Если переданы 2 аргумента: проверить или второй аргумент является числом.
#         # Если условие верно, то удалить первую запись с БД.
#         elif a is not None and type(b) is int and c is None:
#             print('DELETE')
#             cursor.execute('''DELETE FROM tab_3 WHERE id=1''')
#             conn.commit()
#         # Если переданы 2 аргумента и их тип значений неизвестен, а 3 аргумент является числом,
#         # то обновить значение колонки БД на число 77 в 3 записи.
#         elif a is not None and b is not None and type(c) is int:
#             print('UPDATE')
#             cursor.execute('''UPDATE tab_3 SET col_1=77 WHERE id=3''')
#             conn.commit()
#
#
# a_obj = A()
# a_obj.m(1,'as',3)
# cursor.execute('''SELECT * FROM tab_3''')
# k = cursor.fetchall()
# print(k)

# задача 3
# Создать таблицу в Базе Данных с тремя колонками(id, 2 - text, 3 - text).
# Заполнить её с помощью INSERT данными (3 записи).
# Удалить с помощью DELETE 2 запись.
# Обновить значения 3-ей записи на: hello world с помощью UPDATE
# *Записать данные с таблицы в файл в три колонки.
# Первая – id, вторая и третья с данными.

# import sqlite3
#
# conn = sqlite3.connect('base_3.db')
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT,col_2 TEXT) ''')
# cursor.execute('''INSERT INTO tab_1(col_1,col_2) VALUES ('hello','world')''')
# cursor.execute('''DELETE FROM tab_1 WHERE id = 2''')
# conn.commit()
#
# t = 'hello world' # обновление данных в таблице
# cursor.execute('''UPDATE tab_1 SET col_2='people' WHERE id=?''', (t,))
# # cursor.execute('''UPDATE tab_1 SET col_1='test', col_2='test' WHERE id=?''', (t,))
# cursor.execute('''SELECT*FROM tab_1''')
# k = cursor.fetchall()
# print(k)
# conn.commit()
# f = open('BD.txt', 'w', encoding='utf-8')
# for i in k:
#     c = ','.join([str(x) for x in i])
#     f.write((c + '\n'))
# print(k)
#
# f.close()

# Сформулируйте SQL запрос для создания таблицы book (book_id INT …, title TEXT, author TEXT, price INT, amount INT )
# 2. Занесите новую строку в таблицу book с клавиатуры
# 3. Выбрать информацию о всех книгах из таблицы book.
import sqlite3

conn = sqlite3.connect('Book.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title TEXT,author TEXT, price INT, amount INT) ''')
while True:
    a = input('Введите название книги: ')
    b = input('Введите автора книги: ')
    c = int(input('Введите цену книги: '))
    d = int(input('Введите количесво книг или 0 для выхода: '))
    if d == 0:
        break
    cursor.execute('''INSERT INTO tab_1(title ,author, price, amount ) VALUES (?,?,?,?)''', (a, b, c, d))

cursor.execute('''SELECT*FROM Book''')
k = cursor.fetchall()
print(k)


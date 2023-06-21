import sqlite3

# Создаём Базу данных
conn = sqlite3.connect('name.db')
# Создаем объект cursor, который позволяет нам взаимодействовать с базой данных и добавлять записи
cursor = conn.cursor()
# Создадим таблицу с двумя текстовыми колонками
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT,col_2 TEXT) ''')

# Заполняем таблицу данными
cursor.execute('''INSERT INTO tab_1(col_1,col_2) VALUES ('hello','world')''')
# # Сохраняем изменения
# conn.commit()

# d = "red"
# f = "black"
# cursor.execute('''INSERT INTO tab_1(col_1,col_2) VALUES (?,?)''', (d, f))
# conn.commit()

# cursor.execute('''SELECT*FROM tab_1''')
# k = cursor.fetchall()
# print(k)
#
#cursor.execute('''SELECT col_1, id, col_2 FROM tab_1''')
cursor.execute('''SELECT id FROM tab_1''')
k2 = cursor.fetchall()
print(k2)

t = 3 # обновление данных в таблице
# cursor.execute('''UPDATE tab_1 SET col_1='world WHERE id=?''', (t,))
cursor.execute('''UPDATE tab_1 SET col_1='test', col_2='test' WHERE id=?''', (t,))
cursor.execute('''SELECT*FROM tab_1''')
k = cursor.fetchall()
print(k)
conn.commit()

# 1
# Примеры Select
# cursor.execute('''SELECT * FROM tab_1 WHERE col_1='hello''')
# conn.commit()
# k = cursor.fetchall()
# print(k)
# 2
# Список всех записей отсортированных относительно тертьей колонки
# cursor.execute('''SELECT * FROM tab_1 ORDER BY col_3''')
# conn.commit()
# k = cursor.fetchall()
# print(k)
# 3
# В нашем случае мы искали по всей таблице записи третьей колонки, которые начитнаются с 7.
# Знак процент(%) является подстановочным оператором.
# cursor.execute('''SELECT * FROM tab_1 WHERE col_3 LIKE '7%' ''')
# conn.commit()
# k = cursor.fetchall()
# print(k)

# import sqlite3
# #
# # Создаём Базу данных
# conn = sqlite3.connect('name.db')
# # Создаем объект cursor, который позволяет нам взаимодействовать с базой данных и добавлять записи
# cursor = conn.cursor()
# # Создадим таблицу с двумя текстовыми колонками
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_2(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT,col_2 INT) ''')

# Заполняем таблицу данными
# for i in range(4):
#     cursor.execute('''INSERT INTO tab_2(col_1,col_2) VALUES ('hello',12)''')
# # Сохраняем изменения
# conn.commit()

# n = 77
# cursor.execute('''INSERT INTO tab_2(col_1,col_2) VALUES ('hello',?)''', (n,))
# conn.commit()
# cursor.execute('''SELECT * FROM tab_2''')
# k = cursor.fetchall()
# print(k)

# ЗАДАЧА 1
# import sqlite3
#
# n = int(input("Введите число: "))
# # Создаём Базу данных
# conn = sqlite3.connect('task_1.db')
# # Создаем объект cursor, который позволяет нам взаимодействовать с базой данных и добавлять записи
# cursor = conn.cursor()
# # Создадим таблицу с 3 текстовыми колонками
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_3(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT,col_2 TEXT, col_3 int) ''')
#
# cursor.execute('''INSERT INTO tab_3(col_1,col_2,col_3) VALUES ('hello','world',?)''', (n,))
# conn.commit()
#
# cursor.execute('''SELECT * FROM tab_3''')
# k = cursor.fetchall()
# print(k)
# for i in k:
#     c = ','.join([str(x) for x in i])
#     print(c)

 # Удаление записи из таблицы по id, по значению
# cursor.execute('''DELETE FROM tab_1 WHERE id = 1''')
# conn.commit()
# cursor.execute('''DELETE FROM tab_1 WHERE col_1 ='red' ''')
# conn.commit()
# cursor.execute('''SELECT*FROM tab_1''')
# k=cursor.fetchall()
# print(k)


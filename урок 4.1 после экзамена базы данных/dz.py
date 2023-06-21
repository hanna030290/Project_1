import sqlite3
import random

# # Создаём Базу данных
conn = sqlite3.connect('base_1.db')
cursor = conn.cursor()
# # Создадим таблицу с двумя текстовыми колонками
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INT,col_2 INT) ''')
for i in range(3):
    x = random.randint(1, 9)
    y = random.randint(1, 9)
    cursor.execute('''INSERT INTO tab_1(col_1,col_2) VALUES (?,?)''', (x, y))

cursor.execute('''SELECT col_1,col_2 FROM tab_1''')
k = cursor.fetchall()
print(k)
s = 0
for i in k:
    for j in i:
        s += j
print('SUM', s)
sr = (s / (len(k) * 2))
print(sr)

if sr > len(k):
    cursor.execute('''DELETE FROM tab_1 WHERE id = 4''')
conn.commit()
cursor.execute('''SELECT*FROM tab_1''')
k = cursor.fetchall()
print(k)



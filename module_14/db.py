import sqlite3
from random import randint

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

# cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', ('newuser', 'ex@gmail.com', '28'))
# cursor.execute('UPDATE Users SET age = ? WHERE username = ?', ('29', 'newuser'))
# cursor.execute('DELETE FROM Users WHERE username = ?', ('newuser',))

# for i in range(30):
#     cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)',
#                    (f'newuser{i}', f'{i}ex@gmail.com', str(randint(20, 60))))
# cursor.execute('SELECT * FROM Users')

# cursor.execute('SELECT username, age FROM Users WHERE age > ?', (29,))

# cursor.execute('SELECT username, age FROM Users GROUP BY age')
# users = cursor.fetchall()
# for user in users:
#     print(user)
# print(len(users))

cursor.execute('SELECT SUM(age) FROM Users')
all_age = cursor.fetchone()[0]
cursor.execute('SELECT COUNT(*) FROM Users')
all_users = cursor.fetchone()[0]
print(all_age/all_users)
cursor.execute('SELECT AVG(age) FROM Users')
avg_age = cursor.fetchone()[0]
print(avg_age)
cursor.execute('SELECT MAX(age) FROM Users')
print(cursor.fetchone()[0])
cursor.execute('SELECT MIN(age) FROM Users')
print(cursor.fetchone()[0])


connection.commit()
connection.close()

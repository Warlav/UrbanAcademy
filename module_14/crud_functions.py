import sqlite3

connection = sqlite3.connect('products.db')
cursor = connection.cursor()


# Создание таблиц:
def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INT NOT NULL
    )
    ''')
    connection.commit()


# ----------------------------------------------------------------------------------------------------------------------
# Раздел продуктов:
def add_product(title, description, price):
    check_title = cursor.execute('SELECT * FROM Products WHERE title = ?', (title,))
    if check_title.fetchone() is None:
        cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
                       (title, description, price))
    connection.commit()


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    connection.commit()
    connection.close()
    return products


# ----------------------------------------------------------------------------------------------------------------------
# Раздел пользователей:
def add_user(username, email, age):
    if not is_included(username):
        cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                       (username, email, age, 1000))
    connection.commit()


def is_included(username):
    check_user = cursor.execute('SELECT username FROM Users WHERE username = ?', (username,))
    connection.commit()
    if check_user.fetchone() is not None:
        return True
    else:
        return False


initiate_db()
for i in range(1, 5):
    add_product(f'Цифра {i}', f'цифра {i}', f'{i * 100}')
connection.commit()

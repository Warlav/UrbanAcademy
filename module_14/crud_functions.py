import sqlite3

connection = sqlite3.connect('products.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INT PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INT NOT NULL,
    balance INT NOT NULL
    )
    ''')
    connection.commit()


def add_product(title, description, price):
    check_title = cursor.execute('SELECT * FROM Products WHERE title =?', (title,))
    if check_title.fetchone() is None:
        cursor.execute(f'''
INSERT INTO Products VALUES ({title}, {description}, {price})
''')
        connection.commit()


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    connection.commit()
    connection.close()
    return products


def add_user(username, email, age):
    check_title = cursor.execute('SELECT * FROM Products WHERE title =?', (username,))
    if check_title.fetchone() is None:
        cursor.execute(f'''
    INSERT INTO Products VALUES ({username}, {email}, {age}, 1000)
    ''')
        connection.commit()


connection.commit()

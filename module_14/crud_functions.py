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
    connection.commit()


def add_product(title, description, price):
    check_title = cursor.execute('SELECT * FROM Products WHERE title =?', (title,))
    if check_title.fetchone() is None:
        cursor.execute(f'''
INSERT INTO Products VALUES (f{title}, f{description}, f'{price}')
''')
        connection.commit()


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    connection.commit()
    connection.close()
    return products


connection.commit()

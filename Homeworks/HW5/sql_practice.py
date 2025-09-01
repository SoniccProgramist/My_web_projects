import sqlite3

class User:
    def __init__(self, db_path='users.db'):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def register(self, username, password, email):
        try:
            self.cursor.execute("""
            INSERT INTO users (username, password, email)
            VALUES (?, ?, ?)
            """, (username, password, email))
            self.conn.commit()
            print(f"Користувач {username} успішно додан!")
        except sqlite3.IntegrityError as e:
            print(f"Помилка: Користувач за цими даними вже існує. Спробуйте інші данні.")

    def login(self, username, password):
        self.cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )
        return self.cursor.fetchone() is not None

    def close(self):
        self.conn.close()

if __name__ == '__main__':
    with sqlite3.connect('users.db') as connection:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
            """)

        test_users = [
            ('Alex', 'pas1', 'alex@gmail.com'),
            ('Omar', 'pas2', 'OmariO@gmail.com'),
            ('Mario', 'pas3', 'MaRio@gmail.com')
        ]
        cursor.executemany("INSERT OR IGNORE INTO users (username, password, email) VALUES (?, ?, ?)", test_users)
        connection.commit()

    new_user = User()
    try:
        while True:
            print('Ласкаво просимо! Ось функції:')
            answer = int(input('''
                1 - Зареєструватися
                2 - Увійти
                3 - Вийти
            '''))
            if answer == 1:
                username = input('user name: ')
                password = input('password: ')
                email = input('email: ')
                new_user.register(username, password, email)
            elif answer == 2:
                username = input('user name: ')
                password = input('password: ')
                print('Успішний вхід!' if new_user.login(username, password) else 'Неправильні дані!')
            elif answer == 3:
                break
    finally:
        new_user.close()
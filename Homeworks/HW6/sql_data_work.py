import sqlite3


class User:
    def __init__(self, db_path='users.db'):
        # Ініціалізація підключення до бази даних
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self):
        # Створення таблиці users з унікальними обмеженнями
        # Поле provider зберігає інформацію про сервіс (local, google, apple, facebook)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            provider TEXT DEFAULT 'local'
        )
        """)

        # Створення додаткової таблиці site_registrations
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS site_registrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            site_name TEXT NOT NULL,
            login TEXT,
            password TEXT,
            entry_type TEXT NOT NULL,  -- google, apple, facebook, other
            user_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
        """)
        self.conn.commit()

    def _email_exists(self, email):
        # Перевірка існування email
        self.cursor.execute("SELECT 1 FROM users WHERE email = ?", (email,))
        return self.cursor.fetchone() is not None

    def register(self, username, password, email, provider='local'):
        # Перевірка, чи не існує email
        if self._email_exists(email):
            print(f"Помилка: Email {email} вже зареєстрований.")
            return

        try:
            # Реєстрація нового користувача
            self.cursor.execute("""
            INSERT INTO users (username, email, password, provider)
            VALUES (?, ?, ?, ?)
            """, (username, email, password, provider))
            self.conn.commit()
            print(f"Користувач {username} успішно зареєстрований через {provider}!")
        except sqlite3.IntegrityError as e:
            print(f"Помилка: Користувач з іменем {username} або email {email} вже існує.")

    def login(self, username, password, provider='local'):
        # Перевірка даних для входу та повернення user_id
        self.cursor.execute("""
        SELECT id, password FROM users WHERE username = ? AND provider = ?
        """, (username, provider))
        result = self.cursor.fetchone()
        if result and password == result[1]:
            print(f"Успішний вхід для {username} через {provider}!")
            return result[0]  # Повертаємо user_id
        else:
            print("Неправильні дані!")
            return None

    def add_site_registration(self, user_id, site_name, entry_type):
        # Додавання інформації про реєстрацію на сайті
        login = None
        password = None
        entry_type = entry_type.lower()

        if entry_type not in ['google', 'apple', 'facebook', 'other']:
            print("Помилка: Невідомий вид входу. Використовуйте google, apple, facebook або other.")
            return

        if entry_type == 'other':
            login = input('login: ')
            password = input('password: ')

        try:
            self.cursor.execute("""
            INSERT INTO site_registrations (site_name, login, password, entry_type, user_id)
            VALUES (?, ?, ?, ?, ?)
            """, (site_name, login, password, entry_type, user_id))
            self.conn.commit()
            print(f"Інформація про сайт {site_name} успішно додана!")
        except sqlite3.Error as e:
            print(f"Помилка під час додавання: {e}")

    def list_site_registrations(self, user_id):
        # Виведення списку сайтів для користувача
        self.cursor.execute("""
        SELECT site_name, entry_type, login, password 
        FROM site_registrations WHERE user_id = ?
        """, (user_id,))
        sites = self.cursor.fetchall()

        if not sites:
            print("У вас немає зареєстрованих сайтів.")
            return

        print("Ваші зареєстровані сайти:")
        for site in sites:
            site_name, entry_type, login, password = site
            print(f"- Сайт: {site_name}, Вид входу: {entry_type}")
            if login:
                print(f"  Логін: {login}, Пароль: {password}")
            else:
                print("  (Спеціальний вхід без логіна/пароля)")

    def close(self):
        # Закриття підключення до бази даних
        self.conn.close()


if __name__ == '__main__':
    # Створення таблиць та додавання тестових користувачів
    with sqlite3.connect('users.db') as connection:
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            provider TEXT DEFAULT 'local'
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS site_registrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            site_name TEXT NOT NULL,
            login TEXT,
            password TEXT,
            entry_type TEXT NOT NULL,
            user_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
        """)
        # Тестові користувачі
        test_users = [
            ('testuser1', 'password1', '<EMAIL>', 'local'),
            ('testuser2', 'password2', '<EMAIL>', 'google'),
            ('testuser3', 'password3', '<EMAIL>', 'facebook')
        ]
        cursor.executemany("INSERT OR IGNORE INTO users (username, password, email, provider) VALUES (?, ?, ?, ?)",
                           test_users)
        connection.commit()

    new_user = User()
    try:
        while True:
            print('Вибери що треба')
            answer = int(input('''
                1 - Зареєструватися
                2 - Увійти
                3 - Вийти
            '''))
            if answer == 1:
                username = input('user name: ')
                password = input('password: ')
                email = input('email: ')
                provider = input('Provider (local/google/apple/facebook): ').lower() or 'local'
                new_user.register(username, password, email, provider)
            elif answer == 2:
                username = input('user name: ')
                password = input('password: ')
                provider = input('Provider (local/google/apple/facebook): ').lower() or 'local'
                user_id = new_user.login(username, password, provider)
                if user_id:
                    # Підменю після успішного входу
                    while True:
                        sub_answer = int(input('''
                            4 - Додати сайт
                            5 - Переглянути сайти
                            6 - Вийти з підменю
                        '''))
                        if sub_answer == 4:
                            site_name = input('site name: ')
                            entry_type = input('Entry type (google/apple/facebook/other): ').lower()
                            new_user.add_site_registration(user_id, site_name, entry_type)
                        elif sub_answer == 5:
                            new_user.list_site_registrations(user_id)
                        elif sub_answer == 6:
                            break
            elif answer == 3:
                break
    finally:
        new_user.close()
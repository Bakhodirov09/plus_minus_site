import sqlite3


class DatabaseManager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        try:
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT,
            age INTEGER,
            gender TEXT,
            phone_number TEXT,
            photo TEXT,
            chat_id INTEGER,
            longitude TEXT,
            latitude TEXT
            )
            """)
            self.conn.commit()
        except Exception as exc:
            print(exc)

        try:
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER,
            chat_id INTEGER,
            total_price INTEGER,
            total_product INTEGER,
            )
            """)
            self.conn.commit()
        except Exception as exc:
            print(exc)

        try:
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS order_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER,
            product_name INTEGER,
            product_price INTEGER,
            product_quantity INTEGER,
            product_size TEXT
            )
            """)
            self.conn.commit()
        except Exception as exc:
            print(exc)

    def add_user(self, data: dict):
        try:
            full_name = data.get('full_name')
            longitude = data.get('longitude')
            latitude = data.get('latitude')
            age = data.get('age')
            phone_number = data.get('phone_number')
            chat_id = data.get('chat_id')
            gender = data.get('gender')
            photo = data.get('photo')

            self.cursor.execute("""
            INSERT INTO users (full_name, longitude, latitude, age, phone_number, chat_id, gender, photo) VALUES (?,?,?,?,?,?,?,?)
            """, (full_name, longitude, latitude, age, phone_number, chat_id, gender, photo))
            self.conn.commit()
            return True
        except Exception as exc:
            print(exc)
            return False

    def get_user(self, chat_id):
        return self.cursor.execute(f"SELECT * FROM users WHERE chat_id={chat_id}").fetchone()

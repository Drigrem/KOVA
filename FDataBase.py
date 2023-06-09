import math
import sqlite3
import time
import datetime


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def add_user(self, surname, name, second_surname, phone_number, weight, distance, password):
        try:
            self.__cur.execute("SELECT COUNT(*) as count FROM users WHERE phone_number = ?", (phone_number,))
            if self.__cur.fetchone()['count'] > 0:
                return False

            tm = int(time.time())
            time_formatted = datetime.datetime.fromtimestamp(tm).strftime("%H:%M")
            self.__cur.execute("INSERT INTO users VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?)",
                                (surname, name, second_surname, phone_number, weight, distance, password, time_formatted))
            self.__db.commit()
            return True
        except sqlite3.Error as e:
            print("Ошибка добавления пользователя в БД: ", e)
            return False

    def get_users(self):
        try:
            self.__cur.execute("SELECT id, surname, name, second_surname, phone_number, time FROM users ORDER BY time DESC")
            return self.__cur.fetchall()
        except sqlite3.Error as e:
            print("Ошибка получения данных о пользователях из БД:", e)
            return []

    def get_user_by_phone(self, phone_number):
        try:
            self.__cur.execute("SELECT * FROM users WHERE phone_number = ?", (phone_number,))
            res = self.__cur.fetchone()
            return dict(zip(self.__cur.description, res)) if res else False
        except sqlite3.Error as e:
            print("Ошибка получения данных о пользователе из БД:", e)
            return False

    def get_password(self, password):
        try:
            self.__cur.execute("SELECT * FROM users WHERE password = ?", (password,))
            return self.__cur.fetchone() or False
        except sqlite3.Error as e:
            print("Ошибка получения данных о пользователе из БД:", e)
            return False

    def get_user(self, user_id):
        try:
            self.__cur.execute("SELECT * FROM users WHERE id = ?", (user_id,))
            res = self.__cur.fetchone()
            if not res:
                print("Пользователь не найден")
            return res or False
        except sqlite3.Error as e:
            print("Ошибка получения данных о пользователе из БД:", e)
            return False

    def add_order(self, cost, distance, weight):
        try:
            tm = int(time.time())
            time_formatted = datetime.datetime.fromtimestamp(tm).strftime("%H:%M")
            self.__cur.execute("INSERT INTO orders (price, distance, weight, time) VALUES (?, ?, ?, ?)",
                                (cost, distance, weight, time_formatted))
            self.__db.commit()
            return True
        except sqlite3.Error as e:
            print("Ошибка добавления заказа в БД:", e)
            return False

    def get_orders(self):
        try:
            self.__cur.execute("SELECT * FROM orders")
            return self.__cur.fetchall()
        except sqlite3.Error as e:
            print("Ошибка получения заказов из БД:", e)
            return []

    def get_drivers(self):
        try:
            self.__cur.execute("SELECT * FROM users")
            return self.__cur.fetchall()
        except sqlite3.Error as e:
            print("Ошибка получения данных о водителях из БД:", e)
            return []

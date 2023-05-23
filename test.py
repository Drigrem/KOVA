import unittest
import sqlite3
from app import app
from FDataBase import FDataBase


class FDataBaseTestCase(unittest.TestCase):
    def setUp(self):
        app.config['DATABASE'] = 'test.db'
        self.db = sqlite3.connect(app.config['DATABASE'])
        self.db.execute("DROP TABLE IF EXISTS users")
        self.db.execute("CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, "
                        "surname VARCHAR(50), name VARCHAR(50), second_surname VARCHAR(50), "
                        "phone_number VARCHAR(20), weight INTEGER, distance INTEGER, password VARCHAR(50), time VARCHAR(50))")
        self.db.execute("INSERT INTO users VALUES (1, 'John', 'Doe', 'Smith', '123456789', 70, 10, 'password123', '10:00')")
        self.db.commit()

    def tearDown(self):
        self.db.execute("DROP TABLE IF EXISTS users")
        self.db.close()

    def test_get_drivers(self):
        db = FDataBase(self.db)
        drivers = db.get_drivers()
        self.assertEqual(len(drivers), 1)
        driver = drivers[0]
        self.assertEqual(driver[1], 'John')
        self.assertEqual(driver[2], 'Doe')
        self.assertEqual(driver[3], 'Smith')
        self.assertEqual(driver[4], '123456789')
        self.assertEqual(driver[5], 70)
        self.assertEqual(driver[6], 10)
        self.assertEqual(driver[7], 'password123')
        self.assertEqual(driver[8], '10:00')


if __name__ == '__main__':
    unittest.main()

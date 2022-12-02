import unittest
import sqlite3
from car_part import CarPart
from sqlite_inventory_database import SQLiteInventoryDatabase


class TestDatabaseMethods(unittest.TestCase):
    def setUp(self):
        self.database = SQLiteInventoryDatabase(
            connection=sqlite3.connect(':memory:'))
        self.conn = self.database.connection
        self.cursor = self.conn.cursor()

        self.cursor.execute(
            'CREATE TABLE car_parts(id INTEGER PRIMARY KEY, name, count, price, manufacturer, category)')

        data = [('test name', 10, 20.00, 'test manufacturer', 'test category'),
                ('random', 1000, 10.50, 'manu', 'cat'),
                ('car part', 275, 5.00, 'abc', 'abc'),
                ('tires', 5000, 50.00, 'Apollo Tyres', 'tires'),
                ('name', 856, 1.25, 'xyz', 'xyz')]
        self.cursor.executemany(
            'INSERT INTO car_parts(name, count, price, manufacturer, category) VALUES (?, ?, ?, ?, ?)', data)
        self.conn.commit()

    def tearDown(self):
        self.conn.close()

    def test_get_part(self):
        '''Test Case 11'''

        car_part = CarPart(id=4, name='tires', count=5000, price=50.00,
                           manufacturer='Apollo Tyres', category='tires')

        database_part = self.database.get_part(4)

        self.assertEqual(database_part, car_part)

    def test_get_all_parts(self):
        '''Test Case 12'''

        car_parts = {
            1: CarPart(id=1, name='test name', count=10, price=20.00, manufacturer='test manufacturer', category='test category'),
            2: CarPart(id=2, name='random', count=1000, price=10.50, manufacturer='manu', category='cat'),
            3: CarPart(id=3, name='car part', count=275, price=5.00, manufacturer='abc', category='abc'),
            4: CarPart(id=4, name='tires', count=5000, price=50.00, manufacturer='Apollo Tyres', category='tires'),
            5: CarPart(id=5, name='name', count=856, price=1.25, manufacturer='xyz', category='xyz')
        }

        database_parts = self.database.get_all_data()

        self.assertDictEqual(database_parts, car_parts)

    def test_add_part(self):
        '''Test Case 13'''

        new_part = CarPart(id=0, name='new part', count=1, price=2.33,
                           manufacturer='new manufacturer', category='new category')

        self.database.add_part(new_part)

        self.cursor.execute('SELECT * FROM car_parts')
        result = self.cursor.fetchall()

        self.assertEqual(result, [(1, 'test name', 10, 20.00, 'test manufacturer', 'test category'),
                                  (2, 'random', 1000, 10.50, 'manu', 'cat'),
                                  (3, 'car part', 275, 5.00, 'abc', 'abc'),
                                  (4, 'tires', 5000, 50.00,
                                   'Apollo Tyres', 'tires'),
                                  (5, 'name', 856, 1.25, 'xyz', 'xyz'),
                                  (6, 'new part', 1, 2.33, 'new manufacturer', 'new category')])

    def test_delete_part(self):
        '''Test Case 14'''

        self.database.delete_part(2)

        self.cursor.execute('SELECT * FROM car_parts')
        result = self.cursor.fetchall()

        self.assertEqual(result, [(1, 'test name', 10, 20.00, 'test manufacturer', 'test category'),
                                  (3, 'car part', 275, 5.00, 'abc', 'abc'),
                                  (4, 'tires', 5000, 50.00,
                                   'Apollo Tyres', 'tires'),
                                  (5, 'name', 856, 1.25, 'xyz', 'xyz'), ])

    def test_update_part(self):
        '''Test Case 15'''

        updated_part = CarPart(id=2, name='updated name', count=1624, price=68.53,
                               manufacturer='updated manufacturer', category='updated category')

        self.database.update_part(2, updated_part)

        self.cursor.execute('SELECT * FROM car_parts')
        result = self.cursor.fetchall()

        self.assertEqual(result, [(1, 'test name', 10, 20.00, 'test manufacturer', 'test category'),
                                  (2, 'updated name', 1624, 68.53,
                                   'updated manufacturer', 'updated category'),
                                  (3, 'car part', 275, 5.00, 'abc', 'abc'),
                                  (4, 'tires', 5000, 50.00,
                                   'Apollo Tyres', 'tires'),
                                  (5, 'name', 856, 1.25, 'xyz', 'xyz'), ])

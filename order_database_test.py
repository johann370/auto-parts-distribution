import unittest
import sqlite3
from my_order import Order
from sqlite_order_database import SQLiteOrderDatabase
import json


class TestDatabaseMethods(unittest.TestCase):
    def setUp(self):
        self.database = SQLiteOrderDatabase(
            connection=sqlite3.connect(':memory:'))
        self.conn = self.database.connection
        self.cursor = self.conn.cursor()

        self.cursor.execute(
            'CREATE TABLE orders(order_id INTEGER PRIMARY KEY, first_name, last_name, address, total, car_parts, card_number)')

        data = [('first', 'last', 'address', 1000.0,
                 '[{"id": 1, "count": 10}, {"id": 2, "count": 200}]', '1111 1111 1111 1111'),
                ('john', 'john', 'my street st', 50.0,
                 '[{"id": 1, "count": 20}, {"id": 2, "count": 500}]', '1111 1111 1111 1111')]

        self.cursor.executemany(
            'INSERT INTO orders(first_name, last_name, address, total, car_parts, card_number) VALUES (?, ?, ?, ?, ?, ?)', data)

        self.conn.commit()

    def tearDown(self):
        self.conn.close()

    def test_add_order(self):
        '''Test Case 17'''

        new_order = Order(order_id=0, first_name='new',
                          last_name='order', address='new address', total=1000, car_parts=json.dumps([{"id": 1, "count": 15}, {"id": 2, "count": 20}]), card_number='1111 1111 1111 1111')

        database_order = self.database.add_order(new_order)

        self.cursor.execute('SELECT * FROM orders')
        result = self.cursor.fetchall()

        self.assertEqual(result, [(1, 'first', 'last', 'address', 1000.0,
                                   '[{"id": 1, "count": 10}, {"id": 2, "count": 200}]', '1111 1111 1111 1111'),
                                  (2, 'john', 'john', 'my street st', 50.0,
                                   '[{"id": 1, "count": 20}, {"id": 2, "count": 500}]', '1111 1111 1111 1111'),
                                  (3, 'new', 'order', 'new address', 1000, '[{"id": 1, "count": 15}, {"id": 2, "count": 20}]', '1111 1111 1111 1111')])

    def test_get_all_orders(self):
        '''Test Case 18'''

        orders = {
            1: Order(order_id=1, first_name='first', last_name='last', address='address', total=1000.0,
                     car_parts=[{"id": 1, "count": 10}, {"id": 2, "count": 200}], card_number='1111 1111 1111 1111'),
            2: Order(order_id=2, first_name='john', last_name='john', address='my street st', total=50.0,
                     car_parts=[{"id": 1, "count": 20}, {"id": 2, "count": 500}], card_number='1111 1111 1111 1111')}

        database_orders = self.database.get_all_data()

        self.assertDictEqual(database_orders, orders)

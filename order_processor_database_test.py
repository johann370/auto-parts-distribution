import unittest
import sqlite3
from Order import Order
from SQLiteOrderDatabase import SQLiteOrderDatabase

class TestDatabaseMethods(unittest.TestCase):
    def setUp(self):
        self.database = SQLiteOrderDatabase(database =':memory:')
        self.conn = self.database.connection
        self.cursor = self.conn.cursor()

        self.cursor.execute('CREATE TABLE orders(order_id INTEGER PRIMARY KEY, parts_received, full_parts_list, full_parts_list_by_name)')
        info = [['1', '1,2', 'part1, part2'],['2', '2,3', 'part2, part3'],['3','4,5,6', 'part4, part5, part6'],['3', '7,8,9', 'part7, part8, part9'],['5', '7,8,9,10,11', 'part7, part8, part9, part10, part11']]
        self.cursor.executemany('INSERT INTO orders(order_id, parts_received, full_parts_list, full_parts_list_by_name) VALUES (?,?,?,?)', info)

        self.conn.commit()

    def tearDown(self):
        self.conn.close()

    def test_get_order(self, order_id):
        orders = Order(order_id= 1, parts_received = '2,3', full_parts_list = '2,3,5', full_parts_list_by_name = 'part2, part3, part5')

        database_order = self.database.get_order(4)

        self.assertEqual(database_order, orders)


        

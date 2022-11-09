import unittest
import sqlite3


class TestDatabaseMethods(unittest.TestCase):
    def setUp(self):
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE test(data)')
        cursor.execute('INSERT INTO test VALUES (10)')
        conn.commit()

    def tearDown(self):
        pass

    def test_something(self):
        print('hi')

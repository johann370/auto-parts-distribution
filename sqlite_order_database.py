import sqlite3
from sqlite3 import Error
from typing import Protocol
from my_order import Order


class SQLiteOrderDatabase():
    def __init__(self, connection) -> None:
        self.connection = connection

    def add_order(self, new_order) -> None:
        query = 'INSERT INTO orders(first_name, last_name, address, total, car_parts, card_number) VALUES(?, ?, ?, ?, ?, ?)'
        cursor = self.connection.cursor()
        cursor.execute(query, (new_order.first_name, new_order.last_name, new_order.address,
                       new_order.total, new_order.car_parts, new_order.card_number))
        self.connection.commit()
        # call the lower_count function of the sqlite_inventory_database through the api

    def create_connection(self, path):
        connection = None
        try:
            connection = sqlite3.connect(path)
            print('Connection to SQLite DB successful')
        except Error as e:
            print(f'The error "{e}" occurred')

        return connection

    def get_all_data(self):
        temp_dict = {}
        result = self.execute_query('SELECT * FROM order')

        for order in result:
            temp_dict[order[0]] = Order(id=order[0])

        return temp_dict

    def execute_query(self, query):
        cursor = self.connection.cursor()
        result = None

        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f'Error: {e}')

    def __str__(self) -> str:
        str_rep = ''
        for order in self.order.values():
            str_rep += f'{order}'
        return str_rep

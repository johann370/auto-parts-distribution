import sqlite3
from sqlite3 import Error
from typing import Protocol
from my_order import Order
import json


class SQLiteOrderDatabase():
    '''Order database class using sqlite'''

    def __init__(self, connection) -> None:
        '''Inits the order database

        :param connection: Connection to database
        :type connection: Database connection
        '''

        self.connection = connection

    def add_order(self, new_order) -> None:
        '''
        This function adds a new order to the order database
        (Requirement 4.6)

        :param new_order: Order to add to the database
        :type new_order: Order
        '''

        query = 'INSERT INTO orders(first_name, last_name, address, total, car_parts, card_number) VALUES(?, ?, ?, ?, ?, ?)'
        cursor = self.connection.cursor()
        cursor.execute(query, (new_order.first_name, new_order.last_name, new_order.address,
                       new_order.total, new_order.car_parts, new_order.card_number))
        self.connection.commit()

    def get_all_data(self):
        '''
        Returns a dict of the orders in the database as Order objects
        (Requirement: 3.7)
        '''

        temp_dict = {}
        result = self.execute_query('SELECT * FROM orders')

        for order in result:
            temp_dict[order[0]] = Order(
                order_id=order[0], first_name=order[1], last_name=order[2], address=order[3], total=order[4], car_parts=json.loads(order[5]), card_number=order[6])

        return temp_dict

    def execute_query(self, query):
        '''Executes a query on the database and returns the result

        :param query: The SQL query to execute
        :type query: str
        :returns: List of entries that match the query
        '''

        cursor = self.connection.cursor()
        result = None

        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f'Error: {e}')

    def __str__(self) -> str:
        '''Returns a string representation of the inventory database'''

        str_rep = ''
        for order in self.order.values():
            str_rep += f'{order}'
        return str_rep

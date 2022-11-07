import sqlite3
from sqlite3 import Error
from typing import Protocol
from Order import Order


class OrderDatabase(Protocol):
    order: dict

    def __init__(self, order={}, database = 'Order.db') -> None:
        self.connection = self.create.connection(database)
		self.order = self.get_all_data()

    def get_order(self, order_id) -> Order:
        return self.order[order_id]

    def add_order(self, new_order) -> None:
        query = 'INSERT INTO order(order_id) VALUES(?)'
		cursor = self.connection.cursor()
		cursor.execute(query, (new_order.order_id))
		self.connection.commit()
		order_id = cursor.lastrowid()
		new_order.id = order_id
		self.order[new_order.id] = new_order



    def delete_order(self, id_to_delete) -> None:
        query = 'DELETE FROM order WHERE id = ?'
		cursor = self.connection.cursor()
		cursor.execute(query, (id_to_delete,))
		self.connection.commit()
		self.inventory.pop(id_to_delete)


	def update_part(self, id_to_update, updated_order) -> None:
		query = 'UPDATE order SET id = ? WHERE id= ?'
		cursor = self.connection.cursor()
		cursor.execute(query,(updated_order.id, id_to_update))
		self.connection.commit()
		self.order[id_to_update] = updated_order
        

	def get_length(self) -> int:
		return len(self.order)

	
	def create_connection(self,path):
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
			temp_dict[order[0]] = Order(id = order[0])

		return temp_dict

	def execute_query(self,query):
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
			str_rep += f'{part}'
		return str_rep 



import sqlite3
from sqlite3 import Error
from CarPart import CarPart


class SQLiteInventoryDatabase:
    inventory: dict

    def __init__(self, inventory={}, database='CarParts.db') -> None:
        self.connection = self.create_connection(database)

    def get_part(self, part_id) -> CarPart:
        query = 'SELECT * FROM car_parts WHERE id = ?'
        cursor = self.connection.cursor()
        cursor.execute(query, (part_id,))
        result = cursor.fetchone()

        car_part = CarPart(id=result[0], name=result[1], count=result[2], price=result[
            3], manufacturer=result[4], category=result[5])

        return car_part

    def add_part(self, new_part) -> None:
        query = 'INSERT INTO car_parts(name, count, price, manufacturer, category) VALUES(?, ?, ?, ?, ?)'
        cursor = self.connection.cursor()
        cursor.execute(query, (new_part.name, new_part.count,
                       new_part.price, new_part.manufacturer, new_part.category))
        self.connection.commit()

    def delete_part(self, id_to_delete) -> None:
        query = 'DELETE FROM car_parts WHERE id = ?'
        cursor = self.connection.cursor()
        cursor.execute(query, (id_to_delete,))
        self.connection.commit()

    def update_part(self, id_to_update, updated_part) -> None:
        query = 'UPDATE car_parts SET name = ?, count = ?, price = ?, manufacturer = ?, category = ? WHERE id = ?'
        cursor = self.connection.cursor()
        cursor.execute(query, (updated_part.name, updated_part.count, updated_part.price,
                       updated_part.manufacturer, updated_part.category, id_to_update))
        self.connection.commit()

    def get_length(self) -> int:
        query = 'SELECT Count(*) FROM car_parts'
        cursor = self.connection.cursor()
        cursor.execute(query)
        length = cursor.fetchone()[0]

        return length

    def create_connection(self, path):
        connection = None
        try:
            connection = sqlite3.connect(path)
        except Error as e:
            print(f'The error "{e}" occurred')

        return connection

    def get_all_data(self):
        temp_dict = {}
        result = self.execute_query('SELECT * FROM car_parts')

        for part in result:
            temp_dict[part[0]] = CarPart(id=part[0], name=part[1], count=part[2], price=part[
                                         3], manufacturer=part[4], category=part[5])

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
        for part in self.inventory.values():
            str_rep += f'{part}'

        return str_rep

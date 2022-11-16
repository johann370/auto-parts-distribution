import sqlite3
from sqlite3 import Error
from car_part import CarPart


class SQLiteInventoryDatabase:
    '''Inventory database class using sqlite'''

    def __init__(self, database='CarParts.db') -> None:
        '''Inits the inventory database

        :param database: Name of sqlite database to connect to
        :type database: str
        '''

        self.connection = self.create_connection(database)

    def get_part(self, part_id) -> CarPart:
        '''
        This function returns a car part from the database that matches the part id

        :param part_id: The part id to search
        :type part_id: int
        :returns: The car part from the database as a CarPart object
        '''

        query = 'SELECT * FROM car_parts WHERE id = ?'
        cursor = self.connection.cursor()
        cursor.execute(query, (part_id,))
        result = cursor.fetchone()

        car_part = CarPart(id=result[0], name=result[1], count=result[2], price=result[
            3], manufacturer=result[4], category=result[5])

        return car_part

    def add_part(self, new_part) -> None:
        '''
        This function adds a new car part to the inventory database

        :param new_part: Car part to add to the database
        :type new_part: CarPart
        '''

        query = 'INSERT INTO car_parts(name, count, price, manufacturer, category) VALUES(?, ?, ?, ?, ?)'
        cursor = self.connection.cursor()
        cursor.execute(query, (new_part.name, new_part.count,
                       new_part.price, new_part.manufacturer, new_part.category))
        self.connection.commit()

    def delete_part(self, id_to_delete) -> None:
        '''
        This function deletes a car part from the inventory database based on id

        :param id_to_delete: The part id to delete
        :type id_to_delete: int
        '''

        query = 'DELETE FROM car_parts WHERE id = ?'
        cursor = self.connection.cursor()
        cursor.execute(query, (id_to_delete,))
        self.connection.commit()

    def update_part(self, id_to_update, updated_part) -> None:
        '''
        This function updates a part's information based on id

        :param id_to_update: The part id to update
        :type id_to_update: int
        :param updated_part: The CarPart object with the updated information
        :type updated_part: CarPart
        '''

        query = 'UPDATE car_parts SET name = ?, count = ?, price = ?, manufacturer = ?, category = ? WHERE id = ?'
        cursor = self.connection.cursor()
        cursor.execute(query, (updated_part.name, updated_part.count, updated_part.price,
                       updated_part.manufacturer, updated_part.category, id_to_update))
        self.connection.commit()

    def get_length(self) -> int:
        '''
        This function returns the number of parts in the inventory database

        :returns: Length of inventory database
        '''

        query = 'SELECT Count(*) FROM car_parts'
        cursor = self.connection.cursor()
        cursor.execute(query)
        length = cursor.fetchone()[0]

        return length

    def create_connection(self, path):
        '''Returns a connection using the path to the database

        :param path: The path to the sqlite database to connect to
        :type path: str
        :returns: The sqlite connection
        '''
        connection = None
        try:
            connection = sqlite3.connect(path)
        except Error as e:
            print(f'The error "{e}" occurred')

        return connection

    def get_all_data(self):
        '''Returns a dict of the car parts in the database as CarPart objects'''

        temp_dict = {}
        result = self.execute_query('SELECT * FROM car_parts')

        for part in result:
            temp_dict[part[0]] = CarPart(id=part[0], name=part[1], count=part[2], price=part[
                                         3], manufacturer=part[4], category=part[5])

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
        for part in self.inventory.values():
            str_rep += f'{part}'

        return str_rep

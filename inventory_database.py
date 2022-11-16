from typing import Protocol

from car_part import CarPart


class InventoryDatabase(Protocol):
    '''Protocol class for the inventory database'''

    def __init__(self, database) -> None:
        '''Inits the inventory database

        :param database: Name of database to connect to
        :type database: str
        '''

        raise NotImplementedError

    def get_part(self, part_id) -> CarPart:
        '''
        This function returns a car part from the database that matches the part id

        :param part_id: The part id to search
        :type part_id: int
        :returns: The car part from the database as a CarPart object
        '''

        raise NotImplementedError

    def add_part(self, new_part) -> None:
        '''
        This function adds a new car part to the inventory database

        :param new_part: Car part to add to the database
        :type new_part: CarPart
        '''

        raise NotImplementedError

    def delete_part(self, id_to_delete) -> None:
        '''
        This function deletes a car part from the inventory database based on id

        :param id_to_delete: The part id to delete
        :type id_to_delete: int
        '''

        raise NotImplementedError

    def update_part(self, id_to_update, updated_part) -> None:
        '''
        This function updates a part's information based on id

        :param id_to_update: The part id to update
        :type id_to_update: int
        :param updated_part: The CarPart object with the updated information
        :type updated_part: CarPart
        '''

        raise NotImplementedError

    def get_length(self) -> int:
        '''
        This function returns the number of parts in the inventory database

        :returns: Length of inventory database
        '''

        raise NotImplementedError

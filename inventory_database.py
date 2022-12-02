from typing import Protocol

from car_part import CarPart


class InventoryDatabase(Protocol):
    '''Protocol class for the inventory database'''

    def __init__(self, connection) -> None:
        '''Inits the inventory database

        :param connection: Connection to database
        :type connection: Database connection
        '''

        raise NotImplementedError

    def get_part(self, part_id) -> CarPart:
        '''
        This function returns a car part from the database that matches the part id
        (Requirement: 3.6)

        :param part_id: The part id to search
        :type part_id: int
        :returns: The car part from the database as a CarPart object
        '''

        raise NotImplementedError

    def add_part(self, new_part) -> None:
        '''
        This function adds a new car part to the inventory database
        (Requirement: 3.8)

        :param new_part: Car part to add to the database
        :type new_part: CarPart
        '''

        raise NotImplementedError

    def delete_part(self, id_to_delete) -> None:
        '''
        This function deletes a car part from the inventory database based on id
        (Requirement: 3.9)

        :param id_to_delete: The part id to delete
        :type id_to_delete: int
        '''

        raise NotImplementedError

    def update_part(self, id_to_update, updated_part) -> None:
        '''
        This function updates a part's information based on id
        (Requirement: 3.10)

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

    def lower_count(self, id_to_lower, amount_to_lower) -> None:
        '''
        This function lowers the count of a car part by a certain amount
        (Requirement: 3.11)

        :param id_to_lower: The part id to lower
        :type id_to_lower: int
        :param amount_to_lower: The amount to remove from the count
        :type amount_to_lower: int
        '''

        raise NotImplementedError

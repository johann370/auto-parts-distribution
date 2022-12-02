from typing import Protocol

from my_order import Order


class OrderDatabase(Protocol):
    '''Protocol class for the order database'''

    def __init__(self, connection) -> None:
        '''Inits the order database

        :param connection: Connection to database
        :type connection: Database connection
        '''

        raise NotImplementedError

    def add_order(self, new_order) -> None:
        '''
        This function adds a new order to the order database
        (Requirement 4.6)

        :param new_order: Order to add to the database
        :type new_order: Order
        '''
        raise NotImplementedError

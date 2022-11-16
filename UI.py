from typing import Protocol


class UI(Protocol):
    '''Protocol class for the ui'''

    def get_part_info(self) -> dict:
        '''This function gets the car part information from the user

        :returns: A dict of car part information
        '''

        raise NotImplementedError

    def get_updated_info(self, part_to_update) -> dict:
        '''This functions gets the updated information from the user

        :returns: A dict of updated car part information
        '''

        raise NotImplementedError

    def get_part_to_delete(self) -> int:
        '''Gets the part id to delete

        :returns: An int of the part id
        '''

        raise NotImplementedError

    def get_part_to_update(self) -> int:
        '''Gets the part id to update

        :returns: An int of the part id
        '''

        raise NotImplementedError

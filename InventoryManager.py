from CarPart import CarPart
from InventoryDatabase import InventoryDatabase
from UI import UI


class InventoryManager:
    def __init__(self, ui: UI, inventory: InventoryDatabase) -> None:
        '''Inits the inventory manager

        :param ui: The ui to get user input
        :type ui: UI
        :param inventory: The instance of the database 
        :type inventory: InventoryDatabase
        '''
        self.inventory = inventory
        self.ui = ui

    def add_part(self):
        '''Gets part info through ui and adds the part to the database'''
        part_info = self.ui.get_part_info()
        new_part = CarPart(id=self.inventory.get_length() + 1, name=part_info['name'], count=part_info['count'],
                           price=part_info['price'], manufacturer=part_info['manufacturer'], category=part_info['category'])

        self.inventory.add_part(new_part)

    def delete_part(self):
        '''Gets id to delete from ui and deletes the part from the database'''
        id_to_delete = self.ui.get_part_to_delete()

        self.inventory.delete_part(id_to_delete)

    def update_part(self):
        '''Gets id and updated part info from the user and updates the databse'''
        id_to_update = self.ui.get_part_to_update()
        updated_info = self.ui.get_updated_info(
            self.inventory.get_part(id_to_update))
        updated_part = CarPart(id=id_to_update, name=updated_info['name'], count=updated_info['count'],
                               price=updated_info['price'], manufacturer=updated_info['manufacturer'], category=updated_info['category'])

        self.inventory.update_part(id_to_update, updated_part)

    def display_parts(self):
        '''Displays the inventory'''
        print(self.inventory)

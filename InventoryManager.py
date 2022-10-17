from CarPart import CarPart
from Database import Database
from UI import UI


class InventoryManager:
    def __init__(self, ui: UI, inventory: Database) -> None:
        self.inventory = inventory
        self.ui = ui

    def add_part(self):
        part_info = self.ui.get_part_info()
        new_part = CarPart(id=self.inventory.get_length() + 1, name=part_info['name'], count=part_info['count'],
                           price=part_info['price'], manufacturer=part_info['manufacturer'], category=part_info['category'])

        self.inventory.add_part(new_part)

    def delete_part(self):
        id_to_delete = self.ui.get_part_to_delete()

        self.inventory.delete_part(id_to_delete)

    def update_part(self):
        id_to_update = self.ui.get_part_to_update()
        updated_info = self.ui.get_updated_info(
            self.inventory.get_part(id_to_update))
        updated_part = CarPart(id=id_to_update, name=updated_info['name'], count=updated_info['count'],
                               price=updated_info['price'], manufacturer=updated_info['manufacturer'], category=updated_info['category'])

        self.inventory.update_part(id_to_update, updated_part)

    def display_parts(self):
        print(self.inventory)

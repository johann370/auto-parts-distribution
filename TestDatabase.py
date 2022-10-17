from CarPart import CarPart


class TestDatabase:
    inventory: dict

    def __init__(self, inventory={}) -> None:
        self.inventory = inventory

    def get_part(self, part_id) -> CarPart:
        return self.inventory[part_id]

    def add_part(self, new_part) -> None:
        self.inventory[new_part.id] = new_part

    def delete_part(self, id_to_delete) -> None:
        self.inventory.pop(id_to_delete)

    def update_part(self, id_to_update, updated_part) -> None:
        self.inventory[id_to_update] = updated_part

    def get_length(self) -> int:
        return len(self.inventory)

    def __str__(self) -> str:
        str_rep = ''
        for part in self.inventory.values():
            str_rep += f'{part}'

        return str_rep

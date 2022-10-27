from typing import Protocol

from CarPart import CarPart


class Database(Protocol):
    inventory: dict

    def __init__(self, inventory={}) -> None:
        raise NotImplementedError

    def get_part(self, part_id) -> CarPart:
        raise NotImplementedError

    def add_part(self, new_part) -> None:
        raise NotImplementedError

    def delete_part(self, id_to_delete) -> None:
        raise NotImplementedError

    def update_part(self, id_to_update, updated_part) -> None:
        raise NotImplementedError

    def get_length(self) -> int:
        raise NotImplementedError

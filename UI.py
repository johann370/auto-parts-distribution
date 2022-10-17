from typing import Protocol


class UI(Protocol):
    def get_part_info(self) -> dict:
        raise NotImplementedError

    def get_updated_info(self, part_to_update) -> dict:
        raise NotImplementedError

    def get_part_to_delete(self) -> int:
        raise NotImplementedError

    def get_part_to_update(self) -> int:
        raise NotImplementedError

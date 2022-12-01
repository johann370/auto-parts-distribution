from typing import Protocol

from order import Order


class OrderDatabase(Protocol):
    order: dict

    def __init__(self, order={}) -> None:
        raise NotImplementedError

    def get_order(self, order_id) -> Order:
        raise NotImplementedError

    def add_order(self, new_order) -> None:
        raise NotImplementedError

    def delete_order(self, id_to_delete) -> None:
        raise NotImplementedError

    def update_order(self, id_to_update, updated_order) -> None:
        raise NotImplementedError

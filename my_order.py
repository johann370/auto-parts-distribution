from dataclasses import dataclass


@dataclass
class Order:
    '''Class for storing order information'''

    order_id: int
    first_name: str
    last_name: str
    address: str
    car_parts: str
    card_number: str
    total: float

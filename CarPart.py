from dataclasses import dataclass


@dataclass
class CarPart:
    '''Class for storing information of a car part in the inventory'''
    id: int
    name: str
    count: int
    price: float
    manufacturer: str
    category: str

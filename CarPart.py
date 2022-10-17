from dataclasses import dataclass


@dataclass
class CarPart:
    id: int
    name: str
    count: int
    price: float
    manufacturer: str
    category: str

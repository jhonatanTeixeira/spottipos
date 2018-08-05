from typing import List
from dataclasses import dataclass
import pandas as pd

world = pd.DataFrame(
    [
        ['Gode', [0, 1000], [600, 1000], [0, 500], [600, 500]],
        ['Ruja', [400, 1000], [1100, 1000], [400, 500], [1100, 500]],
        ['Jaby', [1100, 1000], [1400, 1000], [1100, 500], [1400, 500]],
        ['Scavy', [0, 500], [600, 500], [0, 0], [600, 0]],
        ['Groola', [600, 500], [800, 500], [600, 0], [800, 0]],
        ['Nova', [800, 500], [1400, 500], [800, 0], [1400, 0]],
    ],
    columns=['region', 'a', 'b', 'c', 'd']
)

properties = pd.DataFrame(
    [],
    columns=['x', 'y', 'title', 'price', 'description', 'beds', 'baths', 'squareMeters', 'provinces']
)


@dataclass(frozen=True)
class Province:
    name: str
    a: list
    b: list
    c: list
    d: list


@dataclass()
class Property:
    title: str
    x: int
    y: int
    price: int
    description: str
    beds: int
    baths: int
    squareMeters: int
    id: int = None
    provinces: List[str] = None

    def __post_init__(self):
        assert self.x <= 1400, 'out of bounds x'
        assert self.y <= 1000, 'out of bounds y'

    def with_id(self, id: int) -> 'Property':
        self.id = id

        return self


@dataclass(frozen=True)
class Area:
    ax: int
    ay: int
    bx: int
    by: int
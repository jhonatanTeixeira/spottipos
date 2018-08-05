from typing import List
from pandas import DataFrame
from app.domain.model import Property, Province, Area


class WorldService():
    def __init__(self, world: DataFrame, properties: DataFrame):
        self.world = world
        self.properties = properties

    def property_provinces(self, property: Property) -> List[Province]:
        provinces = []

        for id, province in self.world.iterrows():
            a = province['a']
            b = province['b']
            c = province['c']
            d = province['d']

            if (a[0] < property.x < d[0]
                    and d[1] < property.y < a[1]):
                provinces.append(Province(province['region'], a, b, c, d))

        if len(provinces) == 0:
            raise ValueError('Property has invalid coordinates')

        return provinces

    def add_property(self, property: Property):
        property.provinces = [province.name for province in self.property_provinces(property)];

        dict = property.__dict__
        data = DataFrame([dict], columns=dict.keys())
        self.properties = self.properties.append([data], ignore_index=True)

        index = self.properties.index[-1]

        property.id = index

    def get_property_by_id(self, id: int):
        data = self.properties.ix[int(id)].to_dict()

        property = Property(**data)
        property.id = id

        return property

    def get_properties(self, area: Area = None) -> List[Property]:
        if area is not None:
            properties = self.properties.query('%d < x < %d and %d > y > %d' % (area.ax, area.bx, area.ay, area.by))
        else:
            properties = self.properties

        return [Property(**property.to_dict()).with_id(int(index)) for index, property in properties.iterrows()]
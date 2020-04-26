from main.ua.lviv.iot.models.Size import Size
from main.ua.lviv.iot.models.Toy import Toy
from abc import ABC


class Car(Toy, ABC):
    def __init__(self, color, door_count, length_in_mm, price_in_UAH, age_group,
                 size: Size):
        super().__init__(price_in_UAH, age_group, size)
        self.color = color
        self.door_count = door_count
        self.length_in_mm = length_in_mm

    def __str__(self):
        return super().__str__() + ", color = {}, door count = {}, length in " \
                                   "mm = {}".format(
            self.color,
            self.door_count,
            self.length_in_mm)

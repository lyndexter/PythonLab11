from main.ua.lviv.iot.models.Size import Size
from main.ua.lviv.iot.models.Toy import Toy


class Cube(Toy):

    def __init__(self, color, filler, price_in_UAH, age_group, size: Size):
        super().__init__(price_in_UAH, age_group, size)
        self.color = color
        self.filler = filler
        self.type_of_toy = "Cube"

    def __str__(self):
        return super().__str__() + ", color = {}, filler = {}]".format(
            self.color, self.filler)

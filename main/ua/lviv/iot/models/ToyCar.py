from main.ua.lviv.iot.models.Car import Car
from main.ua.lviv.iot.models.Size import Size


class ToyCar(Car):
    def __init__(self, material, color, door_count, length_in_mm, price_in_UAH,
                 age_group, size: Size):
        super().__init__(color, door_count, length_in_mm, price_in_UAH,
                         age_group, size)
        self.material = material
        self.type_of_toy = "ToyCar"

    def __str__(self):
        return super().__str__() + ", material = {}]".format(self.material)

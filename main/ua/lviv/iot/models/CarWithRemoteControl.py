from main.ua.lviv.iot.models.Car import Car
from main.ua.lviv.iot.models.Size import Size


class CarWithRemoteControl(Car):
    def __init__(self, battery_capacity_in_mah, color, door_count, length_in_mm,
                 price_in_UAH, age_group, size: Size):
        super().__init__(color, door_count, length_in_mm, price_in_UAH,
                         age_group, size)
        self.battery_capacity_in_mah = battery_capacity_in_mah
        self.type_of_toy = "CarWithRemoteControl"

    def __str__(self):
        return super().__str__() + ", battery capacity in mah = {}]".format(
            self.battery_capacity_in_mah)

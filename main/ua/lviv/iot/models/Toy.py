from main.ua.lviv.iot.models.Size import Size


class Toy:
    def __init__(self, price_in_UAH, age_group, size: Size):
        super().__init__()
        self.price_in_UAH = price_in_UAH
        self.age_group = age_group
        self.size = size
        self.type_of_toy = None

    def __str__(self):
        return "[price in UAH = {}, age group = {}, size = {}".format(
            self.price_in_UAH, self.age_group, self.size)

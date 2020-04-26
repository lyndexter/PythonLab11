from main.ua.lviv.iot.models.Size import Size
from main.ua.lviv.iot.models.Toy import Toy


class Doll(Toy):
    def __init__(self, color_of_eyes, phrase, price_in_UAH, age_group,
                 size: Size):
        super().__init__(price_in_UAH, age_group, size)
        self.color_of_eyes = color_of_eyes
        self.phrase = phrase
        self.type_of_toy = "Doll"

    def say_phrase(self):
        print(self.phrase)

    def __str__(self):
        return super().__str__() + ", color of eyes = {}, phrase = {}]".format(
            self.color_of_eyes, self.phrase)

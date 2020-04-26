from main.ua.lviv.iot.models.BallType import BallType
from main.ua.lviv.iot.models.Size import Size
from main.ua.lviv.iot.models.Toy import Toy
from abc import ABC


class Ball(Toy, ABC):
    def __init__(self, type_of_ball: BallType, price_in_UAH, age_group,
                 size: Size):
        super().__init__(price_in_UAH, age_group, size)
        self.type_of_ball = type_of_ball
        self.type_of_toy = "Ball"

    def __str__(self):
        return super().__str__() + ", type of ball = {}]".format(
            self.type_of_ball)

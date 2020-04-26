from main.ua.lviv.iot.models.Size import Size
from main.ua.lviv.iot.models.Toy import Toy
from main.ua.lviv.iot.models.ToyCar import ToyCar


class ToyManager:
    def __init__(self, toys):
        self.toys = toys

    def add_toy(self, toy: Toy):
        self.toys.append(toy)

    def add_toys(self, toys: list):
        self.toys.extend(toys)

    def find_by_size(self, size: Size):
        """
        function return object with specific size
        >>> print(toy_manager.find_by_size(Size.Small)[1])
        [price in UAH = 450, age group = 8, size = Size.Small, color = black, door count = 4, length in mm = 150, material = Metal]
        """
        return list(filter(lambda toy: toy.size == size, self.toys))

    def find_by_age_group(self, age_group):
        """
        function return object with specific age group
        >>> print(toy_manager.find_by_age_group(7)[0])
        [price in UAH = 400, age group = 7, size = Size.Small, color = yellow, door count = 4, length in mm = 150, material = Metal]
        """
        return list(filter(lambda toy: toy.age_group == age_group, self.toys))

    def find_by_price_in_UAH(self, price_in_UAH):
        """
        function return object with specific price
        >>> print(toy_manager.find_by_price_in_UAH(400)[0])
        [price in UAH = 400, age group = 7, size = Size.Small, color = yellow, door count = 4, length in mm = 150, material = Metal]
        """
        return list(filter(lambda toy: toy.price_in_UAH == price_in_UAH, self.toys))


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True, extraglobs={'toy_manager': ToyManager(
        [ToyCar("Metal", "yellow", 4, 150, 400, 7, Size.Small), ToyCar("Metal", "black", 4, 150, 450, 8, Size.Small),
         ToyCar("Metal", "yellow", 4, 150, 460, 8, Size.Large),
         ToyCar("Metal", "yellow", 4, 150, 400, 7, Size.Small)])})
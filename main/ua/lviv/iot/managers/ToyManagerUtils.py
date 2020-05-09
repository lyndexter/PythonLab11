from typing import List

from main.ua.lviv.iot.models.Size import Size
from main.ua.lviv.iot.models.SortType import SortType
from main.ua.lviv.iot.models.Toy import Toy
from main.ua.lviv.iot.models.ToyCar import ToyCar


class ToyManagerUtils:
    @staticmethod
    def sort_by_price(toys: List[Toy], sort_type: SortType):
        """
        return sorted object by price
        >>> for i in ToyManagerUtils.sort_by_price(toys,SortType.Ascending): print(i)
        [price in UAH = 400, age group = 7, size = Size.Small, color = yellow, door count = 4, length in mm = 150, material = Metal]
        [price in UAH = 400, age group = 7, size = Size.Small, color = yellow, door count = 4, length in mm = 150, material = Metal]
        [price in UAH = 450, age group = 8, size = Size.Small, color = black, door count = 4, length in mm = 150, material = Metal]
        [price in UAH = 460, age group = 8, size = Size.Large, color = yellow, door count = 4, length in mm = 150, material = Metal]
       """
        toys.sort(key=lambda toy: toy.price_in_UAH, reverse=sort_type.value)
        return toys

    @staticmethod
    def sort_by_age_group(toys: List[Toy], sort_type: SortType):
        """
        return sorted object by age group
        >>> print(ToyManagerUtils.sort_by_age_group(toys,SortType.Ascending)[2])
        [price in UAH = 450, age group = 8, size = Size.Small, color = black, door count = 4, length in mm = 150, material = Metal]
        """
        toys.sort(key=lambda toy: toy.age_group, reverse=sort_type.value)
        return toys

    @staticmethod
    def sort_by_size(toys: List[Toy], sort_type: SortType):
        """
        return sorted object by size
        >>> print(ToyManagerUtils.sort_by_size(toys,SortType.Ascending)[0])
        [price in UAH = 460, age group = 8, size = Size.Large, color = yellow, door count = 4, length in mm = 150, material = Metal]
        """
        toys.sort(key=lambda toy: str(toy.size), reverse=sort_type.value)
        return toys

    @staticmethod
    def sort_by_type(toys: List[Toy], sort_type: SortType):
        """
        return sorted object by type of toy
        >>> print(ToyManagerUtils.sort_by_type(toys,SortType.Ascending)[2])
        [price in UAH = 400, age group = 7, size = Size.Small, color = yellow, door count = 4, length in mm = 150, material = Metal]
        """
        toys.sort(key=lambda toy: toy.type_of_toy, reverse=sort_type.value)
        return toys


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True, extraglobs={
        'toys': [ToyCar("Metal", "yellow", 4, 150, 400, 7, Size.Small),
                 ToyCar("Metal", "black", 4, 150, 450, 8, Size.Small),
                 ToyCar("Metal", "yellow", 4, 150, 460, 8, Size.Large),
                 ToyCar("Metal", "yellow", 4, 150, 400, 7, Size.Small)]})

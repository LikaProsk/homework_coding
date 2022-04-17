import math

from src.Figure import Figure


class Circle(Figure):
    def __init__(self, r: float):
        self.r = r
        if self.check_create_figure():
            self.name = 'Circle'
            self.area = self._area()
            self.perimeter = self._perimeter()

    def _area(self):
        return math.pi * (self.r ** 2)

    def _perimeter(self):
        return 2 * math.pi * self.r

    def check_create_figure(self):
        if self._check_side_type(self.r):
            if self._is_more_than_zero(self.r):
                return True

        return False

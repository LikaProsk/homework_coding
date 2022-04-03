import math

from src.Figure import Figure


class Triangle(Figure):
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c
        if self.check_create_figure():
            self.name = 'Triangle'
            self.area = self._area()
            self.perimeter = self._perimeter()

    def _area(self):
        p = self.__semi_perimeter()
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def __semi_perimeter(self):
        return (self.a + self.b + self.c) / 2

    def _perimeter(self):
        return self.a + self.b + self.c

    def check_create_figure(self):
        if self._check_side_type(self.a) and self._check_side_type(self.b) and self._check_side_type(self.c):
            if self._is_more_than_zero(self.a) and self._is_more_than_zero(self.b) and self._is_more_than_zero(self.c):
                if self.a <= self.b + self.c or self.b <= self.a + self.c or self.c <= self.b + self.a:
                    return True

        return False

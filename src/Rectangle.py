from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b
        if self.check_create_figure():
            self.name = 'Rectangle'
            self.area = self._area()
            self.perimeter = self._perimeter()

    def _area(self):
        return self.a * self.b

    def _perimeter(self):
        return 2 * (self.a + self.b)

    def check_create_figure(self):
        if self._check_side_type(self.a) and self._check_side_type(self.b):
            if self._is_more_than_zero(self.a) and self._is_more_than_zero(self.b):
                return True

        return False

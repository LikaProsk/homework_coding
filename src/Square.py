from src.Figure import Figure


class Square(Figure):
    def __init__(self, a: float):
        self.a = a
        if self.check_create_figure():
            self.name = 'Square'
            self.area = self._area()
            self.perimeter = self._perimeter()

    def _area(self):
        return self.a ** 2

    def _perimeter(self):
        return self.a * 4

    def check_create_figure(self):
        if self._check_side_type(self.a):
            if self._is_more_than_zero(self.a):
                return True

        return False

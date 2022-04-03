class Figure:
    name = None
    area = None
    perimeter = None

    def _check_side_type(self, side):
        return isinstance(side, int) or isinstance(side, float)

    def _is_more_than_zero(self, side):
        return side > 0

    def add_area(self, figure: object):
        if not hasattr(figure, 'area') or figure.area is None:
            raise ValueError('Wrong figure class')
        return self.area + figure.area

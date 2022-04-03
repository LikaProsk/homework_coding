import pytest

from src.Square import Square
from src.Triangle import Triangle


@pytest.mark.parametrize('a, b, c', [(10, 10, 10), (10.5, 10.5, 5)])
def test_figure_name_positive(a, b, c):
    triangle = Triangle(a, b, c)
    assert triangle.name == 'Triangle'


@pytest.mark.parametrize('a, b, c', [(10, 0, 10), (0, 10.5, 5), (10, 10, 0), (0, 0, 0), (0, 0, 10), (10, 0, 0),
                                     (0, 10.5, 0), (-10, 10, 10), (10.5, -10, 10), (10, 10, -10), (-10, -10, -10)])
def test_figure_name_negative(a, b, c):
    triangle = Triangle(a, b, c)
    assert triangle.name is None


@pytest.mark.parametrize('a, b, c, area', [(10, 10, 10, 43.30), (10.5, 10.5, 5, 25.495098)])
def test_area_positive(a, b, c, area):
    triangle = Triangle(a, b, c)
    assert round(triangle.area, 2) == round(area, 2)


@pytest.mark.parametrize('a, b, c', [(10, 0, 10), (0, 10.5, 5), (10, 10, 0), (0, 0, 0), (0, 0, 10), (10, 0, 0),
                                     (0, 10.5, 0), (-10, 10, 10), (10.5, -10, 10), (10, 10, -10), (-10, -10, -10)])
def test_area_negative(a, b, c):
    triangle = Triangle(a, b, c)
    assert triangle.area is None


@pytest.mark.parametrize('a, b, c, perimeter', [(10, 10, 10, 30), (10.5, 10.5, 5, 26)])
def test_perimeter_positive(a, b, c, perimeter):
    triangle = Triangle(a, b, c)
    assert triangle.perimeter == perimeter


@pytest.mark.parametrize('a, b, c', [(10, 0, 10), (0, 10.5, 5), (10, 10, 0), (0, 0, 0), (0, 0, 10), (10, 0, 0),
                                     (0, 10.5, 0), (-10, 10, 10), (10.5, -10, 10), (10, 10, -10), (-10, -10, -10)])
def test_perimeter_negative(a, b, c):
    triangle = Triangle(a, b, c)
    assert triangle.perimeter is None


@pytest.mark.parametrize('a, b, c, square_side, area_sum', [(10, 10, 10, 30, 943.3), (10.5, 10.5, 5, 26, 701.5)])
def test_add_area_square_positive(a, b, c, square_side, area_sum):
    triangle = Triangle(a, b, c)
    assert round(triangle.add_area(Square(square_side)), 2) == round(area_sum, 2)


@pytest.mark.parametrize('figure', [10, 'str', 0, None])
def test_add_area_negative(figure):
    triangle = Triangle(10, 10, 10)
    try:
        triangle.add_area(figure)
        pytest.fail('Incorrect result for negative test')
    except ValueError as error:
        assert 'Wrong figure class' in error.args

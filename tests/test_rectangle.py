import pytest

from src.Circle import Circle
from src.Rectangle import Rectangle


@pytest.mark.parametrize('a, b', [(10, 20), (10.5, 15.5)])
def test_figure_name_positive(a, b):
    rectangle = Rectangle(a, b)
    assert rectangle.name == 'Rectangle'


@pytest.mark.parametrize('a, b', [(10, 0), (0, 10.5), (0, 0), (-10, 16), (10.5, -20.6), (-20, -50.6)])
def test_figure_name_negative(a, b):
    rectangle = Rectangle(a, b)
    assert rectangle.name is None


@pytest.mark.parametrize('a, b, area', [(10, 30, 300), (10.5, 16.5, 173.25)])
def test_area_positive(a, b, area):
    rectangle = Rectangle(a, b)
    assert round(rectangle.area, 2) == round(area, 2)


@pytest.mark.parametrize('a, b', [(10, 0), (0, 10.5), (0, 0), (-10, 20), (10.5, -30), (-10, -40)])
def test_area_negative(a, b):
    rectangle = Rectangle(a, b)
    assert rectangle.area is None


@pytest.mark.parametrize('a, b, perimeter', [(10, 20, 60), (10.5, 15.5, 52)])
def test_perimeter_positive(a, b, perimeter):
    rectangle = Rectangle(a, b)
    assert rectangle.perimeter == perimeter


@pytest.mark.parametrize('a, b', [(100, 0), (0, 205.5), (0, 0), (-106.4, 10), (10.5, -104.9), (-1000, -900)])
def test_perimeter_negative(a, b):
    rectangle = Rectangle(a, b)
    assert rectangle.perimeter is None


@pytest.mark.parametrize('a, b, circle_side, area_sum', [(10, 20, 30, 3027.43), (10.5, 20.5, 32.2, 3472.58)])
def test_add_area_square_positive(a, b, circle_side, area_sum):
    rectangle = Rectangle(a, b)
    assert round(rectangle.add_area(Circle(circle_side)), 2) == round(area_sum, 2)


@pytest.mark.parametrize('figure', [10, 'str', 0, None])
def test_add_area_negative(figure):
    rectangle = Rectangle(100, 200)
    try:
        rectangle.add_area(figure)
        pytest.fail('Incorrect result for negative test')
    except ValueError as error:
        assert 'Wrong figure class' in error.args

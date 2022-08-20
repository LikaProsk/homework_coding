import pytest

from src.Circle import Circle
from src.Rectangle import Rectangle


@pytest.mark.parametrize('r', [10, 20.5])
def test_figure_name_positive(r):
    circle = Circle(r)
    assert circle.name == 'Circle'


@pytest.mark.parametrize('r', [0, -10.5])
def test_figure_name_negative(r):
    circle = Circle(r)
    assert circle.name is None


@pytest.mark.parametrize('r, area', [(10, 314.16), (10.5, 346.36)])
def test_area_positive(r, area):
    circle = Circle(r)
    assert round(circle.area, 2) == round(area, 2)


@pytest.mark.parametrize('r', [0, -10.5])
def test_area_negative(r):
    circle = Circle(r)
    assert circle.area is None


@pytest.mark.parametrize('r, perimeter', [(10, 62.83), (13.2, 82.94)])
def test_perimeter_positive(r, perimeter):
    circle = Circle(r)
    assert round(circle.perimeter, 2) == round(perimeter, 2)


@pytest.mark.parametrize('r', [-10, 0])
def test_perimeter_negative(r):
    circle = Circle(r)
    assert circle.perimeter is None


@pytest.mark.parametrize('r, rectangle_side_a, rectangle_side_b, area_sum', [(10, 20, 15, 614.16),
                                                                             (10.5, 12.5, 15.6, 541.36)])
def test_add_area_rectangle_positive(r, rectangle_side_a, rectangle_side_b, area_sum):
    circle = Circle(r)
    assert round(circle.add_area(Rectangle(rectangle_side_a, rectangle_side_b)), 2) == round(area_sum, 2)


@pytest.mark.parametrize('figure', [10, 'str', 0, None])
def test_add_area_negative(figure):
    circle = Circle(40)
    try:
        circle.add_area(figure)
        pytest.fail('Incorrect result for negative test')
    except ValueError as error:
        assert 'Wrong figure class' in error.args

#PRUEBA TEST 5

import pytest
from min_max_calculator import min_max_funtion

@pytest.mark.parametrize('number_list, expected', [
    ([1, 2, 3, 4, 5], (1, 5)),
    ([10, 20, 30, 40, 50], (10, 50)),
    ([0, 0, 0, 0, 0], (0, 0)),
    ([-5, -3, 0, 3, 5], (-5, 5)),

])
def test_min_max_function(number_list, expected):
    assert min_max_funtion(number_list) == expected
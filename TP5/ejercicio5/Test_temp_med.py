#PRUEBA TEST 3

import pytest
from temp_med import temp_med_funtion

@pytest.mark.parametrize('max_temp, min_temp, expected', [
    (30, 15, 22.5),
    (24, 40, 32),
    (3, 34, 18.5),
    (0, 0, 0),
    (-10, 10, 0), 
])
def test_multiples(max_temp, min_temp, expected):
    assert temp_med_funtion(max_temp, min_temp) == expected
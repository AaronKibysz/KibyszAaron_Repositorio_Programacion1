import pytest
from suma_cifras import number_addition

@pytest.mark.parametrize("number, res",[
    (12,3),
    (99,18),
    (10,1),
    (45,9),
])
def test_cifras(number, res):
    assert number_addition(number) == res
import pytest
from suma_cifras import number_addition

@pytest.mark.paranetrize('a, res',[
    (12,3),
    (99,18),
    (10,1),
    45,9
])
def test_cifras(a, res):
    assert number_addition(a) == res
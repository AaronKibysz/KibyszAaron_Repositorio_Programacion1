# PRUEBA TEST 1

import pytest

from dni_validation import dni_validation_funtion

@pytest.mark.parametrize('dni, expected',[
    ('1234567', True),
    ('98765432', True),
    ('123', False),
    ('987654321', False),
    ('abc123', False),
])
def test_dni(dni, expected):
    assert dni_validation_funtion(dni) == expected
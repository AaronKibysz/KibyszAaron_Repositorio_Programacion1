#PRUEBA TEST 4

import pytest
from separator import separator_funtion

@pytest.mark.parametrize('text, expected', [
        ('Hola', 'H o l a'),
    ('Python', 'P y t h o n'),
    ('123', '1 2 3'),
    ('', ''),
])
def test_separator_funtion(text, expected):
    assert separator_funtion(text) == expected
import pytest

from src.prueba1 import numeromayor

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
      (1, 2, 2),
      (10, 200, 200),
      (200, 10, 200),
    ]
  )
def test_numeromayor_params(input_n1, input_n2, expected):
    assert numeromayor(input_n1, input_n2) == expected
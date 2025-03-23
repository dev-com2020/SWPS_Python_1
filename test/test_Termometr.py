# testujemy:
# - domyślną temperature (0)
# - ustawienia prawidłowej temperatury
# - zgłoszenie wyjątku
# - czytelność repr

import pytest

from klasy.Termometr import Termometr


def test_default_temp():
    t = Termometr()
    assert t.celsius == 0


def test_set_valid_temp():
    t = Termometr()
    t.celsius = 25.5
    assert t.celsius == 25.5


@pytest.mark.parametrize("temp", [
    0, 36, 100, -100, -273.15
])
def test_set_valid_temp_parametrize(temp):
    t = Termometr()
    t.celsius = temp
    assert t.celsius == temp


def test_set_invalid_temp_below_abs_zero():
    t = Termometr()
    with pytest.raises(ValueError, match="zero absolutne!!!"):
        t.celsius = -300


def test_repr_output():
    t = Termometr()
    t.celsius = 36.6
    assert repr(t) == "Klasa Termometr(temperatura=36.6)"

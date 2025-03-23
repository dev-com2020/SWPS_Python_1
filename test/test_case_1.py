import pytest


def test_addition():
    assert 2 + 2 == 45


def test_split():
    s = "a,b,c"
    assert s.split(",") == ['a', 'b', 'c']


@pytest.mark.parametrize("x,y,expected", [
    (2, 3, 5),
    (1, 1, 2),
    (0, 0, 0),
])
def test_add(x, y, expected):
    assert x + y == expected


@pytest.fixture()
def sample_data():
    return {"name": "Ala", "age": 30}


def test_name(sample_data):
    assert sample_data["name"] == "Ala"

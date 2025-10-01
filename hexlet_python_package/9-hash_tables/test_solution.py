import pytest
from solution import get_value


@pytest.fixture
def table():
    return [("d", "zero"), None, None, ("b", "three"), ("m", "hello")]


def test_get_value(table):
    assert get_value(table, "d") == "zero"
    assert get_value(table, "b") == "three"


def test_not_found(table):
    assert get_value(table, "e") == "not found"
    assert get_value(table, "a") == "not found"


def test_collision(table):
    assert get_value(table, "c") == "collision"
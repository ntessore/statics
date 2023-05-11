# type: ignore

import pytest
from consts import consts


class Value:
    def __init__(self, value):
        self.value = value


x, y, z = Value(1), Value(2), Value(3)


def test_consts():
    global x, y, z

    @consts(x, y, z)
    def f():
        x, y, z = "__consts__"
        return x.value, y.value, z.value

    x = y = z = Value(0)

    def g():
        return x.value, y.value, z.value

    del x, y, z

    assert f() == (1, 2, 3)

    with pytest.raises(NameError):
        g()


def test_no_code():
    with pytest.raises(TypeError):
        consts()(object())


def test_no_consts():
    with pytest.raises(ValueError):
        consts()(lambda: None)

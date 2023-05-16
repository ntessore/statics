# type: ignore

import pytest
from bindvar import bind


class Value:
    def __init__(self, value):
        self.value = value


x, y, z = Value(1), Value(2), Value(3)


def test_bind():
    global x, y, z

    @bind(x)
    def f():
        x = "__bound__"
        return x.value

    @bind(x, y, z)
    def g():
        x, y, z = "__bound__"
        return x.value, y.value, z.value

    def h():
        return x.value, y.value, z.value

    del x, y, z

    assert f() == 1
    assert g() == (1, 2, 3)

    with pytest.raises(NameError):
        h()


def test_missing_code():
    with pytest.raises(TypeError):
        bind()(object())


def test_missing_literal():
    with pytest.raises(ValueError):
        bind()(lambda: None)

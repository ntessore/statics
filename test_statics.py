# type: ignore

import pytest
from statics import static


class Value:
    def __init__(self, value):
        self.value = value


x, y, z = Value(1), Value(2), Value(3)


def test_static():
    global x, y, z

    @static(x)
    def f():
        x = "__static__"
        return x.value

    @static(x, y, z)
    def g():
        x, y, z = "__static__"
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
        static()(object())


def test_missing_literal():
    with pytest.raises(ValueError):
        static()(lambda: None)

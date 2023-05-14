# type: ignore

import pytest
import const


class Value:
    def __init__(self, value):
        self.value = value


x, y, z = Value(1), Value(2), Value(3)


def test_store():
    global x, y, z

    @const.store(x)
    def f():
        x = "__const__"
        return x.value

    @const.store(x, y, z)
    def g():
        x, y, z = "__const__"
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
        const.store()(object())


def test_missing_literal():
    with pytest.raises(ValueError):
        const.store()(lambda: None)

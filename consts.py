'''Load variables as consts in Python functions.'''

__version__ = "2023.5.0"

__all__ = ("consts",)

from typing import Any, Callable, TypeVar

F = TypeVar('F', bound=Callable[..., Any])


def consts(*values: Any) -> Callable[[F], F]:
    def decorator(func: F) -> F:
        try:
            co_consts = func.__code__.co_consts
        except AttributeError:
            raise TypeError("consts requires a function object "
                            "with __code__ attribute") from None
        try:
            i = co_consts.index("__consts__")
        except ValueError:
            raise ValueError("no \"__consts__\" literal in function") from None
        co_consts = co_consts[:i] + (values,) + co_consts[i+1:]
        func.__code__ = func.__code__.replace(co_consts=co_consts)
        return func
    return decorator

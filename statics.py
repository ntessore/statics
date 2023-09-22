"""Static objects in Python functions."""

__version__ = "1.0.0"

__all__ = "static",

from typing import Any, Callable, Tuple, TypeVar

F = TypeVar('F', bound=Callable[..., Any])


def _unpack(values: Tuple[Any, ...]) -> Any:
    return values[0] if len(values) == 1 else values


def static(*values: Any) -> Callable[[F], F]:
    def decorator(func: F) -> F:
        try:
            co_consts = func.__code__.co_consts
        except AttributeError:
            raise TypeError("static objects can only be used in functions "
                            "with a __code__ attribute") from None
        try:
            i = co_consts.index("__static__")
        except ValueError:
            raise ValueError("missing \"__static__\" literal "
                             "in function") from None
        co_consts = co_consts[:i] + (_unpack(values),) + co_consts[i+1:]
        func.__code__ = func.__code__.replace(co_consts=co_consts)
        return func
    return decorator

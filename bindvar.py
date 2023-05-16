"""Bind variables to Python functions."""

__version__ = "2023.5.0"

__all__ = ("bind",)

from typing import Any, Callable, Tuple, TypeVar

F = TypeVar('F', bound=Callable[..., Any])


def _unpack(values: Tuple[Any, ...]) -> Any:
    return values[0] if len(values) == 1 else values


def bind(*values: Any) -> Callable[[F], F]:
    def decorator(func: F) -> F:
        try:
            co_consts = func.__code__.co_consts
        except AttributeError:
            raise TypeError("objects can only be bound to functions "
                            "with a __code__ attribute") from None
        try:
            i = co_consts.index("__bound__")
        except ValueError:
            raise ValueError("missing \"__bound__\" literal "
                             "in function") from None
        co_consts = co_consts[:i] + (_unpack(values),) + co_consts[i+1:]
        func.__code__ = func.__code__.replace(co_consts=co_consts)
        return func
    return decorator

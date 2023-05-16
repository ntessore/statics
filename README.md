bindvar
=======

**Bind variables to Python functions**

This is a micropackage with a decorator `@bind` that can be used to bind
objects to Python functions.  The objects can then be loaded into variables in
a function, exactly as they were given, without using globals or closures.

How this works is probably easier shown than explained:

```py
>>> from bindvar import bind
>>>
>>> x = 1
>>>
>>> @bind(x)
... def f():
...     x = "__bound__"
...     print(f"{x=}")
...
>>> del x
>>>
>>> f()
x=1

```

Multiple objects can be bound in a tuple, and assigned to multiple variables:

```py
>>> x, y, z = 1, 2, 3
>>>
>>> @bind(x, y, z)
... def f():
...     x, y, z = "__bound__"
...     print(f"{x=}, {y=}, {z=}")
...
>>> del x, y, z
>>>
>>> f()
x=1, y=2, z=3

```

Variable names in the function do not have to match the names of the bound
objects:

```py
>>> x, y, z = 1, 2, 3
>>>
>>> @bind(x, y, z)
... def f():
...     a, b, c = "__bound__"
...     print(f"{a=}, {b=}, {c=}")
...
>>> del x, y, z
>>>
>>> f()
a=1, b=2, c=3

```

Technically, the binding is achieved by storing the objects in the `co_const`
array of a Python function's code object.  Loading the variables works by
replacing the string literal `"__bound__"` with the bound objects.  The string
`"__bound__"` can therefore not be used for anything else in the decorated
function (strings containing  `"__bound__"` as a substring are not affected).

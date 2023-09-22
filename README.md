statics
=======

**Static objects in Python functions**

This is a micropackage with a decorator `@static` that can be used to achieve
static objects to Python functions.  The objects can then be loaded into
variables in a function, exactly as they were given, without using globals or
closures.

How this works is probably easier shown than explained:

```py
>>> from statics import static
>>>
>>> x = 1
>>>
>>> @static(x)
... def f():
...     x = "__static__"
...     print(f"{x=}")
...
>>> del x
>>>
>>> f()
x=1

```

Multiple static objects can be declared and assigned as a tuple:

```py
>>> x, y, z = 1, 2, 3
>>>
>>> @static(x, y, z)
... def f():
...     x, y, z = "__static__"
...     print(f"{x=}, {y=}, {z=}")
...
>>> del x, y, z
>>>
>>> f()
x=1, y=2, z=3

```

Static names in the function do not have to match the names outside the
function:

```py
>>> x, y, z = 1, 2, 3
>>>
>>> @static(x, y, z)
... def f():
...     a, b, c = "__static__"
...     print(f"{a=}, {b=}, {c=}")
...
>>> del x, y, z
>>>
>>> f()
a=1, b=2, c=3

```

Technically, the static binding is achieved by storing the objects in the
`co_const` array of a Python function's code object.  Loading the variables
works by replacing the string literal `"__static__"` with the static objects.
The string `"__static__"` can therefore not be used for anything else in the
decorated function (but strings containing  `"__static__"` as a substring are
not affected).

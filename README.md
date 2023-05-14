const.store
===========

**Load const objects in Python functions**

This is a micropackage with a decorator `@const.store` that can be used to
store objects in the `co_consts` array of Python functions.  This is a tuple of
constant objects[^1] which are hard-copied into the function definition.  The
objects can then be loaded into variables in a function, exactly as they were
given, without depending on globals or closures.

How this works is probably easier shown than explained:

```py
>>> import const
>>>
>>> x = 1
>>>
>>> @const.store(x)
... def f():
...     x = "__const__"
...     print(f"{x=}")
...
>>> del x
>>>
>>> f()
x=1

```

Multiple objects can be stored in a tuple, and assigned to multiple variables:

```py
>>> x, y, z = 1, 2, 3
>>>
>>> @const.store(x, y, z)
... def f():
...     x, y, z = "__const__"
...     print(f"{x=}, {y=}, {z=}")
...
>>> del x, y, z
>>>
>>> f()
x=1, y=2, z=3

```

Variable names in the function do not have to match the names of the stored
objects:

```py
>>> x, y, z = 1, 2, 3
>>>
>>> @const.store(x, y, z)
... def f():
...     a, b, c = "__const__"
...     print(f"{a=}, {b=}, {c=}")
...
>>> del x, y, z
>>>
>>> f()
a=1, b=2, c=3

```

Loading the variables from `co_consts` relies on replacing the string literal
`"__const__"` with the objects passed to the `@const.store` decorator.  The
string `"__const__"` can hence not be used for anything else in the decorated
function.[^2]


[^1]: "Constant" here refers to the fact that the variable will always point to
      the same object.  The object itself will still be mutable.
[^2]: Strings containing the substring `"__const__"` are not affected.

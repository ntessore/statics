`consts`
========

**Load variables as consts into Python functions**

This is a micropackage with a single decorator `@consts` that can be used to
load variables from the `co_consts` array into Python functions.  Such
variables point to a constant object[^1] that is hard-copied into the
function definition, without depending on globals or closures.

How this works is probably easier shown than explained:

```py
>>> from consts import consts
>>>
>>> x, y, z = 1, 2, 3
>>>
>>> @consts(x, y, z)
... def f():
...     x, y, z = "__consts__"
...     print(x, y, z)
...
>>> del x, y, z
>>>
>>> f()
1 2 3

```

Loading the variables from `co_consts` relies on replacing the string literal
`"__consts__"` with the objects passed to the `@consts` decorator.  You
therefore cannot use the string `"__consts__"` for anything else in the
decorated function.[^2]


[^1]: "Constant" here refers to the fact that the variable will always point to
      the same object.  The object itself is still mutable.
[^2]: Strings containing `"__const__"` as substrings are fine.

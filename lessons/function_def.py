"""An example function definition."""


def my_max(a: int, b: int) -> int:  # signature/"contract"
    # def(reserved name for function definition), 
    # my_max(identifier/name like a variable), 
    # (a: int, b: int)(parameter list, parenthesis surround 
    # variable declarations - order and types of parameters 
    # matter) 
    # -> int: (return type the function call results in)
    """Returns the greatest argument."""  # docstring
    if a >= b:
        return a
    else:
        return b  # body block


print(my_max(10 + 1, 10))
result: int = my_max(-50, 100)
print(result)
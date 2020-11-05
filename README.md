This project demonstrates a simple way to robustly access 
the arguments of a wrapped function in a Python decorator.

This only uses 
[Python's inspect module](https://docs.python.org/3/library/inspect.html).
It'll only work with Python 3.

If you're doing anything more complicated, you probably want 
something like [wrapt](https://pypi.org/project/wrapt/).


```python
from wraps_with_bound_args import wraps_with_bound_args


def my_decorator(func):
    @wraps_with_bound_args(func)
    def wrapper(arguments):
        # See how it's been called.
        print(f"Here's an array of all the args: {arguments.args}")
        print(f"Here's a dict of all the kwargs: {arguments.kwargs}")
        print(f"Here's every argument by name: {arguments.arguments}")
        # Apply and print the defaults
        arguments.apply_defaults()
        print(f"Here's every argument by name, with defaults: {arguments.arguments}")
        # Let's make the surname uppercase
        arguments.arguments["surname"] = arguments.arguments["surname"].upper()
        # Call the function that we've wrapped
        func(*arguments.args, **arguments.kwargs)
    return wrapper


@my_decorator
def greet(forename: str, surname: str, *, greeting: str = "Hello"):
    """
    Greets a named person
    """
    print(f"{greeting} {forename} {surname}")
```
from functools import wraps
from inspect import Signature, BoundArguments
from typing import Callable, Any


DecoratorType = Callable[[Callable], Callable]
WrapperAcceptingBoundArgs = Callable[[BoundArguments], Any]


def wraps_with_bound_args(original_func: Callable) -> DecoratorType:
    """
    For use inside other decorators. Indicates that a function wraps another (like functool's wraps),
    but passes the arguments into the wrapper as single argument, which has the type BoundArguments
    :param original_func: The original function that's being wrapped.
    :return: A decorator
    """
    def decorator(wrapper_func: WrapperAcceptingBoundArgs):
        original_signature = Signature.from_callable(original_func)

        @wraps(original_func)
        def from_args_to_bound_args_obj(*args, **kwargs):
            arguments = original_signature.bind(*args, **kwargs)
            return wrapper_func(arguments)

        return from_args_to_bound_args_obj

    return decorator

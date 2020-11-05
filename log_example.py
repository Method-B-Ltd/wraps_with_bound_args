import logging
import math

from wraps_with_bound_args import wraps_with_bound_args


logging.basicConfig(level=logging.INFO)


def log_calls_with_arguments(func):
    @wraps_with_bound_args(func)
    def wrapper(arguments):
        args_strs = [repr(arg) for arg in arguments.args]
        kwargs_strs = [f"{k}={v!r}" for k, v in arguments.kwargs.items()]
        arg_str = ", ".join(args_strs + kwargs_strs)
        logging.info(f"Called: {func.__name__}({arg_str})")
        arguments.apply_defaults()
        logging.info(f"Argument values with defaults: {arguments.arguments!r}")
        return func(*arguments.args, **arguments.kwargs)
    return wrapper


@log_calls_with_arguments
def calculate_cuboid_volume(length, width=None, height=None):
    if width is None and height is None:
        # It's a cube.
        width = height = length
    return length * width * height


@log_calls_with_arguments
def calculate_cylinder_volume(diameter, height):
    r = diameter / 2
    circ_area = math.pi * r**2
    return circ_area * height


print(calculate_cuboid_volume(3))
print(calculate_cuboid_volume(3, 2, 1))
print(calculate_cylinder_volume(6, 10))


# Output:
# INFO:root:Called: calculate_cuboid_volume(3)
# INFO:root:Argument values with defaults: OrderedDict([('length', 3), ('width', None), ('height', None)])
# 27
# INFO:root:Called: calculate_cuboid_volume(3, 2, 1)
# INFO:root:Argument values with defaults: OrderedDict([('length', 3), ('width', 2), ('height', 1)])
# 6
# INFO:root:Called: calculate_cylinder_volume(6, 10)
# INFO:root:Argument values with defaults: OrderedDict([('diameter', 6), ('height', 10)])
# 282.7433388230814

import math
from typing import Optional

dx = 1e-10


def value_or_none(function, x) -> Optional[float]:
    try:
        value = function(x)
        if math.isfinite(value):
            return value
    except ZeroDivisionError:
        pass


def calculate_value(function, x):
    value = value_or_none(function, x)
    if value is not None:
        return value
    left_limit = value_or_none(function, x - dx)
    right_limit = value_or_none(function, x + dx)
    if (left_limit is None) or (right_limit is None):
        return None
    else:
        return (left_limit + right_limit) / 2

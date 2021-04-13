from calculate import calculate_value
from methods.Method import Method


class TrapezoidalMethod(Method):
    name = "Метод трапеций"

    @staticmethod
    def integrate(f, a, b, partitions) -> float:
        step = (b - a) / partitions
        result = (calculate_value(f, a) + calculate_value(f, b)) / 2
        x = a + step
        while x < b:
            result += calculate_value(f, x)
            x += step
        return result * step

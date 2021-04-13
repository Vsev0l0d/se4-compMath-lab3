from Function import Function
from Result import Result
from calculate import calculate_value
from methods.Method import Method


class RectanglesMethod(Method):
    name = "Метод прямоугольников"

    @staticmethod
    def integrate_left(function, a, b, partitions) -> float:
        step = (b - a) / partitions
        result = 0
        x = a
        while x <= b:
            result += calculate_value(function, x)
            x += step
        return result * step

    @staticmethod
    def integrate_right(function, a, b, partitions) -> float:
        step = (b - a) / partitions
        result = 0
        x = a + step
        while x < b:
            result += calculate_value(function, x)
            x += step
        return result * step

    @staticmethod
    def integrate_middle(function, a, b, partitions) -> float:
        step = (b - a) / partitions
        result = 0
        x = a
        while x < b:
            result += calculate_value(function, x + step / 2)
            x += step
        return result * step

    def solve(self, function: Function, a: float, b: float, epsilon: float, decimal_places: int) -> list:
        left = self.iterate(function.function, self.integrate_left, a, b, epsilon)
        right = self.iterate(function.function, self.integrate_right, a, b, epsilon)
        middle = self.iterate(function.function, self.integrate_middle, a, b, epsilon)

        return [
            Result(left[0], left[1], decimal_places, additional_info=' (левые)'),
            Result(right[0], right[1], decimal_places, additional_info=' (правые)'),
            Result(middle[0], middle[1], decimal_places, additional_info=' (средние)')
        ]

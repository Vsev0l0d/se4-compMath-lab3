import math

from Function import Function
from Result import Result
from calculate import dx

import mainboilerplate
from methods.RectanglesMethod import RectanglesMethod
from methods.SimpsonsMethod import SimpsonsMethod
from methods.TrapezoidalMethod import TrapezoidalMethod

methods = {
    1: RectanglesMethod,
    2: TrapezoidalMethod,
    3: SimpsonsMethod
}

predefined_functions = {
    # Решение на Wolfram: https://cutt.ly/8vqLtZb (96.667)
    1: Function(lambda x: 2 * x ** 3 - 2 * x ** 2 + 7 * x - 14, '2x^3 - 2x^2 + 7x - 14',
                antiderivative=lambda x: 0.5 * x ** 4 - (2 / 3) * x ** 3 + 3.5 * x ** 2 - 14 * x),
    2: Function(lambda x: math.sin(x) / x, 'sin(x) / x'),
    3: Function(lambda x: 1 / x, '1 / x', True, 0,
                antiderivative=lambda x: math.log(x))
}

while True:
    function = mainboilerplate.choose_function(predefined_functions)

    method_number = mainboilerplate.choose_method_number(methods)
    method = methods[method_number]()

    left, right, epsilon, decimal_places = mainboilerplate.read_initial_data()
    if epsilon <= 0:
        print("Точность должна быть больше нуля.")
        continue

    if function.antiderivative is not None:
        i = function.antiderivative(right) - function.antiderivative(left)
        print(f'\nЗначение, вычисленное по формуле Ньютона-лейбница: {i}')

    try:
        print('\nПроцесс решения: ')
        if function.symmetrical and left < function.symmetry_point < right:
            results_left = method.solve(function, left, function.symmetry_point - dx, epsilon, decimal_places)
            results_right = method.solve(function, function.symmetry_point + dx, right, epsilon, decimal_places)

            results = []
            for result in range(len(results_left)):
                l = results_left[result]
                r = results_right[result]
                results.append(Result(
                    l.integral_value + r.integral_value,
                    l.partitions + r.partitions,
                    decimal_places,
                    additional_info=l.additional_info
                ))
        else:
            results = method.solve(function, left, right, epsilon, decimal_places)
    except TypeError:
        print('(!) Ошибка при вычислении значения функции, возможно она не определена на всем интервале.')
        continue

    print('\n')
    for result in results:
        print(str(result))

    if input('\nЕще раз? [y/n] ') != 'y':
        break

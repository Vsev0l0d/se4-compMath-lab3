from typing import Tuple
import decimal
from Function import Function


def choose_function(functions) -> Function:
    print("Выберите уравнение:")
    for num, func in functions.items():
        print(str(num) + ': ' + func.text)
    try:
        equation_number = int(input("Введите номер уравнения: "))
    except ValueError:
        print('(!) Вы ввели не число')
        return choose_function(functions)
    if equation_number < 1 or equation_number > len(functions):
        print("(!) Такого номера нет.")
        return choose_function(functions)
    return functions[equation_number]


def choose_method_number(methods) -> int:
    print("Выберите метод:")
    for num, mtd in methods.items():
        print(str(num) + ': ' + mtd.name)
    try:
        method_number = int(input("Введите номер метода: "))
    except ValueError:
        print('(!) Вы ввели не число')
        return choose_method_number(methods)
    if method_number < 1 or method_number > len(methods):
        print("(!) Такого номера нет.")
        return choose_method_number(methods)
    return method_number


def read_initial_data() -> Tuple[float, float, float, int]:
    while True:
        filename = input("Введите имя файла для загрузки исходных данных и интервала "
                         "или пустую строку, чтобы ввести вручную: ")
        if filename == '':
            try:
                left = float(input('Введите левую границу интервала: '))
                right = float(input('Введите правую границу интервала: '))
                if right < left:
                    print('(!) правая граница не может быть меньше левой')
                    continue
                epsilon = input('Введите погрешность вычисления: ')
                break
            except ValueError:
                print('(!) Вы ввели не число')
        else:
            try:
                f = open(filename, "r")
                left = float(f.readline())
                right = float(f.readline())
                if right < left:
                    print('(!) правая граница не может быть меньше левой')
                    continue
                epsilon = f.readline()
                f.close()
                print('Считано из файла:')
                print(f'Левая граница: {left}, правая: {right}, погрешность: {epsilon}')
                break
            except FileNotFoundError:
                print('(!) Файл для загрузки исходных данных не найден.')

    decimal_places = abs(decimal.Decimal(epsilon).as_tuple().exponent)
    epsilon = float(epsilon)

    return left, right, epsilon, decimal_places

import Model
import View


def input_calculating_string():
    calculating_string = input('Введите выражение:')
    return calculating_string


def split_by_signs(string):
    signs = ['*', '/', '-', '+']
    result = []
    number = ''
    for symbol in string:
        if symbol in signs:
            result.append(int(number))
            number = ''
            result.append(symbol)
        else:
            number = number + symbol
    result.append(int(number))
    return result


def print_result(calculating_string, result):
    """Вывод результата"""
    print(f'{calculating_string} = {result}')

def division_by_zero():
    """Сообщение об ошибке"""
    print('Ошибка: деление на 0')

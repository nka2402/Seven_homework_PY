first = 0
second = 0
result = 0

listOperator = {
    '*': lambda x, y: int(x) * int(y),
    '/': lambda x, y: int(x) / int(y),
    '+': lambda x, y: int(x) + int(y),
    '-': lambda x, y: int(x) - int(y)
}


def set_first(number: int):
    global first
    first = number


def set_second(number: int):
    global second
    second = number


def set_result(oper: str):
    global result
    global second
    if second == 0:
        return
    result = listOperator.get(oper)(first, second)


def get_first():
    global first
    return first


def get_second():
    global second
    return second


def get_result():
    global result
    return result

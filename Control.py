import Model
import View


def get_operator_info(arithmetic_elements):
    mult_index = None
    div_index = None
    add_index = None
    sub_index = None

    oper = None
    
    oper_index = None

    if '*' in arithmetic_elements:
        mult_index = arithmetic_elements.index('*')
    if '/' in arithmetic_elements:
        div_index = arithmetic_elements.index('/')

    if mult_index or div_index:
        if mult_index and div_index:
            oper_index = min(mult_index, div_index)
            oper = arithmetic_elements[oper_index]
        elif mult_index:
            oper_index = mult_index
            oper = '*'
        else:
            oper_index = div_index
            oper = '/'
    else:
        if '+' in arithmetic_elements:
            add_index = arithmetic_elements.index('+')
        if '-' in arithmetic_elements:
            sub_index = arithmetic_elements.index('-')

        if add_index and div_index:
            oper_index = min(add_index, div_index)
            oper = arithmetic_elements[oper_index]
        elif add_index:
            oper_index = add_index
            oper = '+'
        else:
            oper_index = sub_index
            oper = '-'
    return oper, oper_index


def start():
    calculating_string = View.input_calculating_string()
    arithmetic_elements = View.split_by_signs(calculating_string)

    while len(arithmetic_elements) > 1:
        oper, oper_index = get_operator_info(arithmetic_elements)
        Model.set_first(arithmetic_elements[oper_index - 1])
        Model.set_second(arithmetic_elements[oper_index + 1])
        Model.set_result(oper)
        result = Model.get_result()

        if result is None:
            View.division_by_zero()
            return
        arithmetic_elements[oper_index] = result
        arithmetic_elements.pop(oper_index + 1)
        arithmetic_elements.pop(oper_index - 1)

    View.print_result(calculating_string, arithmetic_elements[0])

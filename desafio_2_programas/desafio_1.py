import re


def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False


def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False


def is_number(val):
    return is_int(val) or is_float(val)


"""
if (numero%2) == 0:
"""
num1 = input('Informe um número: ')

if is_number(num1):
    num1 = float(num1)
    if (num1%2) == 0:
        print(f'O número {num1} é um número par.')
    else:
        print(f'O número {num1} é um número Ímpar.')
elif not is_number(num1):
    print(f'O valor digitado {num1} não é um número válido.')
else:
    print(f'O número \"{num1}\" não é um número inteiro.')
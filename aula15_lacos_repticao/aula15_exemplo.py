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

cond = True

while cond:
    print('Para sair, digite [s]im em qualquer momento do programa!')
    valor1 = input('Digite um número: ')
    valor2 = input('Digite outro númer: ')
    operador = input('Digite um operador: ')

    if is_number(valor1) and is_number(valor2):
        valor1 = float(valor1)
        valor2 = float(valor2)
        if operador == '+':
            print('Selecionado soma! \n')
            print(f'A soma de {valor1} + {valor2} é {valor1+valor2}')
        elif operador == '-':
            print('Selecionado Subtração: ')
            print(f'A subtração de {valor1} - {valor2} é de: {valor1-valor2}')
        elif operador == '*':
            print('Selecionado multiplicação: ')
            print(f'A multiplicação de {valor1} * {valor2} é de: {valor1*valor2}')
        elif operador == '/':
            print('Selecionado Divisão: ')
            print(f'A Divisão do valor {valor1} dividido pelo valor {valor2} é de: {valor1/valor2}')
        else:
            print(f'Operador matemático digitado errado, operador digitado "{operador}"')
            cond = True
    else:
        if not is_number(valor1):
            non_numeric = valor1
        elif not is_number(valor2):
            non_numeric = valor2
        print(f'Os valores digitados não são numéricos "{non_numeric}"')

print(f'Encerramento do While, condição está setada como "{cond}"')


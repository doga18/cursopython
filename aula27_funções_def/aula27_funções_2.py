"""
Funções DEF em Python (Parte 2)
"""

def verificar(var):
    return f'Erro ao retornar o valor {var}'


resultad = verificar('')

if resultad:
    print(f'Trouxe resultado {resultad}')
else:
    print(f'Não trouxe resultado {resultad}')


def verificar_idade():
    idade = input('Informe sua idade: ')
    if not idade.isnumeric():
        print(f'Você digitou um valor não número {idade}, tente novamente.')
    else:

        if int(idade) >= 18:
            return 'Autorizado'
        else:
            return 'Não autorizado'

def v_is_number(valor):
    if valor.isnumeric:
        return True

def calculadora():

    ver_nm_1 = False
    ver_nm_2 = False

    while not ver_nm_1:
        nm_1 = input('Insira o primeiro número a ser calculado: ')
        ver_nm_1 = True
        if v_is_number(nm_1):
            valor_verificado_1 = nm_1
            print(valor_verificado_1)
        else:
            print(f'O Valor digitado não é um valor número válido{nm_1}')
            ver_nm_1 = False
        while not ver_nm_2:
            nm_2 = input('Insira o segundo número a ser calculado: ')
            if v_is_number(nm_2):
                ver_nm_2 = True
                valor_verificado_2 = nm_2
            else:
                print(f'O valor digitado não é um valor numérico válido{nm_2}')

    resultado_final = int(valor_verificado_1) * int(valor_verificado_2)

    return resultado_final

resultado = verificar_idade()

if resultado == 'Autorizado':
    exibir = calculadora()
    print(exibir)
else:
    print(f'Você não está autorizado a utilizar a calculadora.')

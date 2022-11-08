"""
Funções DEF em Python (Parte 2)
"""

def divisao(n1, n2):
    if n2 == 0:
        return
    return n1 / n2
divide = divisao(8,2)

if divide:
    print(divide)
else:
    print('Conta inválida')

def dumb():
    return 1.2

print(dumb(), type(dumb()))


def mostrar(var):
    print(var)

def trazer_a_msg():
    #Quando não tem os parenteses, você não irá executar a função, somente trazer ela para a varíavel que desejar, com () você está executando ela.
    return mostrar

qualquer = trazer_a_msg()('E mostrar o valor na outra função de retorno.')

print(type(trazer_a_msg()))
print(id(trazer_a_msg), id(mostrar))

if trazer_a_msg == mostrar:
    print('Trazer a msg é igual a mostrar')
else:
    print('Blaaaaaa')

def dumb_2():
    return ('Luiz', 'Otávio')

var = dumb_2()
print(var, type(var))
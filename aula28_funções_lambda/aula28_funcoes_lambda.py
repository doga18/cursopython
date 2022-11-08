"""
Funções anonimas, expressões lambda
"""
from audioop import reverse


def func(arg, arg2):
    return arg * arg2

var = func(2,2)
print(var)

#anonima
a = lambda x, y: x * y

print(a(2,2))

lista = [
    ['P1', 14],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]
# def funcao(item):
#     return item[1]

# lista.sort(key=funcao, reverse=True)
lista.sort(key=lambda item: item[1], reverse=True)

print(lista)
print(sorted(lista, key=lambda i: i[0]))
# Explicando, o I seria o índice daquela lista, onde o [0] Seria o primeiro campo, neste exemplo o P1, o [1] Seria os valores, exemplo o 14, então seria o item ou indíce a contar
# mais o indice inicial, a KEY serve para mostrar o tipo de funções anônima, que seria no caso a lambda!

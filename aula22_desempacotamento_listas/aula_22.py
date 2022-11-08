"""
Desempacotamento de listas em Python
"""

lista = ['Luiz', 'João', 'Maria', 1, 2, 3]

n1, n2, *outra_lista, ultimo_da_lista = lista

# *_ sem não for usar o resultado dessa litas, significa que ninguem vai usar nem vc.

print(n1, n2)

print(*outra_lista)

print(ultimo_da_lista)
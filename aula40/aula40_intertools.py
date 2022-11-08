"""
count - Intertools
"""
from types import GeneratorType
from itertools import count

variavel = ((x, y)for x, y in zip('Alo', 'Alo'))
print(list(variavel))

contador = count(start=5)

for valor in contador:
    print(valor)

    if valor >= 10:
        break


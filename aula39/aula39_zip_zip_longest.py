"""
Zip - Unindo iteráveis
Zip_longest - Itertool
"""
from itertools import zip_longest, count

# Código
cidades = ['São paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']

# Código
estados = ['SP', 'MG', 'BA']

indice = count()

cidades_estados_1 = zip(cidades, estados)
cidades_estados_2 = zip_longest(cidades, estados, fillvalue='Estado Sem Nome')
# cidades_estados_2 = zip_longest(indice, cidades, estados, fillvalue='Estado Sem Nome')

for valor in cidades_estados_1:
    print(valor[0], valor[1])

for valor in cidades_estados_2:
    print(valor[0], valor[1])


# for valor in cidades_estados_2:
#     # print(valor)
#     print(indice, estados, cidades)
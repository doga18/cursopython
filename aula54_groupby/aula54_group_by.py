# Groupby agrupando valores (itertools)
from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Douglas', 'nota': 'B'},
    {'nome': 'Luana', 'nota': 'C'},
    {'nome': 'Silvia', 'nota': 'D'},
    {'nome': 'Michele', 'nota': 'F'},
    {'nome': 'Sthephanie', 'nota': 'B'},
    {'nome': 'Bianca', 'nota': 'A'},
    {'nome': 'Lais', 'nota': 'C'},
    {'nome': 'Vitória', 'nota': 'A'},
    {'nome': 'Bis', 'nota': 'A'},
]

def ordena(valor):
    return valor['nota']

alunos_agrupados = sorted(alunos, key=ordena)


# for aluno in alunos_agrupados:
#     print(aluno)

grupos = groupby(alunos_agrupados, key=ordena)

for chave, grupo in grupos:
    # print(chave)
    for aluno in grupo:
        print(aluno)

# grupos = groupby(alunos)
#
# for chave, grupo in grupos:
#     print(chave)
#     print(list(grupo))

"""
Para usar o groupby precisamos sempre ordenar os valores, caso não possamos ordenar porque os dados são oriundos de outro lugar, podemos usar o sorted para ordenar a lista antes.

Veja o exemplo abaixo.
"""

# Exemplo de baixo é mais simples para compreensão.

# alunos = ['a', 'a', 'a', 'b', 'c', 'a']
#
# grupos = groupby(alunos)
# grupos_ordenados = groupby(sorted(alunos))
#
# for chave, grupo in grupos:
#     print(chave)
#     print(list(grupo))
# print('Separador')
#
# for chave1, grupo1 in grupos_ordenados:
#     print(chave1)
#     print(list(grupo1))
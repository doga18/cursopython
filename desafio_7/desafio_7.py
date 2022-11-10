# Exercicio - Unir lista_soma
# Crie uma função zupper (como o zipper de roupas)
# O Trabalho dessa função será unir duas litas na ordem
# Use todos os valores da menor lista.
# Ex:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizon', 'MG')]
from itertools import zip_longest

# def zipper(lista1, lista2):
#
#     intervalo_maximo = min(len(lista1), len(lista2))
#     return [
#         (lista1[i], lista2[i]) for i in range(intervalo_maximo)
#     ]

    # tam1 = len(lista1)
    # tam2 = len(lista2)

    # if tam1 > tam2:
    #     return f'A lista 1: {tam1} é maior que a lista 2: {tam2}'
    # elif tam1 < tam2:
    #     return f'A lista 2: {tam2} é maior que a lista 1: {tam1}'
    # else:
    #     return f'Erro {tam1} e {tam2}'


lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']

# print(zipper(lista1, lista2))

print(list(zip(lista1, lista2))) # Isso equivale toda aquela função acima, executando exatamente a mesma coisa, só que usando a lista menor como referência

print(list(zip_longest(lista1, lista2, fillvalue='Sem Cidade Descrita'))) # Isso equivale toda aquela função acima, porém, utiliza a lista maior como referência.

# Functools são ferramentas para funções.
# Reduce

from functools import reduce

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 2', 'preco': 13.25},
    {'nome': 'Produto 3', 'preco': 51.32},
    {'nome': 'Produto 4', 'preco': 217.64},
    {'nome': 'Produto 1', 'preco': 78.42},
]


def funcao_do_reduce(total, produto):
    print('total', total)
    print('produto', produto)
    print()
    return total + produto['preco']


total = reduce(
    funcao_do_reduce,
    produtos,
    0
)

# Sem usar a função acima e usar função anônima lambda

total_simples = reduce(
    lambda ac, p: ac + p['preco'],
    produtos,
    0
)

print(f'Total é: {total}')
print()
print(f'Total Lambda é: {total_simples}')

# print_iter(total)





# total = 0
#
# for p in produtos:
#     total += p['preco']
#
# print(total)
#
# Simplificando o código acima

# print(sum([p['preco'] for p in produtos]))
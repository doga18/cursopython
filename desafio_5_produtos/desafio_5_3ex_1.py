import copy
from audioop import reverse

from aula41_filtro_de_dados_list_comprehension.aula41_filtro_dados_listcomprehension import novos_produtos
from dados import produtos, douglas

#novos_produtos = copy.deepcopy(produtos)

# print(produtos)
# print(novos_produtos)

def mostrar_lista(description, *lista):
    print(f'\n Segue os produtos {description}\n')
    print(*lista, sep='\n')

# Usando a list comprehension, fazemos a ordenação e copia profunda dos dados.

# 1: 1% de acréscimo dos produtos.
# 2: Ordem do nome dos produtos crescente
# 3: Ordem do preço decrescente.

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]

new_produtos_alf = sorted(
    novos_produtos,
    key=lambda p: p['nome'], reverse=False
)

new_produtos_price_desc = sorted(
    novos_produtos,
    key=lambda p: p['preco'], reverse=True
)


mostrar_lista('Originais', *produtos)
mostrar_lista('Novos, ordenados por nome', *new_produtos_alf)
mostrar_lista('Novos, ordenados por preço', *new_produtos_price_desc)
mostrar_lista('Produtos Originais', *produtos)

# print(f'\nProdutos Originais\n', *produtos, sep='\n')


# print(f'\nProdutos Copiados\n', *novos_produtos, sep='\n')
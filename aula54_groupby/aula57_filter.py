# Functools são ferramentas para funções, nesse caso, utiliza o partial para realizar porcentagem
# Filter



def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

# def muda_preco_de_produtos(produto):
#     return {
#         **produto,
#         'preco': size_then_percent(produto['preco'])
#     }

def filtrando_preco(valor):
    return valor['preco'] > 100



produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 2', 'preco': 13.25},
    {'nome': 'Produto 3', 'preco': 51.32},
    {'nome': 'Produto 4', 'preco': 217.64},
    {'nome': 'Produto 1', 'preco': 78.42},
]

# novos_produtos = [
#     p for p in produtos
#     if p['preco'] > 10
# ]


novos_produtos = filter(
    # Então o primeiro parametro sempre será uma função do filter e a segunda o iteravel.
    lambda p: p['preco'] > 10,
    produtos
)

novos_produtos_com_funcao = filter(
    filtrando_preco,
    produtos
)


print_iter(novos_produtos_com_funcao)
# print_iter(novos_produtos)
print_iter(produtos)

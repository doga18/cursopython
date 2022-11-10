# Functools são ferramentas para funções, nesse caso, utiliza o partial para realizar porcentagem
from functools import partial


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 2', 'preco': 13.25},
    {'nome': 'Produto 3', 'preco': 51.32},
    {'nome': 'Produto 4', 'preco': 27.64},
    {'nome': 'Produto 1', 'preco': 78.42},
]

def aumentar_preco(valor, porcentagem):
    # novo_preco = valor ** porcentagem
    return round(valor * porcentagem, 2)

size_then_percent = partial(
    # função acima
    aumentar_preco,
    #valor definido direto na função
    porcentagem=1.1
)

novos_produtos = [
    # Ao colocar esse ** no dicionario, você expande ele, acho que ele quer dizer que vc copia.
    {**p, 'preco': size_then_percent(p['preco'])} for p in produtos
]

def muda_preco_de_produtos(produto):
    return {
        **produto,
        'preco': size_then_percent(produto['preco'])
    }

new_products = map(
    muda_preco_de_produtos,
    produtos
)

print_iter(new_products)
# print(list(new_products))

# print_iter(produtos)
# print_iter(novos_produtos)

print(
    list(
        map(
            lambda x: x * 3,
            [1, 2, 3, 4]
        )
    )
)
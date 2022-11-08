# Dictionary Comprehension e Set Comprehension

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

print(produto.items())

# for chave, valor in produto.items():
#     print(chave, valor)
#     ...

dc = {
    chave: valor.upper()
    if isinstance(valor, str)else valor
    for chave, valor
    in produto.items()
}

# Ao contrário e verificando 1 ou 2 valores, exemplo de 1 valor, está comentado!

dc2 = {
    chave: valor
    # if isinstance(valor, int)else valor.upper()
    if isinstance(valor, (int, float))else valor.upper()
    for chave, valor
    in produto.items()
    # if chave == 'categoria'
    if chave != 'categoria'
}

print(dc2)

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
]

lista = {
    chave: valor
    for chave, valor in lista
}

s1 = {i ** 2 for i in range(10)}
print(s1)
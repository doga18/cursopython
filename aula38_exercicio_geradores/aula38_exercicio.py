carrinho = []

carrinho.append(('Xbox', 30))
carrinho.append(('PS5', 300))

# print(carrinho)

#Somar preços.

total = 0

for produto in carrinho:
    total += produto[1]
# print(total),

lista_dicionario = [
    ('chave', 2),
    ('chave2', 'valores2'),
    ('chave3', 'valores3'),
]

soma = 0

# Explicando, a função, sum, soma os resultados da comprehension, o float, converte o y que será o segundo valor em flotar, e o X toma o primeiro valor da chave,
# e o y toma o segundo de carrinho
d3 = sum([float(y) for x, y in carrinho])
# print(d3)

#Replicando para melhor compreensão.

lista_de_compras = []

lista_de_compras.append(('Tomate', 44.32))
lista_de_compras.append(('Cebola', 12.12))
lista_de_compras.append(('Macarrão', 9.87))

# descri = [(x) for x, y in lista_de_compras]
# valor_descri = [float(y) for x, y in lista_de_compras]
#
# total_de_compras = sum([float(y) for x, y in lista_de_compras])

for x, y in lista_de_compras:
    print(f'Produto {x} com valor de R$: {y}')
    valor_descri = [float(y) for x, y in lista_de_compras]


total_de_compras = sum([float(y) for x, y in lista_de_compras])

print(f'O Total de compras é R$:{total_de_compras}')


h1 = [1,2,3,4,5,6]
#multiplicando os valores de cima por 2
h2 = [a*2 for a in h1]

lista_dicionario = [
    ('chave', 2),
    ('chave2', 'valores2'),
    ('chave3', 'valores3'),
]

d1 = {x: y*2 for x, y in lista_dicionario} # Comprimindo dicionário em
d3 = {x: y*2 for x, y in lista_dicionario} # Comprimindo dicionário em
d2 = dict(lista_dicionario)

print(h2)
# print(lista_dicionario)
# print(d1)
# print(d2)
print(d3)

f1 = {f'chave_{x}': x**2 for x in range(7)}
# print(f1, type(f1))
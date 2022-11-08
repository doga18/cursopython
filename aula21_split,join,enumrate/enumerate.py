lista_de_nomes = [
    ['Edu', 'João', 'Luiz'],
    ['Maria', 'Aline', 'Joana'],
    ['Helena', 'Ed', 'Lu'],
]

enumerada = list(enumerate(lista_de_nomes))
# print(enumerada)


for v1, v2 in enumerate(lista_de_nomes):
    print(v1, v2)
print('########')

for v1, v2 in enumerate(lista_de_nomes, 53):
    print(v1, v2)
print('########')

for v1 in enumerate(lista_de_nomes, 53):
    print(v1)
print('########')

for v1 in enumerate(lista_de_nomes, 53):
    valor_enumerado, minha_lista = v1
    # print(valor_enumerado, minha_lista)
    nome1, nome2, nome3 = minha_lista
    print(nome1, nome2, nome3)
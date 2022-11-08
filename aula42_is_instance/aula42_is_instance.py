# isinstace - para saber se o objeto é de determinado tipo

lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1, 5}, {'nome': 'Luiz'},
]

lista_de_letras = []
print(lista_de_letras)

for item in lista:
    if isinstance(item, set):
        print('SET')
        item.add(5)
        print(item, isinstance(item, set))

    elif isinstance(item, str):
        print('STR')
        print(item, isinstance(item.upper(), set))

    elif isinstance(item, (int, float)):
        print('NUM')
        print(item, item * 2)

    else:
        print('Outro Tipo')
        print(item)


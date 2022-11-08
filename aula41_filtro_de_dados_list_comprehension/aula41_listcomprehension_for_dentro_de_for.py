lista = []
for x in range(3):
    for y in range(3):
        lista.append((x,y))

    print(lista)

lista2 = [
    # Lado esquerdo do for sempre será incluído na lista, no lado direito são os filtros/condições.
    (x, y)
    for x in range(3)
    for y in range(3)
]

print('Separando')
print(lista2)
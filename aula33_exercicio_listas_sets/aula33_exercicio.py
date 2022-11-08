lista_de_listas_de_inteiros = [
    [1,2,3,4,5,6,7,8,9],
    [9,6,3,5,4,2,9,2,1],
    [5,6,3,5,1,2,1,3,5],
    [9,8,7,7,8,9,4,5,4],
    [2,2,3,1,5,4,6,8,8],
    [4,7,9,9,8,8,4,4,2],
]



def encontra_primeiro_duplicado(param_lista_de_inteiros):
    numeros_checados = set()
    primeiro_duplicado = -1

    for numero in param_lista_de_inteiros:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break
        numeros_checados.add(numero)

    # print(numeros_checados)
    return primeiro_duplicado

for lista_de_inteiros in lista_de_listas_de_inteiros:
    print(encontra_primeiro_duplicado(lista_de_inteiros))
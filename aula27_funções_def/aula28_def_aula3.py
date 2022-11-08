"""
Funções def -- *args **kwargs --
"""

def fun(*args):
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))
    args = list(args)
    args[0] = 20
    print(args)

lista = [1,2,3,4,5]
# print(*lista, sep=' ? ')

fun(1,2,3,4,5)

def exemplo2(*args, **kwargs):
    print(args)
    print(kwargs['nome'], kwargs['sobrenome'])

    nome = kwargs.get('nome')
    idade = kwargs.get('idade')
    if idade is not None:
        print(idade)
    else:
        print('Idade não informada.')

    print(nome)

lista2 = [10,20,30,50]
exemplo2(*lista, *lista2, nome='Douglas', sobrenome='pfeiffer', idade='15')
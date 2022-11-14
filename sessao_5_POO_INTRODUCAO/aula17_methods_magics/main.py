"""
https://rszalski.github.io/magicmethods/
"""


class LetraA:
    def __new__(cls, *args, **kwargs):

        if not hasattr(cls, '_jaexiste'):
            cls._jaexiste = object.__new__(cls)
        return cls._jaexiste

        print(f'Eu sou o new')
        return object.__new__(cls)

    def __init__(self):
        print('INIT EU SOU')


a = LetraA()
b = LetraA()
c = LetraA()

print(a == b)

print(id(a), id(b), id(c))


class LetraB:
    def __init__(self):
        print('INIT EU SOU Letra B')

    # O método call, faz a classe funcionar como se fosse uma função.
    # Só que, só vai ser chamado, quando eu chamar a classe do mesmo jeito que se chama uma função.
    # Exemplo abaixo.
    def __call__(self, *args, **kwargs):
        resultado = 1

        for i in args:
            resultado *= i

        return resultado

        # print(args)
        # print(kwargs)
    def __setattr__(self, key, value):
        self.__dict__[key] = value
        print(key, value)


l1 = LetraB()
variavel = l1(1,2,6,5,9)
print(variavel)

l2 = LetraB()
l2.nome = 'Douglas'
print(l2.nome)
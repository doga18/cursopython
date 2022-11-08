"""
Geradores, Iteradores e Iteráveis.
"""
import sys
import time


def gera():
    r = []
    for n in range(100):
        yield n
        # r.append(n)
        time.sleep(0.1)
    return r


def montar():
    variavel = 'Valor 1'
    yield variavel
    variavel = 'Valor 2'
    yield variavel
    variavel = 'Valor 3'
    yield variavel


t = montar()
print(next(t))
print(next(t))
print(next(t))


g=gera()

# for v in g:
#     print(v)

#Utilizando a função next do python, é equivalente ao usar o for, segue exemplo abaixo, para cada Valor, e não todos.
print(next(g))
print(next(g))
print(next(g))
print(next(g))

print(hasattr(g, '__next__'))


lista = list(range(10))

print(lista)
print(sys.getsizeof(lista))

exemplo1 = [0, 1, 2, 3, 4, 5]
exemplo1 = iter(exemplo1)

print(next(exemplo1))
print(next(exemplo1))
print(next(exemplo1))
print(next(exemplo1))
print(next(exemplo1))
print(next(exemplo1))

print(hasattr(exemplo1, '__next__'))
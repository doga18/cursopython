# módulo

import sys

# Generator expression, Iterables e Iterators em Python

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)

# Generator são funções que sabem pausar. Generator é um interator, mas um interator não é um Generator

generator = (n for n in range(10000000))
lista = [n for n in range(1000000)]

# print(generator)
print(sys.getsizeof(generator))
print(sys.getsizeof(lista))

print(next(generator))

# for n in generator:
#     print(n)
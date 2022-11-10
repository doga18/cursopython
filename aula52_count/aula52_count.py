# count contador infinito
from itertools import count

c1 = count(10, 8) # inicio em 10, determinado no primeiro valor, próximo valor, seria o espaçamento entre valores, por exemplo, multiplos de 8.
# c1 = count(start=10, step=2) # inicio em 10, determinado no primeiro valor, próximo valor, seria o espaçamento entre valores, por exemplo, multiplos de 8.

r1 = range(10, 100, 8) # inicio em 10, fim em 100

print(next(c1))
print(next(c1))

print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print('r1', hasattr(c1, '__iter__'))
print('r1', hasattr(c1, '__next__'))


for i in c1:
    if i >= 100:
        break
    print(i)

print('Fim do count')
print('inicio do range')

for i in r1:
    print(i)
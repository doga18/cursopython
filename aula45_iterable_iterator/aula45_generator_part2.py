# Introdução às Generator functions em python
# Generator = (n for n in range(10000000))

limite = 10

def gerador(n=0, maximum=10):
    while True:
        yield n
        n += 5

        if n > maximum:
            return

    # yield 1 # Pausar
    # print('Continuando...')
    # yield 2
    # print('Continuando...')
    # yield 3
    # print('Continuando...')
    # yield 4
    # print('Continuando...')
    # yield 5
    # print('Continuando...')
    #
    #
    # return 'Acabou os numeros'


gen = gerador(n=0, maximum=15);

for n in gen:
    print(n)

# Yield From

def gen1():
    yield 1
    yield 2
    yield 3

def gen2():
    yield from gen1()
    yield 4
    yield 5
    yield 6

g = gen2()

for numero in g:
    print(numero)
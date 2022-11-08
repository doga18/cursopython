# raise - lançando exceções (erros)
# https://docs.python.org/3/library/exceptions.html

print(123)
# raise ValueError('Deu erro')
print(456)

def divide2(n, d):
    try:
        return n / d
    except ZeroDivisionError:
        raise

# print(divide2(8,0))

def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError(f'Você está tentando dividir {d} por 0')
    return True

def verify_if_number(a):
    tipo_a = type(a)
    if not isinstance(a, (float, int)):
        raise TypeError(f'{a} não é uma variável do tipo número.'
                        f' Tipo {tipo_a.__name__} enviado.')
    return True

def divide(n,d):

    verify_if_number(n)
    verify_if_number(d)

    nao_aceito_zero(d)
    return n / d

print(divide(8,'1'))
# Try, except, else, finally

# a = 18
# b = 0
# c = a / b


try:
    a = 18
    b = 0
    c = a / b
    print('Linha 1')
    print(c)
    print('Linha 2')
    ...
except ZeroDivisionError:
    # ZeroDivisionError
    print('Erro')
    ...
except (NameError, IndexError):
    # ZeroDivisionError
    print('Variável não definida')

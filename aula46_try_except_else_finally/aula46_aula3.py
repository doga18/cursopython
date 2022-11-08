# Try, except, else, finally

# a = 18
# b = 0
# c = a / b


try:
    # a = 18
    #b = 0 # Erro proposital
    # c = a / b
    print('Abriu o arquivo')
    8/0
    ...
except ZeroDivisionError as r:
    print('Dividiu por zero', r)
    ...
else:
    print('Não deu erro')
finally:
    print('Fechou o arquivo')

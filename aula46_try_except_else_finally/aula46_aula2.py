# Try, except, else, finally

# a = 18
# b = 0
# c = a / b


try:
    a = 18
    #b = 0 # Erro proposital
    c = a / b
    print('Linha 1')
    print(c)
    print('Linha 2')
    ...
except ZeroDivisionError:
    # ZeroDivisionError
    print('Erro')
    ...
except (NameError, IndexError) as error:
    # ZeroDivisionError
    print('Variável não definida')
    print(f'Mensagem de Erro: {error}') #Cara isso é muito bom para construir funções e tratar os erros.
    print(f'Nome: ', error.__class__.__name__)

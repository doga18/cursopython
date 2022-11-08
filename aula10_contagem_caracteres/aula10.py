usuario = input('Digite seu usário: ')
qtd_caracteres = len(usuario)

print(usuario, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres < 3:
    print(f'O usuario é muito curto! Menos de {qtd_caracteres} caracteres!')
elif qtd_caracteres >= 5:
    print(f'O usuario {usuario} foi cadastrado no sistema!')


string_1 = input('Digite uma frase: ')
string_2 = input('Digite outra frasee: ')

print(f'A quantidade total de caracteres, foi de {len(string_1) + len(string_2)}')


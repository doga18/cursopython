nome = input('Informe seu nome: ')

qtd_letras = len(nome)

if qtd_letras <= 4:
    print(f'Seu nome é curto, possui {qtd_letras} letras.')
elif (qtd_letras >= 5) and (qtd_letras <= 6):
    print(f'Seu nome é normal, possui {qtd_letras} letras.')
else:
    print(f'Seu nome é muito grande, contém {qtd_letras} de letras.')
txt = ['douglas', 'João', 'maria']

comeca_com_j = False

# print('Variável comeca_com_j está com o valor inicial de', comeca_com_j)
#
# for valor in txt:
#     if valor.startswith('J'):
#         print('Começa com J', valor)
#         comeca_com_j = True
#         print('Variável começa_com_j recebeu o valor', comeca_com_j)
#     else:
#         print('Esse valor não começa com a letra J', valor)

#agora seria um laço procurando um termo para sair do laço.

pesquisa = ['Luana', 'Guilherme', 'luiz', 'ASDouglas', 'João', 'maria']



validar = True

while validar == True:
    a_pesquisar = input('Insira uma letra para pesquisa palavras que comecem ao ela: ')
    for valor_x in pesquisa:
        if valor_x.lower().startswith(a_pesquisar):
            print(f'Foi localizado a palavra na lista pesquisa : {pesquisa}, segue a mesma: {valor_x}')
            validar = False
            break
    else:
        print(f'Não existe, uma palavra que comece com a letra "{a_pesquisar}" na lista "{pesquisa}"')


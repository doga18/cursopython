"""
Condições, IF, ELIF, ELSE
"""

if False:
    print('Verdadeiro')
elif False:
    print('Agora é Verdadeiro')
elif False:
    print('Mais um Verdadeiro')
else:
    print('Não é Verdadeiro')


if False:
    print('Verdadeiro')
elif True:
    print('Agora é Verdadeiro')
    nome = input('Insira seu nome: ')
    info_idade = input('Insira sua idade: ')

    # print(info_idade.isnumeric()) isnumeric só verifica se há somente numeros e se são positivos.

    if not (info_idade.isnumeric()):
        print('Idade não informada!')
    elif info_idade.isnumeric():
        idade = int(info_idade)
        if idade <= 10:
            print(f'Você não tem idade suficiente para acessar o sistema, idade informada {idade} anos.')
        elif (idade > 10) & (idade <= 13):
            print(f'Você tem a idade mínima, porém ainda é muito novo, {idade} anos')
        elif idade > 16:
            print(f'Com a idade de {idade} o usuário de nome {nome} tem todo o direito de acessar o sistema!')
        else:
            print('Idade não informada!')

elif False:
    print('Mais um Verdadeiro')
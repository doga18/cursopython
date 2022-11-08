# Montando um sistema de perguntas e respostas com dicionários.

perguntas = {
    'Pergunta 1' : {
        'pergunta' : 'Quanto é 2+2?',
        'respostas' : {
            'a' : '1',
            'b' : '4',
            'c' : '5',
        },
        'resposta_certa' : 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 2+1?',
        'respostas': {
            'a': '1',
            'b': '3',
            'c': '5',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 2+3?',
        'respostas': {
            'a': '1',
            'b': '3',
            'c': '5',
        },
        'resposta_certa': 'c',
    },
}
print()

resposta_certa = 0

for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}] = {rv}')

    resposta_usuario1 = input('Sua Resposta: ')
    if resposta_usuario1 == pv['resposta_certa']:
        print(f'Sua resposta foi a Correta, {resposta_usuario1}')
        resposta_certa += 1
    else:
        print(f'Sua resposta foi a [{resposta_usuario1}], e está errada.')
    print()

qtd_perguntas = len(perguntas) # Len seria para contar os valores, items no caso.
# resposta_certa = 2
porcentagem_acerto = resposta_certa / qtd_perguntas * 100
# print(porcentagem_acerto)
print(f'Você acertou {porcentagem_acerto:.0f}% das perguntas deste questionário.')
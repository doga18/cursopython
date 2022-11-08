'''
For / else em Python
'''

variavel = ['Luiz Otávio', 'Joãozinho', 'Maria']
#cada valor como resultado.
for valor in variavel:
    print(valor)
    #continue, ele termina o primeiro laço antes de ir para o segundo. sem ir para o próximo laço
    continue
    for valor1 in variavel:
        print(valor1)



txt = ['Asuiz Otávio', 'Joãozinho', 'Maria']

for valor_1 in txt:
    if valor_1.startswith('A'):
        print('Começa com A', valor_1)
    else:
        print('não começa A', valor_1)


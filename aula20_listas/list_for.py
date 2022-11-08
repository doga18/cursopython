
l2 = list(range(0, 100, 8))
print(l2)

soma = 0
for valor in l2:
    soma += valor
    print(soma)

l3 = ['$string', True, 10, -20.4]

for elem in l3:
    print(f'O tipo é de {elem} é {type(elem)}')

secreto = 'perfume'
digitadas = []

while True:
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        if digitadas[0] != secreto[0]:
            print('Digite apenas uma letra')
        else:
            print(f'Digite apenas uma letra, até agora temos as letras "{digitadas}"')
        continue
    digitadas.append(letra)
    if letra in secreto:
        print(f'AEEEE, a letra"{letra}" existe na palavra secreta, até agora temos: "{digitadas}"')
    else:
        print(f'Tente mais um pouco a letra "{letra}" digitada não existe na palavra secreta.')
        digitadas.pop()



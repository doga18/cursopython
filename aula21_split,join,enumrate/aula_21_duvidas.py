# secreto_temporario = ''
# for letra_secreto in secreto:
#     if letra_secreto in digitadas:
#         secreto_temporario += letra_secreto
#     else:
#         secreto_temporario += '*';

secreto = 'python'
secreto_temporario = ''

digitadas = ['t', 'o', 'p']



# for letra_secreta in secreto:
#     if letra_secreta == 't':
#         pass
#     else:
#         print(letra_secreta)

for letra_secreta in secreto:
    print(f'Iteração para a letra {letra_secreta}')
    if letra_secreta in digitadas:
        print(f'Eba, a letra que eu queria. {letra_secreta}')
        secreto_temporario += letra_secreta
    else:
        print(f'Essa letra eu não queria! {letra_secreta}')
        secreto_temporario += '*'

print(secreto_temporario)

if secreto == secreto_temporario:
    print(f'Você Ganhou')
else:
    print(f'Você não ganhou')
# for letra_secreta in secreto:   #if contrário se não a letra_secreto igual a T
#     if not letra_secreta == 't':   OU  if letra_secreta != 't':
#         print(letra_secreta)
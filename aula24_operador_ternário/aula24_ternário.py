"""
Operador ternário em Python
"""

logged_user = False

if logged_user:
    msg = 'Usuário Logado'
else:
    msg = 'Usuário precisa logar'

print(msg)

msg = 'Usuário logado.' if logged_user else 'Usuário precisa logar.' # ternário

idade = input('Qual a sua idade? ')

if not idade.isnumeric():
    print('Você precisa digitar somente números')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg_1 = 'Pode acess' if e_de_maior else 'Não pode acesssar.'

if idade >= 18:
    print('Pode acess')
else:
    print('não pode acess')

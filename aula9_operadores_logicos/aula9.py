"""
Operadores lógicos, podendo usar, and or, not and not or...
e, ou. não e, não ou.
in e not in

exemplo de string.

"""


a = 2
b = 2

c = 3

if (a == b) & (b < c):
    print('Verdadeiro')

if not a == b and b < c:
    print('Verdadeiro')
else:
    print('False')


usuario = input('Nome do usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'luiz'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado')
else:
    print('usuário ou senha incorretos')
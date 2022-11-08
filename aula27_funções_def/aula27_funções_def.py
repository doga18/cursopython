"""
Funções DEF em Python (Parte 1)
"""
def funcao():
    print('Hello World')
funcao()

def exibir(msg='nada', nome='usuário'):
    if msg == 'nada':
        return f'Mensagem Vazia'
    else:
        nome = nome.title()
        nome = nome.replace('o', '0')
        nome = nome.replace('a', '4')
        return f'{msg, nome}'






exibir('Eu sou o')
exibir(nome='douglas', msg='Olá')
variavel = exibir()

print(variavel)


"""
Desafios de Python, Segundo!
"""
def titulo_nome(nome):
    nome = nome.capitalize()
    return nome

def saudacao_nome(saudacao, nome):
    nome_titulo = titulo_nome(nome)
    msg = f'Olá {saudacao}, seja bem vindo {nome_titulo}'
    return msg

var = saudacao_nome('Boa noite', 'douglas')

print(type(var), (saudacao_nome('bom dia', 'juana')))

def ola_mundo():
    return 'Olá mundo!'

def mestre(funcao):
    return funcao()

executando = mestre(ola_mundo)

print(executando)

def master(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fala_oi(nome):
    return f'Oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

executar = master(fala_oi, 'Douglas')
executar2 = master(saudacao, 'douglas', saudacao='Boa noite!')
print(executar2)




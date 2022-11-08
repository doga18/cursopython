"""
Def Escopos.
"""

variavel = 'valor'

def func():
    print(variavel)

def func2():
    #Alterar varivaeis de escopo global de dentro da função, NÃO É UMA BOA PRÁTICA!
    global variavel
    variavel = 'Outro Valor'
    print(variavel)

def func3(arg=None):
    arg = arg.replace('v', 'c')
    return arg

def func4():
    print(variavel) # Esse erro é proposital!
    variavel = 1234
    print(variavel)

func4()


outra_variavel = func3(arg=variavel)

print(outra_variavel)
func()
func2()
print(variavel)
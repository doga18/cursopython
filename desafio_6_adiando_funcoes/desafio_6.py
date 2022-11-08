# Exercise - Adiando execuções de funções.

def soma(a, b):
    return a + b


def multiplicar(a, b):
    return a * b


def criar_function(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna


soma_com_cinco = criar_function(soma, 5)
multiplca_por_dez = criar_function(multiplicar, 10)

print(soma_com_cinco(2))
print(multiplca_por_dez(5))





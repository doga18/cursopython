"""
Formatando valor com modificadores - Aula 5

:s - Texto (strings)
:d - Inteiro (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(Caractere)(> ou ^)(Quantidade)(Tipo - s, d ou f)

> - Esquerda - Left
< - Direita - Right
^ - Centro - Center

"""
#Para números!
num_1 = 10
num_2 = 3

divisao = num_1 /num_2

print('{:.2f}'.format(divisao)) #Duas casas decimais após o valor, sendo . porque após o ponto, 2 seriam duas casas decimais e o F seria de float.
print(f'{divisao:.2f}')

nome = 'douglas israel pfeiffer serafim'

#Aqui serve para colocar a quantidade de casas do número selecionado ao resultado, exemplo, ali temos o valor 1, como o > diz 10 casas, serão adicionados
# 9 casas decimais com o valor 0, se fosse 9>10 seria o valor 9.
valor_1 = 1566
print(f'{valor_1:0>10}')

#mesma regra de cima, à direita
valor_2 = 1150
print(f'{valor_2:0<10}')

#mesma regra de cima, com o valor principal no centro.
print(f'{valor_2:0^10}')

#combinando regras.
print(f'{valor_2:0>10.2f}')

#Colocando caracteres antes da String
nome_formatado = '{:@>50}'.format(nome)
print(nome_formatado)

strinjjj = "DouglAs israel"
print(strinjjj.lower()) # tudo minusculo
print(strinjjj.upper()) # tudo maiusculo
print(strinjjj.title()) # primeira letras maiusculo
print(strinjjj.capitalize()) #Capítulos, transformando a primeira palavra com a primeira letra com maiusculo
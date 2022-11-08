"""
add (adiciona), update(atualiza), clear, discard.
union | (une)
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas no set da esquerda)
symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos.)
"""
# SET É MTO PARECIDO, A DIFERENÇA É QUE NÃO TEM CHAVE E VALOR, SÓ VALOR.
Fexemplo = {1,2,3,4,5,6}
e1 = set() #Vazio
e1.add(1)
e1.add(2)
e1.add('Luiz')
print(e1)
e1.discard(2)
print(e1)

f1 = set() # ITERANDO NÃO É INTERANDO.
f1.update('Python')
print(f1)

r1 = [1,2,1,1,3,5,4,6,6,6,6,8,9,6,5,1,'Luiz', 'Luiz'] #Fazer um cast dela, dela mesmo para tirar os valores repetidos.
r1 = set(r1) # Retirando os duplicados, FAZENDO UM CASTING.
r1 = set[r1] # voltando a ser uma lista.
print(r1)

v1 = {1,2,3,4,5,7}
v2 = {1,2,3,4,5,6}
v3 = v1 | v2 # UNION | (une)
v4 = v1 & v2 # intersection & (todos os elementos presentes nos dois sets)
v5 = v1 - v2 # difference - (elementos apenas no set da esquerda)
v6 = v1 ^ v2 # symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos.)

print(v3)
print(v4)
print(len(v4))
print(v5)
print(v6)
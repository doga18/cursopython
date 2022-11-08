l1 = [1,2,3,4,5,6,7,8,9]
l2 = [variavel for variavel in l1]

ex2 = [v * 2 for v in l1]
ex3 = [(v, v2) for v in l1 for v2 in range(3)]

l3 = ['Luiz', 'Mauro', 'Maria']
ex4 = [v.replace('a', '@').upper() for v in l3]

tupla = (
    ('chave', 'valor'), #ISSO É UMA TUPLA JUSTAMENTE PORQUE COMEÇA COM ()
    ('chave2', 'valor2'),
)

ex5 =[(x,y) for x,y in tupla]
ex6 =[(y,x) for x,y in tupla] #Invertendo valor por Chave, alterando o x e y
ex7 = dict(ex6) #Transformando em dicionário.

#filtrar uma listado
l4 = list(range(100))

ex8 = [v for v in l4 if v % 2 == 0 if v % 3 == 0 if v % 4 == 0] # Essa consulta eu consigo ver todos os números que são divisiveis por 2 e por 3 e por 4, por isso deu poucos.
ex9 = [v if v % 3 == 0 else 'Não é' for v in l4] #Para usar o Else, tem que colocar a condição de if antes do caso, no caso acima, sempre será E, ex IF tal coisa e IF tal coisa.

ex9 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in l4] #Com outras condições.

print(l2)
print(ex2)
print(ex3)
print(ex4)
print(ex5)
print(ex6)
print(ex7['valor2'])
print(ex8)
print(ex9)
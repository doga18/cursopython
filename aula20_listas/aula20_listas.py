'''
Listas em Python, tipo Arrays, Fatiamento, append, insert, pop, del, clear, extend, +, min, max, range
'''
#variavel tem 1 valor, exemplo tem
teee = 'algumacoisa'
#lista tem mais valores, de qualuqer tipo
lista = [1, 2, 3, 4, 'douglas', True, 10.2]

list = ['A', 'B', 'C', 'D', 'E', 10.5]
print(list[1])

print(list[5])

list[5] = 'Qualquer outra coisa'

print(list[5])

#exeibição em sequência
print(list[0:2])
print(list[:4])
#para achar o último índice da lista, basta colocar para achar o índice negativo.
print(list[-1:])
#invertendo a exibição
print(list[::-1])

l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1+l2
l4 = l3

l1.extend(l2)
#extender valores!
l1.extend('a')
# no final da lista
l2.append('b')
#Adicionando o índice 0, valor Banana!
l3.insert(0, 'banana')
print(l1)
print(l3)
print(l2)
#retirou o ultimo valor no pop
l3.pop()
print(l3)
#Retirando via fatiamento.
lll = [1,2,3,4,5,6,7,8,9]
del(lll[3:5])
print(lll)


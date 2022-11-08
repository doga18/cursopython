"""
Split, Join Enumrate em Python 2
* Split - Dividir uma strings
* Join - Juntar uma lista # str
* Enumrate - Enumerar elementos da lista # list
"""

string = "O BRASIL É BRASIL E É BRASIL"
lista1 = "1,2,3,4,5,6,7,8,9"

result_list = string.split(' ')
result_list1 = string.split(',')
result_list2 = lista1.split(',')

print(result_list)
print(result_list1)
#por índices
print(result_list2[2])

# for valor in string:
#     print(f'A palavra {valor} apareceu {string.count(valor)}x vezes na Frase')

palavra = ''
count = 0

# for valor in result_list1:
#     xvezes = result_list1.count(valor)
#     if xvezes > count:
#         count = xvezes
#         palavra = valor
# print(f'Palavra {palavra} apareceu {count} Vezes')

for valor in result_list1:
    print(valor.strip().upper())

string4 = ['O', 'Brasil', 'é', 'penta', 'campeão', ]
string3 = "O brasil é penta campeão"
list3 = string3.split(' ')
string_result = ','.join(list3)

print(string4)
print(list3)
print(string_result)


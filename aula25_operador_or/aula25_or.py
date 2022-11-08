"""
CONDIONAL OR
"""

nome = input('Qual seu nome')

print(nome or None or False or 'Você não digitou nada!') #sempre vai cair na primeira verdadeira.

a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Luiz'

var = a or b or c or d or e or f or g

print(var)
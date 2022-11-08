"""
For in em python, Iterando strings com for, Função range(start=0, stop, step=1
"""

txt = 'Python'

c = 0
while c < len(txt): #Fazendo a listagem por letras e índices
    print(txt[c])
    c += 1

for n, letra in enumerate(txt): #Fazendo a listagem por letras e índices, via For.
    print(n, letra)
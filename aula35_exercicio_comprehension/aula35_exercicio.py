string2 = ['01234567890123456789012345678901234567890123456789']
lista = [variavel for variavel in string2]
format = [v.replace('9', '9.') for v in lista]
retorno = list(format)

print(retorno)

# Minha solução acima.

string = '01234567890123456789012345678901234567890123456789'
n = 10
contador = [i for i in range(0, len(string), n)] #Fazendo a contagem
tuplas = [(i, i + n) for i in range(0, len(string), n)]
lista2 = [string[i:i + n] for i in range(0, len(string), n)]
raw = [f'String[{i}:{i+n}]' for i in range(0, len(string), n)]
comp = [i for i in range(0, len(string), n)] # Separando pelo Range da string total, com intervalo de 10.
retorno2 = '.'.join(lista2)



print(tuplas)
print(contador)
print(retorno2)
print(comp)
print(raw)
"""
Manipulando Strings

String indices:
Fatiamento de strings [inicio:fim:passo]
Funções built-in, len, abs, type, print, etc...

Essas funções, podem ser usadas diretamente em cada Tipo.

https://docs.python.org/3/library/stdtypes.html
https://docs.python.org/3/library/functions.html

"""
#positivos  [012345678]
texto = 'Python s2'
#negativos -[987654321]

print(texto[8])
print(texto[-8])

nova_string = texto[2:6] #selecionando os caracteres para ser pego, FATIANDO STRINGS, FIM NÃO É INCLUÍDO.
print(nova_string)

string2 = texto[:4] #pegue do início até o 4
print(string2)

string3 = texto[2:] #pegue do 2 até o fim
print(string3)

#funciona para negativos tbm, exemplo links, excluindo a barra.
url = 'www.google.com.br/'
url_fatiado = url[:-1]

print(url,'\n',url_fatiado)

#Strings tem índices, podem ser tratados, função len pode contar.

for letra in texto:
    print(letra)
d1 = {'chave1':'valor da chave'}
d1['nova_chave']    =   'Valor da nova chave'

print(d1['nova_chave'])

d2 = { 1:   'Valor', 2:   'valor', 3:   'valor da real da chave'}

print([d2])
print(d2[3])

#Dentro da chave D3 tem esses valores, portanto o IF abaixo não funcionaria.
d3 = {
    'str':   'Valor',
    123:    'Outro Valor',
    (1,2,3,4):   'Tupla',
}

print(d3[(1,2,3,4)])

if d3.get('naoexiste') is not None:
    print(d3.get('naoexiste'))

#Agora adicionamos a chave, com o nome, 'naoexiste' mas poderia ser um valor por exemplo = 1, então como existe agora a chave naoexiste irá cair no IF e será exibido o valor dela.

d3['naoexiste'] = 'Agora ela existe'

#se eu quiser atualizar, eu faço da seguinte forma.

d3['str'] = 'Agora o STR tem outro valor'

if d3.get('naoexiste') is not None:
    print(d3.get('naoexiste'))
if d3.get('str') != 'Valor':
    print(d3.get('str'))

#utilizando a função update para atualizar um dicionario, ela atualiza, mantendo os registros anteriores, SE não substituídos.
d4 = {
    1 : 'douglas',
    2 : 'mateus',
    3 : 'jessica',
}
print(d4)
d4.update({
    1 : 'luana',

})
print(d4)

#apagar chave do dicionario
del d4[3] # Deletando a chave 3 Valor == Jessica.

print(1 in d4) #Chegando se ele entende que a chave um (1) existe, se sim, ela trará o resultado como True.
print('luana' in d4.values()) # Isso server para verificar se o valor da chave um (1) bate com a checagem que quero verificar, se sim, trará como True.
print(len(d4)) # Verificar quantos pares existe no dicionario

for k in d4.items(): # Com Items temos como ver o Par de Valores do dicionario, assim, vendo todo o processo, podemos também utilizar o .keys para chaves ou .values para valores.
    print(k)
    print(k[0], k[1]) # Ver chave e valor!

for key, valor in d4.items():
    print(key, valor)

#criando outro exemplo.
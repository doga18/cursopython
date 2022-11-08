clientes = {
    'cliente1' : {
       'nome' : 'Luiz',
       'sobrenome' : 'Otávio'
    },
    'cliente2' : {
       'nome' : 'Douglas',
       'sobrenome' : 'Serafim'
    },
    'cliente3' : {
           'nome' : 'Jessica',
           'sobrenome' : 'Silva'
        },
    'cliente4' : {
       'nome' : 'Lais',
       'sobrenome' : 'Fernanda'
    },
}
# Iteração de dicionarios com filhos em dicionarios.
for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')

import copy

d1 = {1: 'a', 2: 'b', 3: 'c', 'd' : ['Luiz', 'Otávio']}
v = copy.deepcopy(d1)
v = d1.copy() # Cópia Rasa, porém não pode fazer com Tupla, alterando o d acima para () ai invés de []



v[1] = 'Luiz'
v['d'][0] = 'Joãozinho'

print(d1)
print(v)
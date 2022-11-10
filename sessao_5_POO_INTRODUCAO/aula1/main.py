# Onde o From é a origem e o import, diz qual objeto, ou seja a Pessoa.

from pessoa import Pessoa

p1 = Pessoa()
# p2 = Pessoa('joaopaulo', 21)

p1.comer('maça')
p1.comer('banana')
p1.parar_comer()
p1.parar_comer()
p1.falar_assunto(assunto='Política')
p1.comer('Churrasco')
p1.falar_assunto(assunto='Futebol')
p1.parar_falar()
p1.parar_falar()

p2 = Pessoa('João', 32)


print(Pessoa.ano_atual)

print(p2.get_ano_nascimento())


# p1.falar()
# p2.falar()
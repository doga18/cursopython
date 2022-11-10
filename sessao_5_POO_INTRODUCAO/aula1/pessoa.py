# Classe sempre começa com letra maiusculo

from datetime import datetime


class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome='Douglas', idade=20, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

        variavel = 'Valor'
        print(variavel)
        # print(globals(ano_atual))

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo e não pode comer a porção de {alimento}.')
        print(f'{self.nome} está comendo uma portção de {alimento}.')
        self.comendo = True

        if self.falando:
            print(f'{self.nome} ')

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return

        print(f'{self.nome} parou de comer.')
        self.comendo = False

    def falar_assunto(self, assunto):
        if self.comendo:
            print(f'A pessoal {self.nome} está comendo e não pode falar comendo.')

        if self.falando:
            print(f'A pessoa de nome, {self.nome} já está falando sobre o assunto {assunto}.')
            self.falando = True

        print(f'A pessoal {self.nome} vai começar a falar sobre o assunto {assunto}.')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'A pessoa {self.nome} não está falando nada.')
            return

        print(f'A pessoa {self.nome} vai parar de falar.')
        self.falando = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade

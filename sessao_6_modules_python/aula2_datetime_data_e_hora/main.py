# https://docs.python.org/3.0/library/datetime.html

from datetime import datetime, timedelta

data = datetime(2022, 10, 7, 2, 32, 12)

# Modo que salvamos em banco.
print(data)

# Modo de exibição
print(data.strftime("%d-%m-%y %H:%M:%S"))

#######

# Usando a função para receber uma String e transfomar ela em dados para usar.
data2 = datetime.strptime('20/02/2024', '%d/%m/%Y')

print(data2)
print(data2.strftime("%d-%m-%y %H:%M:%S"))
print(data2.timestamp())

# Geralmente utilizam
tempo_de_segundos_ate_hoje = 1708398000.0
data3 = datetime.fromtimestamp(tempo_de_segundos_ate_hoje)
print(data3)

# Pegando a data atual.
dia_atual = datetime.now()
print(dia_atual)

# Somando datas.
date4 = datetime.strptime('20/04/1987 20:55:54', '%d/%m/%Y %H:%M:%S')
print(date4.strftime('%d/%m/%Y %H:%M:%S'))
date4 = date4 + timedelta(days=25)
print(date4.strftime('%d/%m/%Y %H:%M:%S'))
date4 = date4 + timedelta(minutes=25)
print(date4.strftime('%d/%m/%Y %H:%M:%S'))

# Verificando diferenças em Datas, Função dif, diferenças.
d1 = datetime.strptime('20/04/1987 20:59:54', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('05/05/1987 14:37:17', '%d/%m/%Y %H:%M:%S')

dif = d1 - d2
print(dif)
print(dif.seconds)
print(dif.days)

# Ver só a hora.
print(d1.time())

# Comparação de Data.
print(d2 > d1)
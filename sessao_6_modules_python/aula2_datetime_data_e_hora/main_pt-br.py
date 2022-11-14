# https://docs.python.org/3.0/library/datetime.html

from datetime import datetime, timedelta
from locale import setlocale, LC_ALL
# Para pegar o último dia do mês
from calendar import mdays

# Aqui você seta o Local de onde o Programa rodará.
# setlocale(LC_ALL, '')

# Dessa forma você seta exatamente onde o Programa rodará.
setlocale(LC_ALL, 'pt_BR.utf-8')

# segunda-feira, 14 de novembro de 2022.

dt = datetime.now()

format = dt.strftime('%A, %d de %B de %Y.')
print(format)

# Pegando o último dia do mês

mes_atual = int(dt.strftime('%m'))
print(f'Mês: {mes_atual}, Último dia do Mês: {mdays[mes_atual]}.')

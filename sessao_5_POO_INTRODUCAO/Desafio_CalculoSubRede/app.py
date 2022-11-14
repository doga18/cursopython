from classes.calvipv4 import *

calc_ipv4 = CalcIpv4(ip='10.206.252.154', prefixo=26, mascara='255.255.255.0')

print('############## SEGUE INFORMAÇÕES DO IP INFORMADO ##############################')
print()
print(f'IP: {calc_ipv4.ip}')
print(f'Máscara: {calc_ipv4.mascara}')
print(f'Rede: {calc_ipv4.rede}')
print(f'Broadcast: {calc_ipv4.broadcast}')
print(f'Prefixo: {calc_ipv4.prefixo}')
print(f'Números de hosts disponíveis.: {calc_ipv4.get_numero_ips}')
print()
print('###############################################################################')

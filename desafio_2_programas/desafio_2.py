import re


def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False


def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False


def is_number(val):
    return is_int(val) or is_float(val)


"""
if (numero%2) == 0:
"""

hora_informada = input('Por favor informe somente a hora: ')

if is_number(hora_informada):
    hora_informada = int(hora_informada)

    if (hora_informada >= 0) and (hora_informada <= 11):
        print(f"Bom dia, estamos na {hora_informada} hr's do dia.")
    elif (hora_informada >= 12) and (hora_informada <= 17):
        print(f"Boa tarde, estamos na {hora_informada} hr's do dia.")
    else:
        print(f"Boa noite, estamos na {hora_informada} hr's da noite.")
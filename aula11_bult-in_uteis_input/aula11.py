num1 = input('Digite um numero: ')
num2 = input('Digite outro numero: ')

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1+num2)
else:
    print(f'Não pude transformar os valores digitados porque os valores não são números, Valor 1 :{num1}, Valor 2: {num2}')
num1 = float(input('Digite o segundo número: '))
num2 = float(input('Digite o segundo número: '))
if num1 > num2:
    print('O {:.2f} é maior que {:.2f}!'.format(num1, num2))
elif num1 < num2:
    print('O {:.2f} é menor que {:.2f}!'.format(num1, num2))
else:
    print('Os números são iguais')
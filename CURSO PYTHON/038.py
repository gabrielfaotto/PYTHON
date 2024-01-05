num1=int(input('Digite um número: '))
num2=int(input('\nDigite outro número: '))
if num1 > num2:
    print('\nO número {} é maior que o número {}'.format(num1,num2))
elif num2 > num1:
    print('\nO número {} é maior que o número {}'.format(num2, num1))
else:
    print('\nOs números são iguais!!'.format(num1,num2))

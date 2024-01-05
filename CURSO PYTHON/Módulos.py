#Um módulo é um arquivo contendo definições e comandos em Python para serem usados 
#em outros programas em Python. Há diversos módulos do Python que fazem parte da biblioteca padrão.

from math import sqrt, ceil
num=int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz do número {} é igual a {}'.format(num, ceil(raiz)))

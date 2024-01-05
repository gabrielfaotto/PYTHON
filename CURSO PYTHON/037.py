num=int(input('Digite um número: '))
print('''Escolha um dos 3 metódos de conversão:
1 - Binário
2 - Octal
3 - Hexadecimal''')
esc=int(input('\nQual será sua escolha? '))
if esc == 1:
    print('\nO número {} em binário vale {}'.format(num, bin(num)[2:]))
elif esc == 2:
    print('\nO número {} em octal vale {}'.format(num, oct(num)[2:]))
elif esc == 3:
    print('\nO número {} em hexadecimal vale {}'.format(num, hex(num)[2:]))
else:
    print('\nEscolha uma das três opções!!')

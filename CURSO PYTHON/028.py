from random import randint
from time import sleep
num=randint(0,5)
resposta=int(input('Tente adivinhar o número de 0 a 5 que o computador gerou: '))
print('\nPROCESSANDO...')
sleep(2)

if num==resposta:
    print('\nVOCê ESTÁ CERTO, PARABÉNS!!')
else:
    print('\nVocê errou :(')
    print('\nO número gerado foi {}'.format(num))
    
print('\n--FIM--')
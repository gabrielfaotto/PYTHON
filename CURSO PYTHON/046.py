from time import sleep
from emoji import emojize
print('SE PREPARE PARA O GRANDE ESTOURO DE FOGOS!!')
resposta = str(input('VOCÊ ESTÁ PRONTO?? RESPONDA COM SIM OU NÃO!! ')).strip().upper()
if resposta == 'SIM':
    for i in range (10,0-1,-1):
        print(i)
        sleep(1)
    print(emojize(':fireworks::fireworks::fireworks::fireworks::fireworks:'))
elif resposta == 'NÃO':
    print('Fds vai ver mesmo assim:')
    for i in range (10,0-1,-1):
        print(i)
        sleep(1)
    print(emojize(':fireworks::fireworks::fireworks::fireworks::fireworks:'))
else:
    print('\nEscreve direito macaco')

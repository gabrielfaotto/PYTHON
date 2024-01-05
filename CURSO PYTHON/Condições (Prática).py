print('-----Seja bem vindo ao Pornhub!-----')
print('\nPara desfrutar de nosso conteúdo, responda a essa simples pergunta:')
idade=str(input('\nVocê é +18? Responda com SIM ou NÃO: ')).strip()
idadee=idade.upper()
if idadee == 'SIM':
    print('\nEntão aproveite nosso conteúdo :D!!')
elif idadee == 'NÃO':
    print('\nEntão VAZA!!')
else:
    print('Digite SIM ou NÃO!')
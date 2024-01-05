nomcomple=str(input('Digite seu nome completo: ')).strip()
print('\nSeu nome é {}'.format(nomcomple))
nomlist = nomcomple.split()
print('Seu primeiro nome é {}'.format(nomlist[0]))
print('Seu último nome é {}'.format(nomlist[-1]))


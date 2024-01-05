dist=float(input('Digite a distância da sua viagem em KM: '))
if dist<=200:
    preço=0.50*dist
    print('\nO preço da sua passagem, será de R${}'.format(preço))
else:
    preço=0.45*dist
    print('\nO preço da sua passagem, será de R${}'.format(preço))
print('\n--FIM--')
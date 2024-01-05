speed=float(input('Qual a velocidade do seu carro? '))
if speed>80:
    multa=(speed-80)*7
    print('\nVocê receberá uma multa de R${}'.format(multa))
else:
    print('\nEntão faz o L')
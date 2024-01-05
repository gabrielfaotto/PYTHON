d=int(input('Por quantos dias o carro foi alugado? '))
km=float(input('Quantos KM foram andados? '))
a=d*60
b=km*0.15
c=a+b
print('O valor total a pagar será de R${:.2f}'.format(c))
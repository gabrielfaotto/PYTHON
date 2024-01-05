sal=float(input('Digite o salário do funcionário: '))
aum=(sal*15)/100
pog=sal+aum
print('Um funcionário que ganhava {}, com 15% de desconto, passa a receber R${:.2f}'.format(sal, pog))
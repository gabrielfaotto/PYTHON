print('-='*20)
print('SEJA BEM VINDA AO SITE ALUGA BARRACOS!!')
print('\nPreencha as perguntas abaixo e te daremos a melhar resposta possível!!')
valcas=float(input('\nQual é o valor da casa? R$'))
sala=float(input('\nQual é o valor do seu salário? R$'))
prazo=int(input('\nEm quantos anos você irá pagar? '))
prest=valcas/(prazo*12)
porcem=(prest*100)/sala
if porcem > 30:
    print('\n\033[31mO EMPRÉSTIMO FOI NEGADO POIS A PRESTAÇÃO EXCEDE O LIMITE DE 30 PORCENTO DO SEU SALÁRIO!!\033[m')
else:
    print('\n\033[34mO EMPRÉSTIMO FOI APROVADO COM SUCESSO!! AS PRESTAÇÕES TERÃO O VALOR DE R${}\033[m'.format(prest))
print('-='*20)
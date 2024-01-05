print('{:=^40}'.format('LOJAS AMERICANAS!!'))
preço=float(input('\nQual é o preço das compras? R$'))
forma=int(input('''Qual será a forma de pagamento?
[1] À vista;
[2] À vista no cartão;
[3] Em até 2x no cartão;
[4] 3x ou mais no cartão.
Qual é a opção? '''))
if forma == 1:
    desconto = preço * 10 / 100
    preço = preço - desconto
    print('\nAo pagar à vista você ganhou um desconto de 10%, assim pagando R${:.2f}'.format(preço))
elif forma == 2:
    desconto = preço * 5 / 100
    preço = preço - desconto
    print('\nAo pagar à vista com cartão você ganhou um desconto de 5%, assim pagando R${:.2f}'.format(preço))
elif forma == 3:
    parcela=preço/2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif forma == 4:
    juros = preço * 20 / 100
    preço2 = preço + juros
    totparcela = int(input('\nQuantas parcelas? '))
    parcela = preço2 / totparcela
    print('\nAo escolher 3x ou mais no cartão você recebeu um juros de 20%, assim a compra será paga em {}x parcelas de R${:.2f}'.format(totparcela,parcela))
    print('\nResumindo, sua compra saiu de R${} para R${}'.format(preço,preço2))
else:
    print('Digite certo seu animal!!')
    
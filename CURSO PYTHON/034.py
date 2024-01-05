salá=float(input('Digite aqui seu salário: R$'))
if salá>1250:
    porcem=(salá*10)/100
    aumento=salá+porcem
    print('\nSeu salário era de R${}, e agora com um aumento de 10% é de R${}'.format(salá,aumento))
else:
    porcem=(salá*15)/100
    aumento=salá+porcem
    print('\nSeu salário era de R${}, e agora com um aumento de 15% é de R${}'.format(salá,aumento))
print('\n--FIM--')
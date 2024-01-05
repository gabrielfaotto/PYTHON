print('Responda as perguntas abaixo e te direi o seu IMC e a sua clasificação!!')
peso=int(input('\nDigite o seu peso: '))
altura=float(input('\nDigite a sua altura: '))
imc=peso/(altura**2)
if imc < 18.5:
    print('\nO seu IMC é {:.1f} e você está Abaixo do peso normal!'.format(imc))
elif 24.9 >= imc >= 18.5:
    print('\nO seu IMC é {:.1f} e você está em um Peso normal!'.format(imc))
elif 29.9 >= imc >= 25:
    print('\nO seu IMC é {:.1f} e você esta com Excesso de peso!'.format(imc))
elif 34.9 >= imc >= 30:
    print('\nO seu IMC é {:.1f} e você está com Obessidade classe I'.format(imc))
elif 39.9 >= imc >= 35:
    print('\nO seu IMC é {:.1f} e você está com Obessidade classe II'.format(imc))
else:
    print('\nO seu IMC é {:.1f} e você está com Obessidade Mórbida!'.format(imc))
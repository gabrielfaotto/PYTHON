from datetime import date
atual= date.today().year
print('-='*20)
print('SEJA BEM VINDO AO SITE DO EXÉRCITO BRASILEIRO!!')
print('\nResponda nossa questão AGORA :D')
nasc=int(input('\nQual é o seu ano de nascimento? '))
idade = atual - nasc
if idade < 18:
    bungas= nasc + 18
    print('\nVocê ainda não pode se alistar pois possui {} anos, mas no ano de {} será o seu grande momento!!'.format(idade,bungas))
elif idade == 18:
    print('MAS QUE MARAVILHA!! SE ALISTE JÁ!!')
else:
    bungas = nasc + 18
    print('\nInfelizmente você é burro e velho. Como você tem {} anos, já deveria ter se alistado no ano de {}!!'.format(idade, bungas))
print('-='*20)

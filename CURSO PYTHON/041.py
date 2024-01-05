from datetime import date
ano=date.today().year
print('Digite a idade do atleta que direi sua categoria!!')
nasc=int(input('\nQual é o ano de nascimento do atleta? '))
idade=ano-nasc
if idade <= 9:
    print('\nUm atleta com {} anos pertence a categoria MIRIM!'.format(idade))
elif 14 >= idade >= 10:
    print('\nUm atleta com {} anos pertence a categoria INFANTIL!'.format(idade))
elif 19 >= idade >= 15:
    print('\nUm atleta com {} anos pertence a categoria JUNIOR!'.format(idade))
elif 20>= idade >=25:
    print('\nUm atleta com {} anos pertence a categoria SÊNIOR!'.format(idade))
else:
    print('\nUm atleta com {} anos pertence a categoria MASTER'.format(idade))
from random import shuffle
p1=str(input('Digite o nome do primeiro aluno: '))
p2=str(input('Digite o nome do segundo aluno: '))
p3=str(input('Digite o nome do terceiro aluno: '))
p4=str(input('Digite o nome do quarto aluno: '))
lista=[p1,p2,p3,p4]
ordem=shuffle(lista)
print('A ordem de apresentação será {}'.format(ordem))
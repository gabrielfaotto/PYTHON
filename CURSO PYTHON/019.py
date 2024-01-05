from random import choice
alum=input('Digite o nome do primeiro aluno: ')
aludois=input('Digite o nome do segundo aluno: ')
alutrês=input('Digite o nome do terceiro aluno: ')
aluquatro=input('Digite o nome do quarto aluno: ')
lista=[alum,aludois,alutrês,aluquatro]
escolha=choice(lista)
print('O aluno(a) escolhido(a) foi o(a) {}'.format(escolha))
n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))
med=(n1+n2)/2
if med < 5:
    print('\nA média aluno é {:.1f} e ele está REPROVADO!!'.format(med))
elif 6.9 >= med >= 5:
    print('\nA média do aluno é {:.1f} e ele está de RECUPERAÇÃO!!'.format(med))
else:
    print('\nA média do aluno é {:.1f} e ele está APROVADO!!'.format(med))
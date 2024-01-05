Início = int(input('Digite o número inicial: '))
Fim = int(input('Digite o número final: '))
Passos = int(input('Será feito em quantos passos? '))
for i in range(Início,Fim+1,Passos):
    print(i)
print('FIM')
print('='*10)
a = 0
for c in range(0,2):
    n=int(input('Digite um valor: '))
    a=a+n
print('A soma dos valores é {}'.format(a))

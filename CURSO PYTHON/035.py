print('-=-'*15)
a=float(input('Primeiro segmento: '))
print('-=-'*15)
b=float(input('Segundo segmento: '))
print('-=-'*15)
c=float(input('Terceiro segmento: '))
if a<b+c and b<a+c and c<a+b:
    print('-=-'*15)
    print('É possível formar um TRIÂNGULO')
else:
    print('-=-'*15)
    print('NÃO é possível forma um TRIÂNGULO')
print('-=-'*15)
print('--FIM--')
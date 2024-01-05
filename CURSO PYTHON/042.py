a=float(input('Primeiro segmento: '))
b=float(input('Segundo segmento: '))
c=float(input('Terceio segmento: '))
if a<b+c and b<a+c and c<a+b:
    print('É possível criar um triângulo')
    if  a == b == c: 
        print('EQUILÁTERO')
    elif a == b or b == c or c == a:
        print('ISÓSCELES')
    elif a != b and b!=c and c!=a:
        print('ESCALENO')
else:
    print('Não é possível criar um triângulo );')
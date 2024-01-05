from math import hypot
catop=float(input('Digite o cateto oposto do triângulo: '))
catad=float(input('Digite o cateto adjacente do triângulo: '))
hip=hypot(catop,catad)
print('O comprimento da hipotenusa é igual a {:.2f}'.format(hip))
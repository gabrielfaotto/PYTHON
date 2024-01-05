from math import sin,cos,tan,radians
ang=float(input('Digite o ângulo que você deseja: '))
s=sin(radians(ang))
c=cos(radians(ang))
t=tan(radians(ang))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang,s))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang,c))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang,t))
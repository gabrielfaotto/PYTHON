n1=float(input('Digite uma quantidade de metros: '))
km=n1/1000
hm=n1/100
dam=n1/10
dm=n1*10
cm=n1*100
mm=n1*1000
print('A quantidade de {} metros em: \nMilimetros é {} \nCentímetros é {} \nDecímetros é {} \nDecâmetros é {} \nHectômetros é {} \nKilômetros é {}'.format(n1, mm, cm, dm, dam, hm, km))
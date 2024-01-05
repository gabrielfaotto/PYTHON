# Uma string é um tipo de dados usado para armazenar informações de texto. 
# São considerados tipos simples pois seus valores são compostos por uma sequência de caracteres, 
# podendo conter números, letras e pontuações. 
# As strings em Python são sempre colocadas entre aspas simples ou aspas duplas.


frase = 'Eu quero Gozar Agora!'
frase2 = '   Aprenda Sexo  '

#Irá substituir a palavra 'Agora' por 'Android':
print(frase.replace('Agora','Android'))

#Imprime a frase inteira em maiúsculo:
print(frase.upper())

#Imprime a frase inteira em minúsculo:
print(frase.lower())

#Imprime a frase deixando todas as letras em minúsculo, menos o primeiro caractere:
print(frase.capitalize())

#Imprime a frase com a primeira letra de cada palavra em maiúsculo
print(frase.title())

#Imprime a frase com todos os espaços indesejáveis apagados automaticamente
print(frase2.strip())

#Imprime a frase com todos os espaços indesejáveis do lado direito sejam apagados automaticamente
print(frase2.rstrip())

#Imprime a frase com todos os espaços indesejáveis do lado esquerdo sejam apagados automaticamente
print(frase2.lstrip())

# Uma string é um tipo de dados usado para armazenar informações de texto. 
# São considerados tipos simples pois seus valores são compostos por uma sequência de caracteres, 
# podendo conter números, letras e pontuações. 
# As strings em Python são sempre colocadas entre aspas simples ou aspas duplas.

frase= 'Eu quero gozar agora'

#Imprime apenas a letra que se encontra na casa 9
print(frase[9])

#Imprime apenas as letras que se encontram entre as casas 9 e 14
print(frase[9:14])

#Imprime apenas as letras que se encontram entre as casas 9 e 14 e pulando 2 casas
print(frase[9:14:2])

#Imprime todas as letras da frase até a casa 14
print(frase[:14])

#Imprime todo o restante das letras da frase após a casa 9
print(frase[9:])

#Imprime todo o restante das letras da frase após a casa 9 e sempre pulando 3 casas
print(frase[3::3])

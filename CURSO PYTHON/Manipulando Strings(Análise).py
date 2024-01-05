# Uma string é um tipo de dados usado para armazenar informações de texto. 
# São considerados tipos simples pois seus valores são compostos por uma sequência de caracteres, 
# podendo conter números, letras e pontuações. 
# As strings em Python são sempre colocadas entre aspas simples ou aspas duplas.

frase= 'Eu quero gozar agora'

#Imprime a quantidade de caracteres dentro da string:
print(len(frase))

#Imprime a quantidade de vezes que a letra 'o' aparece:
print(frase.count('o'))

#Imprime a quantidade de vezes que a letra 'o' aparece até o caractere 9:
print(frase.count('o',0,9))

#Imprime o número da casa onde se encontra o começo da palavra 'zar'
print(frase.find('zar'))

#Irá imprimir o valor -1 pois a string 'Android', não está nessa frase:
print(frase.find('Android'))

#Irá analisar com true ou false, se a palavra 'gozar' existe ou não na frase
print('gozar' in frase)
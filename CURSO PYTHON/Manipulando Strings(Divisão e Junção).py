# Uma string é um tipo de dados usado para armazenar informações de texto. 
# São considerados tipos simples pois seus valores são compostos por uma sequência de caracteres, 
# podendo conter números, letras e pontuações. 
# As strings em Python são sempre colocadas entre aspas simples ou aspas duplas.

frase= 'Eu quero Gozar Agora!'
frase2= 'Vou me matar hoje'

#Imprime todas as palavras da frase separadas, em uma espécie de lista 
print(frase.split())

#Imprime a frase com todos os espaços em branco preenchidos com '-'
print('-'.join(frase2))

print('mamei'.join(frase))
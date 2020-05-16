# desafio 31) faça um progama que leia um ano qualquer e mostre se ele é bissexto.
# formula. O ano resto da divisão 4 , se der 0 é bissexto. biblioteca datetime
from datetime import date
entrada = int(input('Que ano quer analizar? Coloque 0 para analizar o ano atual: '))
if entrada == 0:
    entrada = date.today().year   # formula para importar o ano atual do pc
if entrada % 4 == 0 and entrada % 100 != 0 or entrada % 400 == 0:
    print('O ano de {} é bissexto!'.format(entrada))
else:
    print('O ano {} não é bissexto!'.format(entrada))

#Desafio16/ Crie um progama que leia um numero real qualquer pelo teclado e mostre na tela a sua porção,
# inteira. quebrando um numero. import math e funçao math.trunc()
import math
entrada = float(input('Digite um numero: '))
print('O valor digitado foi {}\nE a sua porção inteira é {}'.format(entrada, math.trunc(entrada)))
# desafio17) faça um progama que leia o comprimeto do cateto oposto e do cateto adjacente de um
# triangulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math
entrada = float(input('Digite o valor do cateto oposto: '))
b = float(input('Digite o valor do cateto adjacente: '))
h = math.hypot(entrada, b)
print('Cateto oposto = {}\nCateto adjacente = {}\nO comprimento da hipotenusa é {:.2f}'.format(entrada, b, h))
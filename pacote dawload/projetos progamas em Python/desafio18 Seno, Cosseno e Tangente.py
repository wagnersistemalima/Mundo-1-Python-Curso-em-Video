#desafio18) seno\ coseno \ tagente. faça um progama que leia um angulo qualquer e mostre na tela
# o valor do seno,
# cosseno e tangente desse angulo.
import math
entrada = float(input('Digite o valor do angulo: '))
seno = math.sin(math.radians(entrada))
print('O angulo de: {} tem o seno de: {}'.format(entrada, seno))
cosseno = math.cos(math.radians(entrada))
print('O angulo de: {} Tem o cosseno de {:.2f}'.format(entrada, cosseno))
tangente = math.tan(math.radians(entrada))
print('O angulo de: {} tem a tangente de {:.2f}'.format(entrada, tangente))

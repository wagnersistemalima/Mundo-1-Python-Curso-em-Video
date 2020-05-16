#desafio28.1. Condicionais: Escreva um progama que faça o computador " Pensar" em um número inteiro entre 0 e 5,
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O progama deverá escrever na tela se o usuario venceu ou perdeu.
import random
import time # funções de tempo.
computador = random.randint(0, 5) # faz o computador sortear um numero aleatorio de 0 a 5.
print('--=--'*20)
print('Vou pensar em um numero entre 0 e 5. Tente advinhar....')
print('--=--'*20)
jogador = int(input('Em que número eu pensei? ')) # jogador tenta adivinhar
print('Processando...')
time.sleep(4) # função tempo, esperar 4 segundos. sleep
if jogador == computador:
    print('Parabêns você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}'. format(computador, jogador))




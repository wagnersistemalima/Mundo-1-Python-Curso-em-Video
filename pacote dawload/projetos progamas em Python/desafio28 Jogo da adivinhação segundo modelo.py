#desafio28. Condicionais: Escreva um progama que faça o computador " Pensar" em um número inteiro entre 0 e 5,
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O progama deverá escrever na tela se o usuario venceu ou perdeu.
import random
entrada =int(input('O computador está pensando em um numero de (1 a 5). Tente advinhar! '))
lista = [0, 1, 2, 3, 4, 5]
escolhido = random.choice(lista)
if entrada == escolhido :
    print('Parabêns você acertou!\nNumero {}'.format(entrada))
else :
    print('Você errou!\nNumero: {}'.format(entrada))
print('O computador pensou em {}'.format(escolhido))


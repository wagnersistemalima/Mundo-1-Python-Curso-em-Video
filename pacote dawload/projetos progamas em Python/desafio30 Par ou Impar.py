#desafio30) Crie um progama que leia um número inteiro e mostre na tela se ele é par ou impar.
entrada = int(input('Me diga um número qualquer: '))
if  entrada % 2 == 0 :
        print('O numero {} é par!'.format(entrada))
elif entrada % 2 == 1 :
    print('O número {} é ímpar'.format(entrada))
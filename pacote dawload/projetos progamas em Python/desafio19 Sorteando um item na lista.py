#desafio19) Um professor quer sortear um de seus quatro alunos para apagar o quadro. Faça um progama
# que ajude ele, lendo o nome deles e escrevendo o nome do escolhido. Utlizar import random/ random.choice
# random.choice= escolher um numero aleatorio numa lista.
from random import choice
a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno; '))
a4 = str(input('Digite o nome do quarto aluno: '))
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print('o aluno escolhido foi: {}'.format(escolhido))

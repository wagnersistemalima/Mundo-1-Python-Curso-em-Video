#desafio20/ O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos
# dos alunos. Faça um progama que leia o nome dos quatros alunos e moste a ordem sorteada. usando
#   import random ou from import random shuffle. random shuffle significa, embaralhar uma lista.
from random import shuffle
a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))
lista = [a1, a2, a3, a4]
ordem = shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)
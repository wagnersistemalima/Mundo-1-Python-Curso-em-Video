#desafio33. Faça um progama que leia três números e mostre qual é o maior e qual e o menor.
a = int(input())
b = int(input())
c = int(input())
#verificando que é o menor:
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#verificando quem é o maior:
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi: {}'.format(menor))
print('O maior valor digitado foi: {}'.format(maior))
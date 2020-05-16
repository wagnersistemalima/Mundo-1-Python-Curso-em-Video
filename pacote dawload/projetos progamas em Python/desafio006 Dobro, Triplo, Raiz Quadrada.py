# Desafio 006-Dobro, Triplo, Raiz Quadrada. Crie um algoritimo que leia um numero e mostre o seu dobro, triplo e raiz
# quadrada.
numero = int(input('Digite um número:'))
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = numero**(1 / 2)
print('O dobro de {} vale {}'.format(numero, dobro))
print('O triplo de {} vale {}'.format(numero, triplo))
print('A raiz quadrada de {} vale {:.2f}'.format(numero, raiz_quadrada))
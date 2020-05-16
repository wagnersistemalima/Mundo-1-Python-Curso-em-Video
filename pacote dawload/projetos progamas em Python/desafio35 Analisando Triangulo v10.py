#desafio35.desenvolva um progama que leia o comprimento de três retas e diga ão usuario se elas podem ou
# nao formar um triangulo.
print('-=-'*20)
print('Analizador de triângulos')
print('-=-'*20)
a = float(input('Primeiro segmento:'))
b = float(input('Segundo segmento:'))
c = float(input('Terceiro segmento:'))
if b - c < a < b + c and a - c < b < a + c and a - b < c < a + b:
    print('Os segmentos acima podem formar triângulo')
else:
    print('Os segmentos acima não podem formar triângulo')

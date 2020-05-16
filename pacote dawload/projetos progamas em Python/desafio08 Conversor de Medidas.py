# Desafio08  Conversor de Medidas- Escreva um progama que leia um valor em metros e o exiba convertido
#  em centimetros e milimetros.
entrada = float(input('Digite um valor:'))
c = entrada * 100
m = entrada * 1000
print('{} Metro(s) =\n{} Centimetros\n{} Milimetros'.format(entrada, c, m))

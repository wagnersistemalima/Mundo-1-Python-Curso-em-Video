#desafio 11. Calculando Descontos/faça um algoritimo que leia o preço de um produto e mostre se
# novo preço com 5% de desconto.
entrada = float(input('Digite o preço do produto:R$ '))
desconto = entrada * (5 / 100)
preco = entrada - desconto
print('O produto custa R$ {:.2f}\nCom 5% de desconto vai custar R$ {:.2f}'.format(entrada, preco))
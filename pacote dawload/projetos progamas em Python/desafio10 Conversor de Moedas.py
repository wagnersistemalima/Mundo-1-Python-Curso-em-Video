# desafio 10 Conversor de Moedas Crie um progama que leia quanto dinheiro uma pessoa tem na carteira,
#  e mostre quantos dolares ela pode comprar.
# Considere U$$1.00= R$ 3.27
entrada = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = entrada / 3.27
print('Com R$ {:.2f} Reais você consegue comprar U$$ {:.2f} Dolares'.format(entrada, dolar))
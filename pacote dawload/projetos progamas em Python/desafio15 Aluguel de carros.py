#desafio15 Aluguel de carros/ Escreva um progama que pergunte a quantidade de KM percorridos por um carro
#  alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
#  sabendo que o carro custa R$60 por dia e R$0.15 por KM rodado.
entrada = float(input('Quantos KM rodados? '))
dias = int(input('Quantos dias alugados? '))
aluguel = 60
km = 0.15
pagar = entrada * km + dias * aluguel
print('O total a pagar é de R${:.2f}'.format(pagar))

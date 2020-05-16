#desafio31. maneira 1. desenvolva um progama que pergunte a distancia de uma viagem em km.
# calcule o preço da passagem cobrando R$0.50 por km para viagens de até 200 km e R$0.45 para viagens mais longas.
entrada = float(input('Qual é a distancia da sua viagem? '))
if entrada >= 1 and entrada <= 200 :
    preco = entrada * 0.50
    print('Você está prestes a começar uma viagem de {:.1f}Km.'.format(entrada))
    print('e o preço de sua passagem será de R${:.2f}'.format(preco))
elif entrada > 200:
    preco = entrada * 0.45
    print('Você está prestes a começar uma viagem de {:.1f}Km'.format(entrada))
    print('E o preço de sua passagem será de R${:.2f}'.format(preco))
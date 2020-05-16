#desafio34. Escreva um progama que pergunte o salario de um fucionario e calcule o valor do seu aumento.
# para salarios superiores a R$1250.00, caucule um aumento de 10%.
# para os inferiores ou iguais, o aumento é de 15%.
entrada = float(input('Qual é o salario do fucionario? R$'))
if entrada <= 1250.00:
    salario = (entrada * 0.15) + entrada
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(entrada, salario))
else:
    if entrada > 1250.00:
        salario = entrada + (entrada * 10 / 100)
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(entrada, salario))
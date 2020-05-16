#Desafio13- Reajuste Salarial faça um algoritimo que leia o salário de um funcionario, e mostre seu
# novo salario com 15% de aumento.
entrada = float(input('Qual é o salário do fucionário? R$ '))
salario = (entrada * 15 / 100) + entrada
print('O fucionário que ganhava R$ {:.2f}\nCom 15% de aumento, passa a receber R$ {:.2f}'.format(entrada, salario))


# Desafio023 Separando digitos de um número.
# Faça um progama que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.
# Ex: digite um numero 1834
# unidade: 4 / dezena: 3 / centena: 8 / milhar: 1
hipotese = True

while hipotese:
    numero = int(input('Informe um número:'))      #
    unidade = numero // 1 % 10
    dezena = numero // 10 % 100
    centena = numero // 100 % 1000
    milhar = numero // 1000
    print('Unidade é {}'.format(unidade))
    print('dezena é {}'.format(dezena))
    print('Centena é {}'.format(centena))
    print('Milhar é {}'.format(milhar))
    print('-=-'*10)
    print('Quer continuar: [1] Sim / [2] Não')
    opcao = int(input('Sua opcaõ:'))
    while opcao < 1 or opcao > 2:
        print('Quer continuar: [1] Sim / [2] Não')
        opcao = int(input('Sua opção:'))
    if opcao == 2:
        hipotese = False



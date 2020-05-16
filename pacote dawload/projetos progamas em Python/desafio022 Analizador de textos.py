# Desafio 022
# Crie um progama que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas /  O nome com todas minusculas. /
# Quantas letras tem ao todo ( sem considerar os espaços)
# Quantas letras tem o primeiro nome.
hipotese = True
while hipotese:
    nome = str(input('Digite seu nome:')).strip()
    print('Analizando seu nome...')
    dividido = nome.split()
    primeiro_nome = dividido[0]
    print('Seu nome em maiúsculo é {}'.format(nome.upper()))
    print('Seu nome em minusculo é {}'.format(nome.lower()))
    print('Seu nome tem aõ todo {} letras'.format(len(nome) - nome.count(' ')))
    #print('Seu primeiro nome é {} e tem {} letras'.format(dividido[0], len(dividido[0])))
    print('Seu primeiro nome tem {} letras'.format(nome.find(' '))) # encontre o primeiro espaço depois do nome
    print('-=-'*15)
    print('Quer continuar: [1] Sim / [2] Não')
    opcao = int(input('Sua opção:'))
    while opcao < 1 or opcao > 2:
        print('Quer continuar: [1] Sim / [2] Não')
        opcao = int(input('Sua opcão:'))
    if opcao == 2:
        hipotese = False






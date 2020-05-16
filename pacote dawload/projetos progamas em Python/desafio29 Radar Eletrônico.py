#desafio 29) Escreva um progama que leia a velocidade de um carro. se ele ultrapassar 80 km/h, mostre uma
# mensagem dizendo que ele foi multado. A multa vai custar R$ 7.00 por cada km acima do limete.
entrada = float(input('Qual é a velocidade atual do carro? '))
if entrada > 80 :
    print('Multado! Você exedeu o limite permitido que é de 80km/h')
    multa = (entrada - 80) * 7.00
    print('Você deve pagar uma multa de: R$ {:.2f}'.format(multa))
else :
    print('Tenha um bom dia! Dirija com segurança!')

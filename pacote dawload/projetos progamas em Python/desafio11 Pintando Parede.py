#desafio 11 Pintando Parede. faça um progama que leia a largura e a altura de uma parede em
# metros, calcule a sua area e a quantidade de tinta necessaria para pintá-la,
# sabendo que cada litro de tinta, pinta uma area de 2m2.
largura = float(input('Digite a largura da parede em metros:'))
altura = float(input('Digite a altura da parede em metros:'))
area = largura * altura
litro = area / 2
print('Sua parede tem a dimenção de {} metros de largura\nPor {} metros de altura'.format(largura, altura))
print('{} m2 de area\nVai gastar {} litro(s)de tinta para pintar a parede'.format(area, litro))

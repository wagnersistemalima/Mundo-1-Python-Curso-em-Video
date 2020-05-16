#Desafio025 Procurando uma string dentro de outra.
# Crie um progama que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome.
nome = str(input('Qual é o seu nome completo?').strip())
#if nome.find('SILVA') > 0:
#    nome = True
#    print(nome)
#elif nome.find('SILVA') < 0:
#    nome = False
#    print(nome)
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))

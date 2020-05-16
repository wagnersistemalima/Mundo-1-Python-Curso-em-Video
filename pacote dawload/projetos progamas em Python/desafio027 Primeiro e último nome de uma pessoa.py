# Desafio026 Primeiro e ultimo nome de uma pessoa.
# Faça um progama que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome
# separadamente. Ex: Primeiro = Ana / Segundo = Sousa
nome = str(input('Digite seu nome completo:').strip().upper())
divisor = nome.split()
divisor_fim = len(divisor) - 1
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(divisor[0].title()))
print('Seu último nome é {}'.format(divisor[divisor_fim].title()))

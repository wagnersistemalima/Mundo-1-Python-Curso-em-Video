#desafio026 Primeira e ultima ocorrencia de uma string.
# Faça um progama que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra 'A'. / Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.
frase = str(input('Digite uma frase:').strip().upper())
print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A') + 1))
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A') + 1)) # procure pela direita 'A'
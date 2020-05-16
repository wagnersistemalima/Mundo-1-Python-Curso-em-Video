# desafio 007-Média Aritimetica/ desenvolva um progama que leia as duas notas de um aluno,
# calcule e mostre a sua média.
nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))
media = (nota1 + nota2) / 2
print('A media entre a nota {:.1f} e {:.1f} é {:.1f}'.format(nota1, nota2, media))

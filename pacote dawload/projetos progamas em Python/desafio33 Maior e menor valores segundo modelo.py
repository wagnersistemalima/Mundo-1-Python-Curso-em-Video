#desafio33. Faça um progama que leia três números e mostre qual é o maior e qual e o menor.
entrada = input().split()
a, b, c = entrada
a = int(a)
b = int(b)
c = int(c)
lista = []
lista.append(a)
lista.append(b)
lista.append(c)
lista.sort(reverse=True)
a = lista[0]
b = lista[1]
c = lista[2]
print('A ordem decrecente da lista é: {}\nE a ordem digitada foi: {}'.format(lista, entrada))
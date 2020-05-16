#Desafio024 Verificando as primeiras letras de um texto.
# Crie um progama que leia o nome de uma cidade e diga se ela começa ou não com o nome ''SANTO''
cidade = str(input("Em que cidade você nasceu?").strip())
divisor = cidade.split()
print(divisor[0].upper() == 'SANTO')

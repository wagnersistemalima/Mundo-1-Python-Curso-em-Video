#desafio14/ Conversor de Temperaturas. escreva um progama que converta uma temperatura digitada em C e converta para
# formula /  F = C * 1.8 + 32. / C = (F - 32)/ 1.8
entrada = float(input('Informe a temperatura em C: '))
f = entrada * 1.8 + 32
print('{:.1f} Graus Celsius corresponde a {:.1f} Graus Fahrenheit'.format(entrada, f))

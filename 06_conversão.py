# CONVERSÃO DE UNIDADES
# Autor: Miguel Bueno 
# Data: 24/09/2024
# Descrição: faça um algoritimo que receba um numero em pés, faça as conversões e a seguir mostre os resultados.

#entrada de dados
print (' ')
print ('CONVERSOR DE UNIDADES')
print (' ')
valor_pe = float(input('insira seu valor em pés: '))

#processamento de dados
valor_polegada = valor_pe * 12
valor_jarda = valor_pe / 3
valor_milha = valor_pe / 5280

valor_milha = round(valor_milha,4)
valor_jarda = round(valor_jarda,4)
valor_polegada = round(valor_polegada)

#saida de dados
print (f'o valor de {valor_pe} Pés equivale a:')
print (f'{valor_polegada} Polegadas')
print (f'{valor_jarda} Jardas')
print (f'{valor_milha} Milhas')
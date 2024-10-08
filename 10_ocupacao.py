# OCUPAÇÃO DO FUNCIONÁRIO
# Autor: Miguel Bueno 
# Data: 26/09/2024
# Faça um programa para exibir a ocupação de um funcionário a partir de seu código de profissão

#entrada de dados

print ('DESCUBRA SUA OCUPAÇÃO NA EMPRESA')
nome = input('Insira seu nome: ')
cod = int(input('Insira seu código de ocupação: '))

#processamento de dados
if cod == 1:
    ocup = 'Matemático'
elif cod == 2:
    ocup = 'Analista de Sistemas'
elif cod == 3:
    ocup = 'Físico'
elif cod == 4:
    ocup = 'Arquiteto'
elif cod == 5:
    ocup = 'Piloto de Aeronaves'
else:
    ocup = 'Indefinida'
 
 #saida de dados
print ( f'{nome} sua ocupação é {ocup}.')
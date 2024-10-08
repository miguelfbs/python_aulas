# MÊS DO ANO
# Autor: Miguel Bueno 
# Data: 26/09/2024
# Escreva um programa que leia a idade de um indivíduo e escreva a faixa etária a que pertence

#entrada de dados
print (' ')
idade = int(input ('insira sua idade: '))

#processamento de dados
if idade <= 12:
    faixa = 'Criança'
if idade >= 13 and idade <= 17:
    faixa = 'Adolescente'
if idade >= 18 and idade <= 59:
    faixa = 'Adulto'
if idade > 59:
    faixa = 'Especialista'

#saida de dados
print (' ')
print (f'Com base na sua idade ({idade} anos) sua faixa etária é "{faixa}" ')
print (' ')
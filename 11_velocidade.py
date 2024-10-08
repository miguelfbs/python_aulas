# MULTA DE VELOCIDADE
# Autor: Miguel Bueno 
# Data: 01/10/2024
# Escreva um programa que leia a velocidade máxima permitida em uma avenida e velocidade com que o motorista estava dirigindo nela e calcule a multa que uma pessoa vai receber.

#entrada de dados
print ('insira qual a velocidade que você estava percorrendo')
velocidade1 = int (input('insira sua velocidade: '))
permitida = 50
velocidade = velocidade1 - permitida

#processamento de dados
if velocidade <= 0:
    print ('Você não tem multa')
    multa = 'inexistente'
if velocidade > 0 and velocidade <= 10:
    print (f'sua multa é de R$50.00, pois você ultrapassou {velocidade}km/h do permitido')
    multa = 'R$50,00'
if velocidade >= 11 and velocidade <= 30:
    print (f'sua multa é de R$100.00, pois você ultrapassou {velocidade}km/h do permitido')
    multa = 'R$100,00'
if velocidade > 30:
    print (f'sua multa é de R$200.00, pois você ultrapassou {velocidade}km/h do permitido')
    multa = 'R$200,00'

#saida de dados
print ('Dados:')
print (f'Limite: {permitida}km/h')
print (f'Velocidade: {velocidade1}km/h')
print (f'Multa: {multa}')
# AUMENTO DE SALÁRIO
# Autor: Miguel Bueno 
# Data: 26/09/2024
# Descrição: Faça um programa que receba o salário de um funcionário, calcule e mostre o novo
#            salário, sabendo-se que:
#            Salário < R$ 1000,00 aumento de 25%.
#            Salário >= R$ 1000,00 e < R$ 2000,00 aumento de 15%.
#            Salário >= R$ 2000,00 aumento de 10%.
# entrada de dados
# proceessamento de dados
# saída de dados

#entrada de dados
nome = input ('insira seu nome: ')
print ('PARABÉNS')
print ('Você terá um aumento de salário')

#processamento de dados e saída de dados
salario = float(input('insira seu salário atual: '))
if salario  <  1000:
    salario = salario * 1.25
    salario = round(salario,2)
    print (' ')
    print (f'{nome}, Seu novo salário é de R${salario} com aumento de 25%')
if salario >= 1000 and salario < 2000:
    salario = salario * 1.15
    salario = round(salario,2)
    print (' ')
    print (f'{nome}, Seu novo salário é de R${salario} com aumento de 15%')
if salario >= 2000:
    salario = salario * 1.10
    salario = round(salario,2)
    print (' ')
    print (f'{nome}, Seu novo salário é de R${salario} com aumento de 10%')

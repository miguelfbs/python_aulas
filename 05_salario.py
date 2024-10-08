# SALARIO
# Autor: Miguel Bueno 
# Data: 24/09/2024
# Descrição: faça um algorítimo que colete o valor do salário do funcionário e acrescente 25% de aumento

#entrda de dados
print (' ')
print ('você terá um aumento de salário!')
print (' ')
salario_atual = input(('insira seu salário atual:'))

#processamento
salario_atual = float(salario_atual)
salario_final = salario_atual + (salario_atual * 0.25)

#saída de dados
print (f'seu novo salário é de R${salario_final}, com um aumento de 25%')
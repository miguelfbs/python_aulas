# ANALISAR TRIÃNGULO
# Autor: Miguel Bueno 
# Data: 01/10/2024
#Faça um programa que receba 3 valores e verifique se eles podem representar os lados em um triângulo

#entrada de dados
print(' ')
lado1 = int(input('insira o valor do primeiro lado do triângulo: '))
print(f'lado 1 = {lado1}')
print(' ')
lado2 = int(input('insira o valor do segundo lado do triângulo: '))
print(f'lado 2 = {lado2}')
print(' ')
lado3 = int(input('insira o valor do terceiro lado do triângulo: '))
print (f'lado 3 = {lado3}')
print (' ')

# processamento de dados
if lado1 <= 0:
    triangulo = 'inválido'
elif lado2 <= 0:
    triangulo = 'inválido'
elif lado3 <= 0:
    triangulo = 'inválido'
elif lado1 > (lado2 + lado3):
    triangulo = 'inválido'
elif lado2 > (lado1 + lado3):
    triangulo = 'inválido'
elif lado3 > (lado1 + lado2):
    triangulo = 'inválido'
elif lado1 == lado2 == lado3:
    triangulo = 'Equilátero'
elif lado1 == lado2: 
    triangulo = 'Isóceles'
elif lado3 == lado2: 
    triangulo = 'Isóceles'
elif lado1 == lado3:
    triangulo = 'Isóceles'
else:
    triangulo = 'Escaleno'

#saida de dados

print (f'seu triângulo é {triangulo}')
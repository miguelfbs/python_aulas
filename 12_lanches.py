# CODIGO LANCHES
# Autor: Miguel Bueno 
# Data: 01/10/2024
#Escreva um algoritmo para exibir o nome do lanche a partir da entrada do número do mesmo pelo usuário

#entrada de dados

print (' ')
print ('BEM VINDO A LANCHONETE')
print ('OS CÓDIGOS DAS OPÇÕES DE LANCHES SÃO: ')
print (' ')
print ('Big Mac = 1')
print ('Quarteirão = 2')
print ('McChicken = 3')
print ('Cheddar McMelt = 4')
print ('McMax = 5')
print (' ')
cod_lanche = int(input('insira o código do seu lanche: '))
print (' ')
print ('AGORA VEJA OS CÓDIGOS DAS OPÇÕES DE ACOMPANHAMENTOS: ')
print ('Coca-cola = 1')
print ('Fanta = 2')
print ('Guaraná = 3')
print ('Sprite = 4')
cod_bebida = int(input('insira o código da sua bebida: '))

#processamento de dados

if cod_lanche == 1:
    lanche = 'Big Mac'
elif cod_lanche == 2:
    lanche = 'Quarteirão'
elif cod_lanche == 3:
    lanche = 'McChiken'
elif cod_lanche == 4:
    lanche = 'Cheddar McMelt'
elif cod_lanche == 5:
    lanche = 'McMax'
else:
    lanche = '  '

if cod_bebida == 1:
    bebida = 'Coca-cola'
elif cod_bebida == 2:
    bebida = 'Fanta'
elif cod_bebida == 3:
    bebida = 'Guaraná'
elif cod_bebida == 4:
    bebida = 'Sprite'
else:
    bebida = '  '

#saída de dados

print (' ')
print (f'O seu pedido foi: um {lanche}, acompanhado de um copo de {bebida}.')
print ('Aguarde o seu pedido ser feito, Obrigado')
print (' ')
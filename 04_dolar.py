# DÓLAR
# Autor: Miguel Bueno 
# Data: 19/09/2024
# Descrição: faça um algorítimo que um valor na moeda real (R$), a cotação da conversão em REAL para DOLAR, e apresente a quantidade desse valor em dólar ($)

#Entrada

print ('qual seu valor em reais (R$)') 
real = float(input('Inserir valor:'))
        
cotacao = float(input('Insira o valor da cotação de hoje:'))

#processamento de dados
cotacao = float(cotacao)
real = float(real)

dolar = real/cotacao

#saida de dados
print (f'R${real} equivalem a ${dolar}')



# MÊS DO ANO
# Autor: Miguel Bueno 
# Data: 26/09/2024
# Descrição: Faça um programa que receba o mês em número e apresente-o por extenso.

#entrada de dados
print ('Mêses do Ano')
mes = int(input('insira o número deste mês: '))

#processamento de dados
if mes == 1:
    mes = 'JANEIRO'
elif mes == 2:
    mes = 'FEVEREIRO'
elif mes == 3:
    mes = 'MARÇO'
elif mes == 4:
    mes = 'ABRIL'
elif mes == 5:
    mes = 'MAIO'
elif mes == 6:
    mes = 'JUNHO'
elif mes == 7:
    mes = 'JULHO'
elif mes == 8:
    mes = 'AGOSTO'
elif mes == 9:
    mes = 'SETEMBRO'
elif mes == 10:
    mes = 'OUTUBRO'
elif mes == 11: 
    mes = 'NOVEMBRO'
elif mes == 12:
    mes = 'DEZEMBRO'
else:
    mes = 'não existe'

#saida de dados
print (f'o mês do ano: {mes}')
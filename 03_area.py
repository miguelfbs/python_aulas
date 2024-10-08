# CÁUCULO ÁREA
# Autor: Miguel Bueno 
# Data: 19/09/2024
# Descrição: Caucular a área do circulo utilizando seu raio

#entrada de dados
diametro = float(input('insira o diâmetro do circulo:'))

#processamento
raio = diametro / 2
area = 3.14 * (raio * raio)
area = str(area)

#saída
print ('a Área do seu circulo é '+ area)

import random

def adivinhar_numero():
    numero_correto = random.randint(1, 100)  
    tentativas = 8 
    print(' ')
    print('TENTE ADIVINHAR UM NÚMERO ENTRE 1 e 100!')
    print (' ')
    
    while tentativas > 0:
        try:
            palpite = int(input(f"VOCÊ TEM {tentativas} TENTATIVAS? "))
        except ValueError:
            print('INSIRA UM VALOR VÁLIDO')
            continue
        
        if palpite < 1 or palpite > 100:
            print('O NÚMERO DEVE ESTAR ENTRE 1 e 100')
            continue

        if palpite == numero_correto:
            print('VOCÊ ACERTOU')
            break
        else:
            tentativas -= 1
            if palpite < numero_correto:
                print('TENTE UM MAIOR')
            else:
                print('TENTE UM MENOR')

            if tentativas > 0:
                print(f'TENTE NOVAMENTE, {tentativas} TENTATIVAS RESTANTES')
            else:
                print(f'FIM DE JOGO! A RESPOSTA É {numero_correto}.')

if __name__ == '__main__':
    adivinhar_numero()



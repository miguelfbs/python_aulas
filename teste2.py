def nome()
    nome_correto = miguel
    tentativas = 3
    print ('escreva o nome "miguel"')
    while tentativa > 0:
        try:
             palpite = str(input(escreva a resposta: ))
        except ValueError:
            print ('insira uma resposta válida')
            continue
        if palpite = nome_correto:
            print ('nome correto')
            break
        else tentativa -= 1
            if palpite != nome_correto:
            print ('nome incorreto')
            if tentativas > 0:
            print (f'tente denovo, você tem {tentativas} chances')
            else:
            print ('fim de jogo')

        

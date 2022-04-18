def tratamentoDeDados(valor):
    saida = valor
    while(True):
        if(saida <= 0):
            print("A resposta inserida não é válida")
            resposta = input("Voce deseja encerrar o cadastro?[S/N]\n")
            if (resposta == 'S'):
                return False,saida 
                break
            elif (resposta == 'N'):
                if(type(saida) is int):
                    saida = int(input("Insira um novo número maior que zero: \n"))
                elif(type(saida) is float):
                    saida = float(input("Insira um novo número maior que zero: \n"))
        else:
            return True,saida
            break

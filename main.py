from tratamentoDeDados import *
from prettytable import PrettyTable

somaFinal = 0
cadastro = 0
tamanhoDoEstoque = 3
iD = 1
mercadorias = {1: "0"}


while (cadastro == 0):
    control=[True]*4
    loop = True
    
    
    nomeDaMercadoria = input("Digite o nome da mercadoria: \n")
    
    control[0], quantidadeMinima = tratamentoDeDados(int(input("Digite a quantidade mínima da mercadoria: \n")))
    control[1], quantidadeAtual = tratamentoDeDados(int(input("Quantidade Atual da mercadoria: \n")))
    control[2], quantidadeMaxima = tratamentoDeDados(int(input("Quantidade máxima da mercadoria: \n")))
    control[3], valorUnitario = tratamentoDeDados(float(input("Valor unitário da mercadoria: \n")))
    valorUnitario = round(valorUnitario,2)
    valorTotal = round(quantidadeAtual*valorUnitario,2)
    if (control[0] and control[1] and control[2] and control[3]):
        if(iD > tamanhoDoEstoque):
            flag = True
            
        else:
            flag = False
        if flag:
            resposta = input("O estoque atingiu a cacidade máxima, você deseja substituir alguma mercadoria no estoque para a que está sendo cadastrada? [S/N]")
            if(resposta == 'S'):
                iD_aux = int(input("Digite o iD da mercadoria: \n"))
                mercadorias[iD_aux] = [nomeDaMercadoria,quantidadeMinima,quantidadeAtual,quantidadeMaxima,valorUnitario,valorTotal]
            elif(resposta == 'N'):
                print("Retornando ao inicio do cadastro")
        else:
            mercadorias[iD] = [nomeDaMercadoria,quantidadeMinima,quantidadeAtual, quantidadeMaxima,valorUnitario,valorTotal]
            iD += 1
    maisMercadorias = input("Deseja adicionar mais mercadorias? [S/N] \n")
    if maisMercadorias == 'N':
        print("O relatório será exibido")
        cadastro = 1

tabela = PrettyTable()
tabela.field_names = ["Nome da Mercadoria", "Quantidade Mínima", "Quantidade Atual", "Quantidade Máxima", "Valor Unitário","Valor Total"]
for cont in range(1,len(mercadorias)+1):
    somaFinal = somaFinal + mercadorias[cont][5]
    tabela.add_row(mercadorias[cont])

tabela2 = PrettyTable()
tabela2.field_names = ["Valor Total"]
tabela2.add_row([somaFinal])
    

print(tabela)
print("_____________________________________________________")
print(tabela2)







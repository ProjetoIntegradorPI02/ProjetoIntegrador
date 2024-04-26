a=100

comando=int(input("Aperte 0 para Inicia:"))
while comando !=0:
  comando=int(input("Aperte 0 para Inicia:"))
for i in range(a):
    
   if comando<1 or comando >4:
    
    print("\n _______________________________________________")
    print("|\t\tSistema Online\t\t\t|")
    print("|_______________________________________________|\n\n")
    print("[1]Cadastrar Produto\n[2]Deletar Produto\n[3]Editar Produto\n[4]Pesquisar Produto\n ")

    comando=int(input("Resposta:"))
if comando==1:
    estoque={}
    quant_produtos=int(input("Quantos produtos quer cadastrar:"))
    for i in range(quant_produtos):
     
     cadastrar=["Cadastrar Produto","Cadastrar outro Produto"]
     print("\n\n ________________________________________________")
     print("|\t\t",cadastrar[i],"\t\t|")
     print("|_______________________________________________|\n")
     codigo_produto=int(input("digite codigo do produto:\n"))
     nome_produto=str(input("Nome do Produto:\n"))
     desc_produto=str(input("Descrição do Produto:\n"))
     CP=int(input("Valor do produto:\n"))
     CF=int(input("Custo fixo do produto:\n"))
     CV=int(input("Comissão de vendas:\n"))
     IV=int(input("Impostos:\n"))
     ML=int(input("Quanto de rentabilidade:"))
     estoque[codigo_produto]={'Nome':nome_produto,
                              'Descriçao':desc_produto, 
                              'CP':CP,
                              'CF':CF,
                              'CV':CV,
                              'IV':IV,
                              'ML':ML}
     contador=CP+CF+CV+IV+ML
     if ML>100:
        print("Sua rentabilidade n pode ser maior q 100%")
        ML=int(input("Digite novamente"))

     if contador >100:
      print('\nPor favor digite novamente os valores, a soma entre os valores n pode ser superior a 100.\n')
      codigo_produto=int(input("digite codigo do produto:\n"))
      nome_produto=str(input("Nome do Produto:\n"))
      desc_produto=str(input("Descrição do Produto:\n"))
      CP=int(input("Valor do produto:\n"))
      CF=int(input("Custo fixo do produto:\n"))
      CV=int(input("Comissão de vendas:\n"))
      IV=int(input("Impostos:"))
      ML=(input("Quanto de rentabilidade:"))
print("\n\n ________________________________________________")
print("|\t\tPRODUTO CADASTRADO\t\t|")
print("|_______________________________________________|\n")
print("Deseja exibir o calculo?\n[1]SIM\n[2]NÂO")
exibir_calculo=int(input("Resposta:"))
if exibir_calculo <=0 or exibir_calculo >2:
    print("Deseja exibir o calculo?\n[1]SIM\n[2]NÂO")
    exibir_calculo=input("Digite 1 para SIM e 2 para NÂO:")
if exibir_calculo ==1:
    for codigo_produto, produto in estoque.items():
        PV = produto['CP'] / (1 - ((produto['CF'] + produto['CV'] + produto['IV'] + produto['ML']) / 100))
       
     
        PV1 = (PV / produto['CP']) * 100
        CPP = (produto['CP'] / PV) * 100
        RC = PV - produto['CP']
        RC1 = (RC / PV) * 100
        CF1 = (produto['CF'] * PV) / 100
        CV1 = (produto['CV'] * PV) / 100
        IV1 = (produto['IV'] * PV) / 100
        OC = produto['CF'] + produto['CV'] + produto['IV']
        OCP = (OC * PV) / 100
        RENT = produto['CP'] + OC
        rent = PV - RENT
        RENT1 = (rent / PV) * 100
        #Tabela
        print("----------------------------------------------------------------------")
        print('\t\t\t',produto['Nome'], produto['Descriçao'])
        print('----------------------------------------------------------------------')
        print(f"Descrição\t\t\t Valor \t\t\t %")
        print('----------------------------------------------------------------------')
        print(f"Preço de venda\t\t\t R${PV:.2f}\t\t{PV1:.2f} %")
        print('----------------------------------------------------------------------')
        print(f"Preço do produto\t\t R${CP:.2f}\t\t{CPP:.2f} %")
        print('----------------------------------------------------------------------')
        print(f"RECEITA BRUTA\t\t\t R${RC:.2f}\t\t{RC1:.2f} %")
        print('----------------------------------------------------------------------')
        print(f"CUSTO FIXO\t\t\t R${CF1:.2f}\t\t{CF:.2f} %")
        print('----------------------------------------------------------------------')
        print(f"COMISSÃO DE VENDAS\t\t R${CV1:.2f}\t\t\t{CV:.2f} %")
        print('----------------------------------------------------------------------')
        print(f"IMPOSTOS\t\t\t R${IV1:.2f}\t\t\t{IV:.2f} %")
        print('----------------------------------------------------------------------')
        print(f"OUTROS CUSTOS\t\t\t R${OCP:.2f}\t\t{OC:.2f} %")
        print('----------------------------------------------------------------------')
        print(f"RENTABILIDADE\t\t\t R${RENT1:.2f}\t\t{ML:.2f} %")
        print('----------------------------------------------------------------------')

        #Tabela de Lucros

        if RENT1 > 20:
          print('\033[34m'+'Lucro: Alto'+ '\033[0m') #34m imprime em cor azul

        elif RENT1 >= 10 and RENT1 <= 20:
          print('\033[32m'+'Lucro: Medio'+ '\033[0m') #32m imprime em cor verde


        elif RENT1 > 0 and RENT1 < 10:
          print('\033[33m'+'Lucro: Baixo'+ '\033[0m') #33m imprime em cor amarela

        elif RENT1 == 0:
          print('Lucro: Em Equilibrio'+ '\033[0m')

        else:
         print('\033[31m'+'Em Prejuizo'+ '\033[0m') #31m imprime em cor vermelha
if exibir_calculo==2:
        print("[1]Deletar Produto\n[2]Editar Produto\n[3]Pesquisar Produto\n[4]Encerrar Programa ")
        comando=input("Resposta:")
        if comando<1 or comando >4:
         print("[1]Deletar Produto\n[2]Editar Produto\n[3]Pesquisar Produto\n[4]Encerrar Programa ")
         comando=input("Resposta:")
        if comando==4:
            print("\n\n ________________________________________________")
            print("|\t\tPROGRAMA ENCERRADO\t\t|")
            print("|_______________________________________________|\n")
        
        
if comando==2:
    print("\n\n ________________________________________________")
    print("|\t\tDeletar Produto\t\t|")
    print("|_______________________________________________|\n")
 
if comando==3:
    print("\n\n ________________________________________________")
    print("|\t\tEditar Produto\t\t|")
    print("|_______________________________________________|\n")
  
if comando==4:
    print("\n\n ________________________________________________")
    print("|\t\tPesquisar Produto\t\t|")
    print("|_______________________________________________|\n")
  

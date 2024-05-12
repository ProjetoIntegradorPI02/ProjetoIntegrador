
# Programa para o Calculo do Preço de Venda
import oracledb
#
connection = oracledb.connect(
    user = "BD150224438",
    password = "Yxcjw1",
    dsn = "172.16.12.14/xe"
)
print('Conectado')


cursor = connection.cursor() 

#Inicio do Programas
while True:
    BDC=1
    codigo_campos=0
    contador=0
    print("\n") 
    print("_"*55)
    print("\t   Programa Controle de Estoque")
    print("-"*55)
    print ("\033[32m[1] Exibir Calculo \033[0m   \n[2] Cadastrar Produto \n\033[33m[3] Editar Produto Cadastrado\033[0m \n\033[31m[4] Apagar Produto\033[0m\n[5] Banco De Dados")
    num_tela = int ( input ("\033[47m\033[30mEscolha a Opção Desejada: \033[0m"))#\033[47m Codigo pra definir cor de fundo,\033[30m Define cor do testo como preta
   
   
    while num_tela not in [1, 2,3,4,5]:
        print ("\033[32m[1] Exibir Calculo\033[0m   \n[2] Cadastrar Produto \n\033[33m[3] Editar Produto Cadastrado\033[0m \n\033[31m[4] Apagar Produto\033[0m[5] Banco De Dados")
        num_tela = int ( input ("\033[47m\033[30mEscolha a Opção Desejada: \033[0m"))
        
    while num_tela>0:
     if num_tela == 1:
        print("_"*55)
        print("\t   Vizualizar Calculo")
        print("-"*55)
        

        #Informaçoes do Produto
        codigo_produto= int(input('\n\033[47m\033[30mDigite o Código do Produto: \033[0m'))

        tabela_produtos = {}
        codigo_excluir=0
        cursor.execute(f"SELECT * FROM proodutos WHERE codigo = {codigo_produto}")
        tabela_produtos[codigo_produto] = cursor.fetchone()  

        for produto in tabela_produtos.values():
            nome_produto = produto[1]
            descricao_produto = produto[2]
            CP = produto[3]
            CF = produto[4]
            CV = produto[5]
            IV = produto[6]
            ML = produto[7]

        #Formula Calculo Preço de Venda
        PV = CP / ( 1 - ( ( CF + CV + IV + ML) / (100) ) )
        #Cáloulos das % e valores
        #%Preço de venda
        PV1= (PV/PV) * 100
        #%Custo do produto
        CPP= (CP/PV) * 100
        #Receita bruta 
        RC= PV - CP
        #% Receita bruta
        RC1= (RC/PV) * 100
        #% Custo fixo
        CF1= (CF*PV) / 100
        #% Comissão de vendas
        CV1= (CV*PV) / 100
        #% Impostos
        IV1= (IV*PV) / 100
        # Outros custos
        OC= CF+ CV+ IV
        # %Outros custos
        OCP= (OC*PV) / 100
        #Rentabilidade
        RENT= CP+ OC
        rent=PV-RENT
        #% Rentabilidade
        RENT1= (ML*PV) / 100
        #Tabela
        print("\033[32m-\033[0m" * 55)
        print(f"\033[32m{nome_produto:^50}\033[0m")
        print(f"\033[32m{descricao_produto:^50}\033[32m")
        print("\033[32m-\033[0m" * 55)
        print(f"{'\033[47m\033[30mDescrição\033[0m':<20}\t\t\t{'\033[47m\033[30mValor\033[0m':>15}\t{'\033[47m\033[30m%\033[0m':>15}")
        print("\033[32m-\033[0m" * 55)
        print(f"\033[32m{'Preço de venda':<20}\033[0mR${PV:>15.2f}{PV1:>15.2f} %")
        print("\033[32m-\033[0m" * 55)
        print(f"\033[32m{'Preço do produto':<20}\033[0mR${CP:>15.2f}{CPP:>14.1f} %")
        print("\033[32m-\033[0m" * 55)
        print(f"\033[32m{'RECEITA BRUTA':<20}\033[0mR${RC:>15.2f}{RC1:>15.2f} %")
        print("\033[32m-\033[0m" * 55)
        print(f"\033[32m{'CUSTO FIXO':<20}\033[0mR${CF1:>15.2f}{CF:>15.2f} %")
        print("\033[32m-\033[0m" * 55)     
        print(f"\033[32m{'COMISSÃO DE VENDAS':<20}\033[0mR${CV1:>15.2f}{CV:>15.2f} %")
        print("\033[32m-\033[0m" * 55)
        print(f"\033[32m{'IMPOSTOS':<20}\033[0mR${IV1:>15.2f}{IV:>15.2f} %")
        print("\033[32m-\033[0m" * 55)
        print(f"\033[32m{'OUTROS CUSTOS':<20}\033[0mR${OCP:>15.2f}{OC:>15.2f} %")
        print("\033[32m-\033[0m" * 55)
        print(f"\033[32m{'RENTABILIDADE':<20}\033[0mR${RENT1:>15.2f}{ML:>14.1f} %")
        print("\033[32m-\033[0m" * 55)
        
        #Tabela de Lucros

        if RENT1 > 20:
            print('\t\t\033[34m'+'Lucro: Alto'+ '\033[0m') #34m imprime em cor azul

        elif RENT1 >= 10 and RENT1 <= 20:
            print('\t\t\033[32m'+'Lucro: Medio'+ '\033[0m') #32m imprime em cor verde

        elif RENT1 > 0 and RENT1 < 10:
            print('\t\t\033[33m'+'Lucro: Baixo'+ '\033[0m') #33m imprime em cor amarela

        elif RENT1 == 0:
            print('\t\tLucro: Em Equilibrio'+ '\033[0m')

        else:
            print('\t\t\033[31m'+'Em Prejuizo'+ '\033[0m') #31m imprime em cor vermelha

        print("\033[31m[1] Excluir\033[0m \n\033[33m[2] Editar\033[0m  \n[0]Sair")
        contador=1
        num=int(input("\033[47m\033[30mOpção Desejada: \033[0m"))
        while num not in [1, 2,0]:
           print("\033[31m[1] Excluir\033[0m \n\033[33m[2] Editar\033[0m  \n[0]Sair")
           contador=1
           num=int(input("\033[47m\033[30mOpção Desejada: \033[0m"))
        if num==1:
            num_tela=4
        if num==2:
            num_tela=3
        if num==0:
            num_tela=0
    



        #o comando '\033[0m' redefine a cor do terminal para o padrão após o termino do  print'''

    #cadastro de produtos
     elif num_tela == 2: 
        print("\n")
        print("_"*55)
        print("\t\t   Cadastro de Produto")
        print("-"*55)
        
        #Inputs pra receber dados do produto
        nome_cadastro =  input ("Nome do Produto: ")
        descricao_cadastro =  input ( "Descrição do Produto: ")
        codigo_cadastro = int (input("Cadastre o Código Para o Produto: "))
        custo_cadastro = float ( input ( "Custo do Produto: "))
        comissao_cadastro =  float ( input ("Qual a Taxa de Comissão de Vendas: "))
        fixo_cadastro = float ( input ("Qual a Taxa de Custo Fixo: "))
        impostos_cadastro =  float ( input ("Qual a Taxa de Impostos: "))
        rentabilidade_cadastro = float ( input ("Rentabilidade Esperada: "))

        #Primeiro comando pra salvar no banco de dados.
        cursor.execute(f'''INSERT INTO Proodutos VALUES({codigo_cadastro},'{nome_cadastro}','{descricao_cadastro}',
                {custo_cadastro},{fixo_cadastro},{comissao_cadastro},{impostos_cadastro},{rentabilidade_cadastro})'''
                )
        
        print("-"*55)
        print ("\t\tReveja as Informações")
        print(f'\t{nome_cadastro},{descricao_cadastro}')
        print("-"*55)

        print(f"\033[32mPreço de Aquisição\t\tR${custo_cadastro :.1f}\033[0m")
        print(f"\033[32mCusto Fixo       \t\t{fixo_cadastro} %\033[0m")
        print(f"\033[32mComissão de Vendas\t\t{comissao_cadastro} %\033[0m")
        print(f"\033[32mImpostos          \t\t{impostos_cadastro} %\033[0m")
        print(f"\033[32mRentabilidade     \t\t{rentabilidade_cadastro} %\033[0m")

        print("\t\t\nDeseja Confirmar as Opções ?\n")
        print("\033[32m[1] Para Confirmar\033[0m \n\033[31m[2] Para Cancelar\n\033[0m")
        opcao_cadastro = input("\033[47m\033[30mOpção Desejada: \033[0m")

        while opcao_cadastro not in ['1', '2']:#Verificação de entrada
            print("\033[41mERRO\033[0m")#\033[41m Codigo pra definir cor de fundo, No caso dessa linha ermelho
            print("\033[32m[1] Para Confirmar\033[0m \n\033[31m[2] Para Cancelar\n\033[0m")
            opcao_cadastro = input ("\033[47m\033[30mOpção Desejada: \033[0m")

        if opcao_cadastro=='1':
            cursor.execute("commit") #Confirma o Cadastro e Registra os Dados no Banco de Dados
            print("_"*55)
            print("\t\t\033[42mCadastro Concluido.\033[0m")
            print("-"*55)

            num_tela=0#Condição pra volta pra tela inicial
        else:
            num_tela=0#Condição pra volta pra tela inicial
       
           
     if num_tela == 3:
        
        print("\n")
        print("_"*55)
        print("\t\t   Editar Produto")
        print("-"*55)
        if num_tela==3 or contador==0 or confirmar_editar==1:
            if num_tela==3 and contador==0:
                print("\n\t\t\t\033[42mATENÇÃO!!!\033[0m\n\n")
                print("Antes De voçê editar Dados Da Tabela Sujerimos Pesquisar Primeiro.\n")
                print("\033[32m[1]Visualizar\033[0m\n\033[31m[2]Continuar\033[0m\n[0]Voltar")
                Verificar_Dados=int(input("\033[47m\033[30mOpção Desejada: \033[0m"))


                while codigo_campos not in [1, 2,0]:#Verificação de entrada
                    print("\t\033[41mERRO\033[0m\n")
                    Verificar_Dados=int(input("\033[47m\033[30mOpção Desejada: \033[0m"))

                if Verificar_Dados ==0:#Verificar dados ==0 vai voltar pra tela inicial do programa
                     num_tela=0

                if Verificar_Dados==1:#Verificar dados ==1 vai voltar pra tela de pesquisa do programa
                    num_tela=1

                if Verificar_Dados==2:#Verificar dados ==2 o programa continua na edição do Banco de Dados
                    contador=1
            if num_tela==3 and contador==1:
                print("\033[32m\n[1]Nome\n[2]Descricao\n[3]Custo Do Produto\n[4]Comissão\n[5]Custo Fixo\n[6]Impostos\n[7]Rentabilidade\n[0]Voltar\033[0m")
                codigo_campos=input("\033[47m\033[30mDigite o Campo Desejado: \033[0m")

                while codigo_campos not in ['1', '2','3','4','5','6','7','0']:#Verificação de entrada
                    print("\t\033[41mERRO\033[0m\n")
                    codigo_campos=input("\033[47m\033[30mDigite o Campo Desejado: \033[0m")

                if codigo_campos=='1':
                    Campo_Nome=input("Pra qual nome voçê deseja alterar: ")
                    codigo=int(input("\n\033[47m\033[30mCodigo Do Produto: \033[0m"))
                    cursor.execute(f"UPDATE Proodutos SET Nome = '{Campo_Nome}' WHERE codigo = {codigo}")
                    cursor.execute("commit")
       
                elif codigo_campos =='2':
                    Campo_Descriçao=input("Descrição Desejada: ")
                    codigo=int(input("\n\033[47m\033[30mCodigo Do Produto: \033[0m"))
                    cursor.execute(f"UPDATE Proodutos SET Descricao = '{Campo_Descriçao}' WHERE codigo = {codigo}")
                    cursor.execute("commit")

                elif codigo_campos =='3':
                    Campo_CustoP=float(input("Custo do produto desejado: "))
                    codigo=int(input("\n\033[47m\033[30mCodigo Do Produto: \033[0m"))
                    cursor.execute(f"UPDATE Proodutos SET Custo = '{Campo_CustoP}' WHERE codigo = {codigo}")
                    cursor.execute("commit")
             
                elif codigo_campos =='4':
                    Campo_Comissão=float(input("Comição Desejada: "))
                    codigo=int(input("\n\033[47m\033[30mCodigo Do Produto: \033[0m"))
                    cursor.execute(f"UPDATE Proodutos SET Comissao = '{Campo_Comissão}' WHERE codigo = {codigo}")
                    cursor.execute("commit")
         
                elif codigo_campos =='5':
                    Campo_CustoF=float(input("Custo Fixo Desejado: "))
                    codigo=int(input("\n\033[47m\033[30mCodigo Do Produto: \033[0m"))
                    cursor.execute(f"UPDATE Proodutos SET Fixo = '{Campo_CustoF}' WHERE codigo = {codigo}")
                    cursor.execute("commit")
             
                elif codigo_campos =='6':
                    Campo_Imposto=float(input("Impostos Desejado: "))
                    codigo=int(input("\n\033[47m\033[30mCodigo Do Produto: \033[0m"))
                    cursor.execute(f"UPDATE Proodutos SET Impostos = '{Campo_Imposto}' WHERE codigo = {codigo}")
                    cursor.execute("commit")
           
                elif codigo_campos =='7':
                    Campo_Rentabilidae=float(input("Rentabilidade Desejada: "))
                    codigo=int(input("\n\033[47m\033[30mCodigo Do Produto: \033[0m"))
                    cursor.execute(f"UPDATE Proodutos SET Rentabilidade = '{Campo_Rentabilidae}' WHERE codigo = {codigo}")
                    cursor.execute("commit")
         
                elif codigo_campos =='0' :
                    num_tela=0#Condição pra volta pra tela inicial

            if codigo_campos>'0' and codigo_campos<'8': 
                    print("_"*55)
                    print("\t   \033[42mAlteração Bem Sucedida\033[0m")
                    
                    print("-"*55)   
                    print("\033[32m[1]Editar Outro Pedido\033[0m\n[0]Voltar")
                    confirmar_editar=input("\033[47m\033[30mOpção Desejada: \033[0m")

                    if confirmar_editar=='1':
                     num_tela=3#Condição ir pro setor de edição
                    else:
                     num_tela=0#Condição pra volta pra tela inicial
        
        
     if num_tela == 4 :
        print("\n")
        print("_"*55)
        print("\t\t   Excluir Produto")
        print("-"*55)

        if num_tela==4 and contador==0:#vai entra nesse loop se a variavel contador for 0,Isso significar q n vizualizou primeiro a tabela
            print("\n\t\t\t\033[42mATENÇÃO!!!\033[0m\n\n")
            print("Antes De voçê Excluir Dados Da Tabela Sujerimos Pesquisar Primeiro.\n")
            print("\033[31m[1]Continuar\033[0m\n\033[32m[2]Visualizar\033[0m\n[0]Voltar")
            Verificar_Dados=int(input("\033[47m\033[30mOpção Desejada: \033[0m"))

            while Verificar_Dados not in [1, 2,0]:#Verificação de entrada
                print("\n\t\033[41mERRO\033[0m\n")
                Verificar_Dados=int(input("\033[47m\033[30mOpção Desejada: \033[0m"))
             
            if Verificar_Dados==1:
                contador=1
            elif Verificar_Dados==2:
                num_tela=1
        if num_tela==4 and contador>=1:
                    print("\nDigite o Codigo do Produto para Realizar Procedimento\n")
                    codigo_excluir=int(input("\n\033[47m\033[30mDigite o codigo: \033[0m"))

                    cursor.execute(f"DELETE FROM Proodutos WHERE codigo = {codigo_excluir}")
                    cursor.execute("commit")
                    if codigo_excluir>=0:
                        print("_"*55)
                        print("\t   \033[42mDeletado Com Susesso\033[0m")
                        print("-"*55) 
                        print("\033[32m[1]Deletar Outro Produto\033[0m\n[0]Voltar")
                        confirmar_excluir=input("\033[47m\033[30mOpção Desejada: \033[0m")
                        while confirmar_excluir not in ['1','0']:#Verificação de entrada
                            print("\n\t\033[41mERRO\033[0m\n")
                            confirmar_excluir=input("\033[47m\033[30mOpção Desejada: \033[0m")
                        if confirmar_excluir =='1':
                            
                            contador=contador+1
                        else:
                            
                            num_tela=0#Condição pra volta pra tela inicial
            
        if num_tela==4 and contador==1:#vai entra nesse loop se a variavel contador for 1,Isso significar q vizualizou primeiro a tabela
            print("\n\t\t\033[42mATENÇÃO!!!\033[0m\n\n")
            print("Voçê Deseja Mesmo Excluir Dados Da Tabela?\n\033[32m[1]SIM\033[0m\n\033[31m[2]NÃO\033[0m")
            Confirmar_Excluir=input("\n\033[47m\033[30mOpção Desejada:\033[0m")

            while Confirmar_Excluir not in ['1', '2','0']:#Verificação de entrada
                print("\n\t\033[41mERRO\033[0m\n")
                Confirmar_Excluir=input("\n\033[47m\033[30mtOpção Desejada:\033[0m")

            if Confirmar_Excluir =='1':
                print("\nDigite o Codigo do Produto para Realizar Procedimento\n")
                codigo_excluir=int(input("\n\033[47m\033[30mDigite o Codigo:\033[0m"))

                cursor.execute(f"DELETE FROM Proodutos WHERE codigo = {codigo_excluir}")
                cursor.execute("commit")
                print("_"*55)
                print("\t   \033[42mDeletado Com Susesso\033[0m")
                print("-"*55)
                num_tela==0#Condição pra volta pra tela inicial
            else:
                num_tela=0#Condição pra volta pra tela inicial

     if num_tela==5:       
        
        if BDC==1:
            cursor.execute("SELECT * FROM proodutos")
        if BDC==2:
            print("\033[31m[1] Excluir\033[0m \n\033[33m[2] Editar\033[0m\n[3] Vizualizar Calculo\n[0] Sair")
            contador=1
            num=int(input("\033[47m\033[30mOpção Desejada: \033[0m"))
            if num==1:
                num_tela=4
            if num==2:
                num_tela=3
            if num==3:
                num_tela=1
            if num==0:
                num_tela=0
        for produto in cursor:
    
            codigo = produto[0]
            nome_produto = produto[1]
            descricao_produto = produto[2]
            CP = produto[3]
            CF = produto[4]
            CV = produto[5]
            IV = produto[6]
            ML = produto[7]
            if BDC==1:
                print("\t\t\t","_" * 55)
                print("\t\t\t\t\t\033[32mInformações do Produto\033[0m")
                print("\t\t\t","-" * 55)
                print("\n\033[47m\033[30mCódigo\tNome\tDescrição\tCusto do Produto\tCusto Fixo\tComissão\tImpostos\tRentabilidade\033[0m")
                print("\033[32m_\033[0m" * 120)
                BDC=2
            
            print(f"\033[47m\033[30m{codigo}\033[0m\t{nome_produto}\t{descricao_produto}\t\t\t{CP}\t\t   {CF}\t\t   {CV}\t\t   {IV}\t\t     {ML}")
            print("\033[32m-\033[0m" * 120)
cursor.close()
connection.close()
# Programa para o Calculo do Preço de Venda
#
#
#Conexão Oracle 
import oracledb
connection = oracledb.connect(
    user = "BD150224225",
    password = "Yzumv3",
    dsn = "172.16.12.14/xe"
)
print('Conectado')
cursor = connection.cursor()
#
#Inicio do Programas
def telaMenu():

    print('_'*55)
    print('Programa Controle de Estoque')
    print('-'*55)

    print ("[1] Visualizar Produto \n[2]Cadastrar Produto \n[3] Editar Produto Cadastrado \n[4] Apagar Produto")

    num_tela = int ( input (" Escolha a Opção Desejada: "))

    return num_tela

def buscarProdutos():

    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchone()
    tabela_produtos = {}
    lista_produtos = []

    while produtos is not None:

        codigo_produto= produtos[0]
        lista_produtos = produtos[1:]

        tabela_produtos[codigo_produto] = lista_produtos

        produtos = cursor.fetchone()

    for codigo, produto in tabela_produtos.items():
        codigo_produto = codigo
        nome_produto = produto[0]
        descricao_produto = produto[1]
        CP = produto[2]
        CF = produto[3]
        CV = produto[4]
        IV = produto[5]
        ML = produto[6]
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
        #
        #Tabela
        print("-" * 55)
        print(f"Codigo do Produto:  {codigo_produto}")
        print("-" * 55)
        print(f"{nome_produto:^50}")
        print(f"{descricao_produto:^50}")
        print("-" * 55)
        print(f"{'Descrição':<20}{'Valor':>15}{'%':>15}")
        print("-" * 55)
        print(f"{'Preço de venda':<20}R${PV:>15.2f}{PV1:>15.2f} %")
        print("-" * 55)
        print(f"{'Preço do produto':<20}R${CP:>15.2f}{CPP:>14.1f} %")
        print("-" * 55)
        print(f"{'RECEITA BRUTA':<20}R${RC:>15.2f}{RC1:>15.2f} %")
        print("-" * 55)
        print(f"{'CUSTO FIXO':<20}R${CF1:>15.2f}{CF:>15.2f} %")
        print("-" * 55)
        print(f"{'COMISSÃO DE VENDAS':<20}R${CV1:>15.2f}{CV:>15.2f} %")
        print("-" * 55)
        print(f"{'IMPOSTOS':<20}R${IV1:>15.2f}{IV:>15.2f} %")
        print("-" * 55)
        print(f"{'OUTROS CUSTOS':<20}R${OCP:>15.2f}{OC:>15.2f} %")
        print("-" * 55)
        print(f"{'RENTABILIDADE':<20}R${RENT1:>15.2f}{ML:>14.1f} %")
        print("-" * 55 )
        #
        #Tabela de Lucros
        if RENT1 > 20:
            print('\033[34m'+'Lucro: Alto'+ '\033[0m') #34m imprime em cor azul
            print("-" * 55 )
            
        elif RENT1 >= 10 and RENT1 <= 20:
            print('\033[32m'+'Lucro: Medio'+ '\033[0m ') #32m imprime em cor verde
            print("-" * 55 )
            
        elif RENT1 > 0 and RENT1 < 10:
            print('\033[33m'+'Lucro: Baixo'+ '\033[0m') #33m imprime em cor amarela
        elif RENT1 == 0:
            print('Lucro: Em Equilibrio'+ '\033[0m')
            print("-" * 55 )
            
        else:
            print('\033[31m'+'Em Prejuizo'+ '\033[0m') #31m imprime em cor vermelha
            print("-" * 55 )

def cadastroProdutos():

    print ("Cadastro de Produto")
    nome_cadastro =  input ("Nome do Produto: ")
    descricao_cadastro =  input ( "Descrição do Produto: ")
    codigo_cadastro = int (input("Cadastre o Código Para o Produto: "))
    custo_cadastro = float ( input ( "Custo do Produto: "))
    comissao_cadastro =  float ( input ("Qual a Taxa de Comissão de Vendas: "))
    fixo_cadastro = float ( input (" Qual a Taxa de Custo Fixo: "))
    impostos_cadastro =  float ( input ("Qual a Taxa de Impostos: "))
    rentabilidade_cadastro = float ( input ("Rentabilidade Esperada: "))

    cursor.execute(f'''INSERT INTO PRODUTOS VALUES({codigo_cadastro},'{nome_cadastro}','{descricao_cadastro}',
            {custo_cadastro},{fixo_cadastro},{comissao_cadastro},{impostos_cadastro},{rentabilidade_cadastro})'''
            )
    
    print("-"*55)
    print ("\t\tReveja as Informações")
    print(f'\t{nome_cadastro :^50},\n{descricao_cadastro:^50}')
    print("-"*55)

    print(f"Preço de Aquisição\t\tR${custo_cadastro :.1f}")
    print(f"Custo Fixo       \t\t{fixo_cadastro} %")
    print(f"Comissão de Vendas\t\t{comissao_cadastro} %")
    print(f"Impostos          \t\t{impostos_cadastro} %")
    print(f"Rentabilidade     \t\t{rentabilidade_cadastro} %")

    print("Deseja Confirmar as Opções ?")
    print("[SIM] Confirmar \n[NÃO] Cancelar")
    tela_cadastro = input ("Opção Desejada: ")
    tela_cadastro.lower()
    
    if tela_cadastro == 'sim':
        cursor.execute("commit") #Confirma o Cadastro e Registra os Dados no Banco de Dados
        print("Cadastro Concluido.")
        print("[1] Cadastrar Outro Produto \n [2]Sair do Cadastro de Produto")
        
        opcao_cadastro = int ( input ("Opção Desejada: "))
        if opcao_cadastro == 1 :
            cadastroProdutos()

        elif opcao_cadastro == 2:
            num_tela = telaMenu(num_tela)
  
        else:
            print("Opção Digitada Incorreta, Digite uma Opção Fornecida")
            print("[1] Cadastrar Outro Produto \n [2]Sair do Cadastro de Produto")

    elif tela_cadastro == 'nao' or tela_cadastro == 'não':
        print("[1] Recomeçar Cadastro \n[2] Sair do Cadastro de Produto")
        opcao_cadastro = int ( input ("Opção Desejada: "))

        if opcao_cadastro == 1 :
            cadastroProdutos()

        elif opcao_cadastro == 2:
            num_tela = telaMenu(num_tela)
  
        else:
            print("Opção Digitada Incorreta, Digite uma Opção Fornecida")
            print("[1] Recomeçar Cadastro \n[2] Sair do Cadastro de Produto")       

    else:
        print("Opção Digitada Incorreta, Por Favor escolha entre [SIM] ou [NÃO]")
        tela_cadastro = input ("Opção Desejada: ")         

def editarProdutos():

    print("\n\t\t\t\033[42mATENÇÃO!!!\033[0m\n\n")
    print("Antes de Editar os Dados do Produto, Sugerimos Pesquisar as Informações do Produto.\n")
    print("\033[32m[1]Visualizar\033[0m\n\033[31m[2]Continuar\033[0m\n[0]Voltar")
    Verificar_Dados=int(input("\033[47m\033[30mOpção Desejada: \033[0m"))

    if Verificar_Dados != 1 and Verificar_Dados != 2 and Verificar_Dados != 3:#Verificação de entrada
        print("\t\033[41mERRO\033[0m\n")
        Verificar_Dados=int(input("\033[47m\033[30mOpção Desejada: \033[0m"))

    elif Verificar_Dados ==0:#Verificar dados ==0 volta para tela inicial do programa
        telaMenu()

    elif Verificar_Dados==1:#Verificar dados ==1 volta para tela de pesquisa do programa

        tabela_produtos = buscarProdutos()
        editarProdutos()

    elif Verificar_Dados == 2:
        print("\033[32m\n[1]Nome\n[2]Descricao\n[3]Custo Do Produto\n[4]Comissão\n[5]Custo Fixo\n[6]Impostos\n[7]Rentabilidade\n[0]Voltar\033[0m")
        opcao_editar =input("\033[47m\033[30mDigite o Campo Desejado: \033[0m")
        codigo_produto=int(input("\n\033[47m\033[30mCodigo Do Produto: \033[0m"))

        if opcao_editar == '1':
            Campo_Nome=input("Pra qual nome voçê deseja alterar: ")
            cursor.execute(f"UPDATE Produtos SET nome_produto = '{Campo_Nome}' WHERE codigo_produto = {codigo_produto}")
            cursor.execute("commit")

        elif opcao_editar =='2':
            Campo_Descriçao=input("Descrição Desejada: ")
            cursor.execute(f"UPDATE Produtos SET descricao_produto = '{Campo_Descriçao}' WHERE codigo_produto = {codigo_produto}")
            cursor.execute("commit")

        elif opcao_editar =='3':
            Campo_CustoP=float(input("Custo do produto desejado: "))

            cursor.execute(f"UPDATE Produtos SET CP = '{Campo_CustoP}' WHERE codigo_produto = {codigo_produto}")
            cursor.execute("commit")
        
        elif opcao_editar =='4':
            Campo_Comissão=float(input("Comição Desejada: "))

            cursor.execute(f"UPDATE Produtos SET CV = '{Campo_Comissão}' WHERE codigo_produto = {codigo_produto}")
            cursor.execute("commit")
    
        elif opcao_editar =='5':
            Campo_CustoF=float(input("Custo Fixo Desejado: "))
            cursor.execute(f"UPDATE Produtos SET CF = '{Campo_CustoF}' WHERE codigo_produto = {codigo_produto}")
            cursor.execute("commit")
        
        elif opcao_editar =='6':
            Campo_Imposto=float(input("Impostos Desejado: "))
            cursor.execute(f"UPDATE Produtos SET IV = '{Campo_Imposto}' WHERE codigo_produto = {codigo_produto}")
            cursor.execute("commit")
    
        elif opcao_editar =='7':
            campoRentabilidade=float(input("Rentabilidade Desejada: "))
            cursor.execute(f"UPDATE Produtos SET ML = '{campoRentabilidade}' WHERE codigo_produto = {codigo_produto}")
            cursor.execute("commit")


def apagarProdutos():

    print("\n\t\t\033[42mATENÇÃO!!!\033[0m\n\n")
    print("Voçê Deseja Mesmo Excluir Dados Da Tabela?\n\033[32m[1]SIM\033[0m\n\033[31m[2]NÃO\033[0m")
    tela_excluir=input("\n\033[47m\033[30mOpção Desejada:\033[0m")

    while tela_excluir not in ['1', '2','0']:#Verificação de entrada
        print("\n\t\033[41mERRO\033[0m\n")
        tela_excluir=input("\n\033[47m\033[30mtOpção Desejada:\033[0m")

    if tela_excluir =='1':
        print("\nDigite o Codigo do Produto para Realizar Procedimento\n")
        codigo_excluir=int(input("\n\033[47m\033[30mDigite o Codigo:\033[0m"))
        cursor.execute(f"DELETE FROM Produtos WHERE codigo_produto = {codigo_excluir}")
        cursor.execute("commit")

        print("_"*55)
        print("\t   \033[42mDeletado Com Susesso\033[0m")
        print("-"*55)
        print("\033[32m[1]Deletar Outro Produto\033[0m\n[2]Voltar")
        tela_excluir = input("\033[47m\033[30mOpção Desejada: \033[0m")

    elif tela_excluir == 2:
        num_tela = telaMenu(num_tela)
        
num_tela = telaMenu()
while num_tela != 0:

    if num_tela == 1:
        buscarProdutos()
        num_tela = telaMenu()

    elif num_tela == 2: 
        cadastroProdutos()
        num_tela = telaMenu()

    elif num_tela == 3:
        buscarProdutos()
        editarProdutos()
        num_tela = telaMenu()

    elif num_tela == 4:
        apagarProdutos()
        num_tela = telaMenu()
        
cursor.close()
connection.close()
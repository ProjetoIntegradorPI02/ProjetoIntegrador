
# Programa para o Calculo do Preço de Venda
import oracledb
#
connection = oracledb.connect(
    user = "BD150224225",
    password = "Yzumv3",
    dsn = "172.16.12.14/xe"
)
print('Conectado')

cursor = connection.cursor()

#Inicio do Programas
print('_'*55)
print('Programa Controle de Estoque')
print('- \n'*55)

print ("[1] Visualizar Produto \n[2]Cadastrar Produto \n[3] Editar Produto Cadastrado \n[4] Apagar Produto")

num_tela = int ( input (" Escolha a Opção Desejada: "))

while num_tela != 0:

    if num_tela == 1:

        #Informaçoes do Produto
        codigo_produto= int (input('Digite o Código do Produto: '))

        tabela_produtos = {}

        cursor.execute(f"SELECT * FROM produtos WHERE codigo_produto = {codigo_produto}")
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
        print("-" * 55)
        
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

        print("[1] Visualizar Outro Produto \n[2] Voltar ao Menu")

        #o comando '\033[0m' redefine a cor do terminal para o padrão após o termino do  print'''

    #cadastro de produtos
    elif num_tela == 2: 

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
        print(f'\t{nome_cadastro},{descricao_cadastro}')
        print("-"*55)

        print(f"Preço de Aquisição\t\tR${custo_cadastro :.1f}")
        print(f"Custo Fixo       \t\t{fixo_cadastro} %")
        print(f"Comissão de Vendas\t\t{comissao_cadastro} %")
        print(f"Impostos          \t\t{impostos_cadastro} %")
        print(f"Rentabilidade     \t\t{rentabilidade_cadastro} %")

        print("Deseja Confirmar as Opções ?")

        print("[SIM] Para Confirmar \n[NÃO] Para Cancelar")

        opcao_cadastro = input ("Opção Desejada: ")

        if opcao_cadastro == 'Sim' or opcao_cadastro == 'SIM' or opcao_cadastro == 'sim':

            cursor.execute("commit") #Confirma o Cadastro e Registra os Dados no Banco de Dados

            print("Cadastro Concluido.")
            print("[1] Cadastrar Outro Produto \n [2]Sair do Cadastro de Produto")
            
            num_tela = int ( input (" Escolha a Opção Desejada: "))
             

        elif opcao_cadastro == 'Nao' or opcao_cadastro == 'NAO' or opcao_cadastro == 'Não' or opcao_cadastro == 'NÃO'or opcao_cadastro =='nao':
            print("[1] Recomeçar Cadastro \n[2] Sair do Cadastro de Produto")

            num_tela = int ( input (" Escolha a Opção Desejada: "))

            if num_tela != 1 or num_tela != 2:
                print("ERRO")
                num_tela = int ( input ("Opção Desejada: "))
        else:
            print("Opção Digitada Incorreta, Por Favor escolha entre [SIM] ou [NÃO]")
            opcao_cadastro = input ("Opção Desejada: ")



    elif num_tela == 3:
        print("Digite o Codigo do Produto para Realizar as Alterações")
        
        


print ("[1] Visualizar Produto \n[2]Cadastrar Produto \n[3] Editar Produto Cadastrado \n[4] Apagar Produto")
num_tela = int ( input (" Escolha a Opção Desejada: "))


cursor.close()
connection.close()
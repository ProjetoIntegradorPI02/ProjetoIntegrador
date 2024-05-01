
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
print('_'*50)
print('Programa Controle de Estoque')
print('-'*50)

print ("[1] Abrir Menu de Produtos\n[2] Cadastrar Produtos\n[3] Editar Produtos Cadastrados")

num_tela = int ( input (" Escolha a Opção Desejada: "))

while num_tela != 0:

    if num_tela == 1:
        print('''Escolha a Opção Desejada:
              
    [1] Visualizar Produto 
    [2] Escolher os Produtos por Categoria
    [3] Visualizar Todos Produtos''' )
        
        opcao_tela = int ( input (" Escolha a Opção Desejada: "))

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
        
        print("-"*50)
        print ("\t\tReveja as Informações")
        print(f'\t{nome_cadastro},{descricao_cadastro}')
        print("-"*50)

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

#Informaçoes do Produto
codigo_produto= int (input('Digite o Código do Produto: '))

cursor.execute(f"SELECT CP FROM produtos WHERE codigo_produto = {codigo_produto}") 
CP = cursor.fetchone()[0]
#
cursor.execute(f"SELECT CV FROM produtos WHERE codigo_produto = {codigo_produto}")
CV = cursor.fetchone()[0]
#
cursor.execute(f"SELECT CF FROM produtos WHERE codigo_produto = {codigo_produto}")
CF = cursor.fetchone()[0]
#
cursor.execute(f"SELECT IV FROM produtos WHERE codigo_produto = {codigo_produto}")
IV = cursor.fetchone()[0]
#
cursor.execute(f"SELECT ML FROM produtos WHERE codigo_produto = {codigo_produto}")
ML = cursor.fetchone()[0]
#
cursor.execute(f"SELECT nome_produto FROM produtos WHERE codigo_produto = {codigo_produto}")
nome_produto = cursor.fetchone()[0]
#
cursor.execute(f"SELECT descricao_produto FROM produtos WHERE codigo_produto = {codigo_produto}")
descricao_produto = cursor.fetchone()[0]

#Formula Calcluo Preço de Venda
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
print("----------------------------------------------------------------------")
print(f'\t\t\t{nome_produto} {descricao_produto}')
print('----------------------------------------------------------------------')
print(f"Descrição\t\t\t Valor \t\t\t %")
print('----------------------------------------------------------------------')
print(f"Preço de venda\t\t\t R${PV:.2f}\t\t{PV1:.2f} %")
print('----------------------------------------------------------------------')
print(f"Preço do produto\t\t R${CP:.2f}\t\t{CPP :.1f} %")
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
print(f"RENTABILIDADE\t\t\t R${RENT1:.2f}\t\t{ML:.1f} %")
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


#o comando '\033[0m' redefine a cor do terminal para o padrão após o termino do  print'''
cursor.close()
connection.close()
# Programa para o Calculo do Preço de Venda
import oracledb
#
connection = oracledb.connect(
    user = "BD150224438",
    password = "Yxcjw1",
    dsn = "172.16.12.14/xe"
)


print('Conectado')  # Mostra que a conexão foi bem-sucedida
# Obtém um cursor
cursor = connection.cursor()
# Executa a consulta para selecionar todas as linhas da tabela de produtos
cursor.execute("SELECT * FROM proodutos")
a=1
# Itera sobre as linhas e exibe as informações de cada produto
for produto in cursor:
    
    codigo = produto[0]
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
    if a==1:
        print("\t\t\t","_" * 55)
        print("\t\t\t\t\t\033[32mInformações do Produto\033[0m")
        print("\t\t\t","-" * 55)
        print("\n\033[47m\033[30mCódigo\tNome\tDescrição\t\tPV\tCP\tRB\tCF\tCV\tIV\tOC\tML\033[0m")
        print("\033[32m_\033[0m" * 120)
        a=2
     
    
    print(f"\033[47m\033[30m{codigo}\033[0m\t{nome_produto}\t  {descricao_produto}\t    {PV:>15.2f}\t{CP:.2f}\t{RC1:.2f}\t{CF:.2f}\t{CV:.2f}\t{IV:.2f}\t{OC:.2f}\t{ML:.2f}\033[0m")
    print("\033[32m-\033[0m" * 120)

# Fecha a conexão
connection.close()





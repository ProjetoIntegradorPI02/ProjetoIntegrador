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
    if a==1:
        print("\t\t\t","_" * 55)
        print("\t\t\t\t\t\033[32mInformações do Produto\033[0m")
        print("\t\t\t","-" * 55)
        print("\n\033[47m\033[30mCódigo\tNome\tDescrição\tCusto do Produto\tCusto Fixo\tComissão\tImpostos\tRentabilidade\033[0m")
        print("\033[32m_\033[0m" * 120)
        a=2
    
    print(f"\033[47m\033[30m{codigo}\033[0m\t{nome_produto}\t  {descricao_produto}\t\t\t{CP}\t\t   {CF}\t\t   {CV}\t\t   {IV}\t\t     {ML}\033[0m")
    print("\033[32m-\033[0m" * 120)

# Fecha a conexão
connection.close()





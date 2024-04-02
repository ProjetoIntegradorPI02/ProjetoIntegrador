# Programa para o Calculo do Preço de Venda

#Informaçoes do Produto
codigo_produto=     int (input('Digite o Código do Produto: '))
nome_produto =      str ( input ( 'Informe o Nome do Produto: '))
descricao_produto = str ( input ( 'Informe a Descrição do Produto: '))

#Variaveis do Preço de Venda

CP = float ( input ( 'Custo do Produto: '))
CF = float ( input ( 'Custo Fixo: '))
CV = float ( input ( 'Comisão de Vendas: '))
IV = float ( input ( 'Impostos: '))
ML = float ( input ( 'Rentabilidade Esperada: '))

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
OC= CF1+ CV1+ IV1

# %Outros custos
OCP= (OC*PV) / 100

#Rentabilidade
RENT= RC- OC

#% Rentabilidade
RENT1= (RENT/PV) * 100

#Tabela
print("----------------------------------------------------------------------")
print(f'\t\t\t{nome_produto} {descricao_produto}')
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
print(f"RENTABILIDADE\t\t\t R${RENT:.2f}\t\t{RENT1:.2f} %")
print('----------------------------------------------------------------------')

#Tabela de Lucros
if RENT1 > 20:
    print('\033[34m'+'Lucro: Alto'+ '\033[0m') #34m COR AZUl

elif RENT1 >= 10 and RENT1 <= 20:
    print('\033[32m'+'Lucro: Medio'+ '\033[0m') #32m COR VERDE

elif RENT1 > 0 and RENT1 < 10:
    print('\033[33m'+'Lucro: Baixo'+ '\033[0m') #33m COR AMARELA

elif RENT1 == 0:
    print('Lucro: Em Equilibrio'+ '\033[0m')

else:
    print('\033[31m'+'Em Prejuizo'+ '\033[0m') #31m COR VERMELHA

#O '\033[0m' serve para redefinir a cor para o padrão após o print    





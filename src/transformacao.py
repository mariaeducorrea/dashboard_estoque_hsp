import pandas as pd 
import openpyxl 

dados = pd.read_csv("C:/Users/Administrador/Desktop/projetos/dashboard_estoque_hsp/dados/dados.csv")



# 1. Converter data_saida para datetime
dados['data_saida'] = pd.to_datetime(dados['data_saida'], errors='coerce', format='%Y-%m-%d')

# 2. Converter custo_unitario para float com 2 casas decimais
dados['custo_unitario'] = dados['custo_unitario'].astype(float).round(2)

# 3. Converter quantidade para inteiro
dados['quantidade'] = dados['quantidade'].astype(int)

# 4. Exportar para Excel
caminho = 'C:/Users/Administrador/Desktop/projetos/dashboard_estoque_hsp/dados/dados.xlsx' 

with pd.ExcelWriter(caminho) as file:
    dados.to_excel(file, sheet_name='historico saidas', index=False)


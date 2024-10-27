import pandas as pd
import os
import datetime

data = datetime.datetime.now()

# Criando um dataframe vazio com a estrutura final do consolidador.
colunas = [
    'Segmento',
    'País',
    'Produto', 
    'Qtde de Unidades Vendidas',	
    'Preço Unitário', 
    'Valor Total', 
    'Desconto', 
    'Valor Total c/ Desconto', 
    'Custo Total', 
    'Lucro', 
    'Data', 
    'Mês', 
    'Ano'
    ]
consolidado = pd.DataFrame(columns=colunas)

# Buscando o nome dos arquivos que serão consolidados.
arquivos = os.listdir("consolidando_planilhas\\planilhas")


# Realiza a consolidação apenas de arquivos .xlsx 
for excel in arquivos:
    
    if excel.endswith('.xlsx'):
        dados_arquivo = excel.split('-')
        segmento = dados_arquivo[0]
        pais = dados_arquivo[1].replace('.xlsx', '')
    
    
        try:
            df = pd.read_excel(f'consolidando_planilhas\\planilhas\\{excel}')
            df.insert(0, 'Segmento', segmento)
            df.insert(1, 'País', pais)
    
            consolidado = pd.concat([consolidado, df])
        except:
            with open('log_erros.txt', 'a') as arquivo:
                arquivo.write(f'Erro ao tentar consolidar o arquivo {excel}.')
    else:
        with open('log_erros.txt', 'a') as arquivo:
                arquivo.write(f'O arquivo {excel} nãoo é um arquivo excel válido!')
                

# exporta o df consolidado para um arquivo Excel
consolidado.to_excel(f"Report-consolidado-{data.strftime('%d-%m-%y')}.xlsx", 
                     index=False,
                     sheet_name='Report consolidado')

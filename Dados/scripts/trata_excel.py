import os
import pandas as pd

def process_excel(filepath):
    # Carregar o arquivo Excel
    xls = pd.ExcelFile(filepath)

    # Lista para armazenar os dataframes tratados
    dfs_cleaned = []

    # Extrair o nome do estado a partir do nome do arquivo
    state_name = os.path.basename(filepath).split(' - ')[1].split('.')[0]

    # Lista de colunas para substituição e verificação
    cols_to_check = ['Área destinada à colheita (Hectares)', 'Área colhida (Hectares)', 
                     'Quantidade produzida (Toneladas)', 
                     'Rendimento médio da produção (Quilogramas por Hectare)', 
                     'Valor da produção (Mil Reais)']

    # Lista de abas a ignorar
    sheets_to_ignore = ['2019; Total', 'Total', 'Notas']

    # Iterar por todas as abas do arquivo, exceto as abas ignoradas
    for sheet_name in [sheet for sheet in xls.sheet_names if sheet not in sheets_to_ignore]:
        # Extrair ano e produto do nome da aba usando o separador ";"
        year, product = sheet_name.split('; ')
        
        # Ler o conteúdo da aba começando da linha 5
        df = pd.read_excel(xls, sheet_name=sheet_name, skiprows=4)
        
        # Filtrar as linhas da coluna A que começam com seis espaços e remover os espaços à esquerda e à direita
        df = df[df.iloc[:, 0].str.startswith("      ")]
        df.iloc[:, 0] = df.iloc[:, 0].str.strip()
        
        # Substituir "..", "..." e "-" por "0" nas colunas especificadas
        df[cols_to_check] = df[cols_to_check].replace(["..", "...", "-"], 0)

        # Filtrar linhas em que todas as colunas especificadas não sejam 0
        df = df[~(df[cols_to_check].astype(int).sum(axis=1) == 0)]

        # Adicionar colunas Estado, Ano e Produto
        df['Estado'] = state_name
        df['Ano'] = year
        df['Produto'] = product.strip()
        
        # Adicionar o dataframe tratado à lista
        dfs_cleaned.append(df)

    # Concatenar todos os dataframes tratados em um único dataframe
    final_df = pd.concat(dfs_cleaned, ignore_index=True)
    
    # Renomear a coluna A para "Município"
    final_df.rename(columns={final_df.columns[0]: 'Município'}, inplace=True)
    
    return final_df

def process_all_files_in_directory(directory, output_filepath):
    all_dfs = []

    # Iterar sobre todos os arquivos Excel na pasta especificada
    for filename in os.listdir(directory):
        if filename.endswith(".xlsx") and not filename.startswith("~$"):  # Evitar arquivos temporários
            file_path = os.path.join(directory, filename)
            all_dfs.append(process_excel(file_path))

    # Combinar todos os dataframes em um único dataframe
    final_combined_df = pd.concat(all_dfs, ignore_index=True)
    
    # Salvar o dataframe combinado em um arquivo Excel final
    final_combined_df.to_excel(output_filepath, index=False)

# Uso do script
# directory = 'path_to_your_directory'  # Substitua pelo caminho da sua pasta
# output_filepath = 'final_combined_file.xlsx'
# process_all_files_in_directory(directory, output_filepath)

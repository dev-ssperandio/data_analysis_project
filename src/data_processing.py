import pandas as pd


# Funções para ler os principais tipos de arquivo
def read_csv(filepath):
    """Realiza a leitura de arquivo CSV e retorna um DataFrame"""
    df_csv = pd.read_csv(filepath)
    return df_csv

def read_excel(filepath):
    """Realiza a leitura de arquivo Excel e retorna um DataFrame"""
    df_excel = pd.read_excel(filepath)
    return df_excel

def read_json(filepath):
    """Realiza a leitura de arquivo Json e retorna um DataFrame"""
    df_json = pd.read_json(filepath)
    return df_json
    

# Selecionando dados com loc e iloc
def select_data_loc(df, rows, columns):
    """Selecionando dados com loc"""
    return df.loc[rows, columns]

def select_data_iloc(df, index_rows, index_columns):
    """Selecionando dados com iloc"""
    return df.iloc[index_rows, index_columns]    
    

if __name__ == "__main__":
    # Rodando 'read_csv'
    df = read_csv('data/raw/customers-100.csv')
    print(df)

    # Rodando 'read_excel'
    df = read_excel('data/raw/Employee-Management-Sample-Data.xlsx')
    print(df)

    # Rodando 'read_json'
    df = read_json('data/raw/estados-brasileiros.json')
    print(df)

    # loc e iloc
    #subset_loc = select_data_loc(df, 5,['coluna1', 'coluna2'])

    

import pytest
import pandas as pd
from src.data_processing import read_csv, read_excel, read_json


def test_read_csv():
    """Teste da função 'read_csv()'"""
    # Cria um DataFrame de exemplo
    data = {'Coluna 1': [1, 2, 3], 'Coluna 2': [4, 5, 6]}
    df_expected = pd.DataFrame(data)

    # Salva 'df_expected' como CSV
    df_expected.to_csv('./data/raw/teste_exemplo.csv', index=False)

    # Lê o CSV utilizando a função read_csv
    df_atual = read_csv('./data/raw/teste_exemplo.csv')

    # Verifica se os DataFrames são iguais
    pd.testing.assert_frame_equal(df_expected, df_atual)

def test_read_excel():
    data = {'Coluna 1': [1, 2, 3], 'Coluna 2': [4, 5, 6]}
    df_expected = pd.DataFrame(data)

    df_expected.to_excel('./data/raw/teste_excel_exemplo.xlsx', index=False)

    df_atual = read_excel('./data/raw/teste_excel_exemplo.xlsx')
    
    pd.testing.assert_frame_equal(df_expected, df_atual)

def test_read_json():
    data = {'Coluna 1': [1, 2, 3], 'Coluna 2': [4, 5, 6]}
    df_expected = pd.DataFrame(data)

    df_expected.to_json('./data/raw/teste_json_exemplo.xlsx', index=False)

    df_atual = read_json('./data/raw/teste_json_exemplo.xlsx')
    
    pd.testing.assert_frame_equal(df_expected, df_atual)

import pandas as pd
import pytest
from application.LeakSeekerModel.pre_processing.PreProcessing import PreProcessing
from application.LeakSeekerModel.pipeline.PipeLineHandler import PipeLineHandler
import sys
import os

# Adiciona o caminho do diretório à variável de sistema para o correto import dos módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

@pytest.fixture
def sample_data():
    # Simula um arquivo CSV de dados
    data = {
        'MATRICULA': [1, 2],
        'REFERENCIA': ['2023-01', '2023-02'],
        'CATEGORIA': ['COMERCIAL', 'RESIDENCIAL'],
        'COD_LATITUDE': [10.0, 20.0],
        'COD_LONGITUDE': [30.0, 40.0],
        'VOLUME_ESTIMADO': [100, 200],
        'DSC_OCORRENCIA': ['NORMAL', 'NORMAL']
    }
    df = pd.DataFrame(data)
    df.to_csv('sample_data.csv', index=False)
    return 'sample_data.csv'  # retorna o caminho do CSV simulado

@pytest.fixture
def sample_fraudes():
    # Simula um arquivo CSV de fraudes
    fraudes = {
        'MATRICULA': [1],
        'DESCRICAO': ['FRAUDE']
    }
    df = pd.DataFrame(fraudes)
    df.to_csv('sample_fraudes.csv', index=False)
    return 'sample_fraudes.csv'  # retorna o caminho do CSV simulado

def test_pipeline(sample_data, sample_fraudes):
    # Processamento dos CSVs
    df_processado = PipeLineHandler.process(sample_data, sample_fraudes)

    # Verifique se o DataFrame processado não está vazio
    assert not df_processado.empty

    # Predição e agregação
    df_predicoes = PipeLineHandler.predict_and_aggregate(df_processado)

    # Verifique se as predições foram adicionadas
    assert 'predictions' in df_predicoes.columns

    # Verifique se o DataFrame de predições não está vazio
    assert not df_predicoes.empty

    # Salvar o resultado em um CSV (opcional para teste)
    PipeLineHandler.save_to_csv(df_predicoes, 'resultado_test.csv')

    # Verifique se o arquivo CSV foi criado
    assert os.path.exists('resultado_test.csv')

    # Limpeza do arquivo gerado após o teste
    os.remove('resultado_test.csv')

if __name__ == "__main__":
    pytest.main()

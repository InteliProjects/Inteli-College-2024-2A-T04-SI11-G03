import pandas as pd
from pandas import DataFrame
from ..inferencia.Model import Model
from ..pre_processing.PreProcessing import PreProcessing

class PipeLineHandler:
    @staticmethod
    def process(csv_data_path: str, csv_fraudes_path: str) -> tuple:
        """
        Lê arquivos CSV e processa os DataFrames de dados e fraudes.
        """
        # Lê os arquivos CSV para DataFrames
        df_data = pd.read_csv(csv_data_path)
        df_fraudes = pd.read_csv(csv_fraudes_path)

        # Passa ambos os DataFrames para o pré-processamento
        pre_processor = PreProcessing(df_data, df_fraudes)

        # Chama o método de pré-processamento que retorna ambos os DataFrames
        df_data_processado, df_fraudes_processado = pre_processor.preprocessamento_unificado()

        return df_data_processado, df_fraudes_processado  # Retorna ambos os DataFrames


    @staticmethod
    def predict_and_aggregate(df: pd.DataFrame) -> pd.DataFrame:
        """
        Faz as predições do modelo e agrega ao DataFrame.
        """
        df_comercial = df[df['CATEGORIA'] == 'COMERCIAL']
        df_residencial = df[df['CATEGORIA'] == 'RESIDENCIAL']

        model_comercial = Model.load_model('models/modelo_lstm_PJ.pkl')
        model_residencial = Model.load_model('models/model_PF.pkl')

        if not df_comercial.empty:
            df_comercial['predictions'] = Model.predict(df_comercial, model_comercial)
        if not df_residencial.empty:
            df_residencial['predictions'] = Model.predict(df_residencial, model_residencial)

        df = pd.concat([df_comercial, df_residencial])

        return df

    @staticmethod
    def save_to_csv(df: pd.DataFrame, filename: str):
        df.to_csv(filename, index=False)

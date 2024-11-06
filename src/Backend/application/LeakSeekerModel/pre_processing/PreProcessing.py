from sklearn.cluster import KMeans
from sklearn.preprocessing import RobustScaler
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import pandas as pd

kmeans_loaded_pj = joblib.load('../models/kmeans_pj.pkl')

class PreProcessing:
    def __init__(self, df: pd.DataFrame, fraudes: pd.DataFrame):
        self.df = df
        self.fraudes = fraudes

    def preprocessamento_unificado(self):
        # Remover colunas comuns
        colunas_comuns = ['Unnamed: 0', 'EMP_CODIGO', 'COD_GRUPO', 'COD_SETOR_COMERCIAL', 'NUM_QUADRA',
                          'COD_ROTA_LEITURA', 'SEQ_RESPONSAVEL', 'ECO_RESIDENCIAL', 'ECO_COMERCIAL',
                          'ECO_INDUSTRIAL', 'ECO_PUBLICA', 'ECO_OUTRAS', 'LTR_ATUAL', 'LTR_COLETADA',
                          'DAT_LEITURA', 'DIAS_LEITURA', 'COD_LEITURA_INF_1', 'COD_LEITURA_INF_2',
                          'COD_LEITURA_INF_3', 'HORA_LEITURA', 'DSC_SIMULTANEA', 'COD_LEITURA_INT', 'EXCECAO']
        self.__remover_colunas(colunas_comuns)

        # Pré-processamento comum
        self.__verificar_duplicatas_referencia()
        self.__remove_rows_with_column_value_greater_than_one(self.df.columns, -10)

        # Condicional para PJ
        df_pj = self.df[self.df["CATEGORIA"].isin(["COMERCIAL", "PUBLICA", "INDUSTRIAL"]) & (self.df['VOLUME_ESTIMADO'] != 0)]
        df_pj = df_pj[df_pj['DSC_OCORRENCIA'].isin(['NORMAL', 'MEDIDOR RETIRADO/FURTADO',
                                                       'LEITURA COLETADA PELO CLIENTE',
                                                       'MEDIDOR NÃO LOCALIZADO', 'IMÓVEL DESOCUPADO'])]

        # Remove outliers para PJ
        df_pj = self.__remove_outliers(df_pj, 'CONS_MEDIDO')

        # Cria variáveis dummy para colunas categóricas
        df_pj = pd.get_dummies(df_pj, columns=['TIPO_LIGACAO', 'DSC_OCORRENCIA', 'STA_TROCA', 'STA_ACEITA_LEITURA'], dtype='int')

        # Processamento das fraudes
        df_fraudes = self.fraudes[['MATRICULA', 'DESCRICAO']].drop_duplicates()
        df_fraudes = pd.get_dummies(df_fraudes, columns=['DESCRICAO'], dtype='int')

        # Merge entre df_pj e fraudes
        df_pj = pd.merge(df_pj, df_fraudes, on='MATRICULA', how='left')
        df_pj = df_pj.dropna(subset=["REFERENCIA", "COD_LATITUDE", "COD_LONGITUDE"])

        # adicionando a feature de clusters
        df_pj['cluster'] = kmeans_loaded_pj.predict(df_pj[['COD_LATITUDE', 'COD_LONGITUDE']])
        df_pj.drop(columns=['COD_LATITUDE', 'COD_LONGITUDE'], inplace=True)
        df_pj = pd.get_dummies(df_pj, columns=['cluster'], dtype=int)

        # Normalização com RobustScaler para PJ
        scaler = RobustScaler()
        df_pj[['CONS_MEDIDO']] = scaler.fit_transform(df_pj[['CONS_MEDIDO']])
        df_pj[['VOLUME_ESTIMADO']] = scaler.fit_transform(df_pj[['VOLUME_ESTIMADO']])

        # Cria tabela pivô para PJ
        pivoted_df_pj = pd.pivot_table(
            df_pj,
            index='MATRICULA',
            columns='REFERENCIA',
            values=['CONS_MEDIDO', 'VOLUME_ESTIMADO'],
            aggfunc='sum'
        )

        pivoted_df_pj.columns = ['_'.join(col).strip() for col in pivoted_df_pj.columns.values]
        pivoted_df_pj = pivoted_df_pj.reset_index()

        # Merge com tipo de ligação
        tipo_ligacao = df_pj[['MATRICULA', 'TIPO_LIGACAO_Consumo Fixo', 'TIPO_LIGACAO_Hidrometrado']].drop_duplicates(subset='MATRICULA', keep='first')
        pivoted_df_pj = pivoted_df_pj.merge(tipo_ligacao, on='MATRICULA', how='left').fillna(0)

        # Merge com descrições de ocorrência
        descricao_ocorrencia = df_pj[['MATRICULA', 'DSC_OCORRENCIA_MEDIDOR NÃO LOCALIZADO',
                                       'DSC_OCORRENCIA_MEDIDOR RETIRADO/FURTADO', 'DSC_OCORRENCIA_NORMAL']].drop_duplicates(subset='MATRICULA', keep='first')
        pivoted_df_pj = pivoted_df_pj.merge(descricao_ocorrencia, on='MATRICULA', how='left').fillna(0)

        # Merge com fraudes
        fraude_ou_não = df_pj[['MATRICULA', 'DESCRICAO_IRREGULARIDADE IDENTIFICADA']].drop_duplicates(subset='MATRICULA', keep='first')
        pivoted_df_pj = pivoted_df_pj.merge(fraude_ou_não, on='MATRICULA', how='left').fillna(0)

        # Merge com clusters
        clusters = df_pj[['MATRICULA'] + [f'cluster_{i}' for i in range(40)]].drop_duplicates(subset='MATRICULA', keep='first')
        pivoted_df_pj = pivoted_df_pj.merge(clusters, on='MATRICULA', how='left').fillna(0)

        # Condicional para PF
        df_pf = self.df[self.df["CATEGORIA"] == "RESIDENCIAL"]
        colunas_remover_pf = ["SUB_CATEGORIA", "STA_TROCA", "STA_ACEITA_LEITURA"]
        df_pf.drop(columns=colunas_remover_pf, inplace=True)

        # Remove outliers para PF
        df_pf = self.__remove_outliers(df_pf, 'CONS_MEDIDO')

    @staticmethod
    def __remove_outliers(df, column_name):
        """Remove outliers based on the IQR method and returns the filtered DataFrame."""
        Q1 = df[column_name].quantile(0.25)
        Q3 = df[column_name].quantile(0.75)
        IQR = Q3 - Q1
        limite_inferior = Q1 - 1.5 * IQR
        limite_superior = Q3 + 1.5 * IQR

        # Filter data to remove outliers
        df_filtrado = df[(df[column_name] >= limite_inferior) & (df[column_name] <= limite_superior)]

        return df_filtrado

    def __remover_colunas(self, colunas):
        colunas_existentes = [col for col in colunas if col in self.df.columns]
        if colunas_existentes:
            self.df.drop(columns=colunas_existentes, inplace=True)
        else:
            print("Nenhuma coluna para remover.")

    def __verificar_duplicatas_referencia(self):
        
        # Verifica e mantém apenas linhas duplicadas com base em 'MATRICULA' e 'REFERENCIA'
        df_duplicados = self.df[self.df.duplicated(subset=['MATRICULA', 'REFERENCIA'], keep=False)]
        self.df = df_duplicados.dropna()

    def __remove_rows_with_column_value_greater_than_one(self, column_names, threshold):
        condition = (self.df[column_names] > threshold).any(axis=1)
        self.df = self.df[~condition]

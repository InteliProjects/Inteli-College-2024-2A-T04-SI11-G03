from pandas import DataFrame
import pickle

class Model:
    @staticmethod
    def load_model(model_path: str):
        with open(model_path, 'rb') as file:
            model = pickle.load(file)
        return model

    @staticmethod
    def predict(df: DataFrame, model) -> DataFrame:
        # Supondo que o modelo tenha um método predict que aceita um DataFrame
        predictions = model.predict(df)
        return predictions

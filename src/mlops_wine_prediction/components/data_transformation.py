import os
from src.mlops_wine_prediction import logger
from sklearn.model_selection import train_test_split
from src.mlops_wine_prediction.entity.config_entity import DataTransformationConfig
import pandas as pd

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config


    def train_test_splitting(self):
        data=pd.read_csv(self.config.data_path)

        # Divide os dados em conjuntos de treinamento e teste. Divisão (0.75, 0.25).
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Dados divididos em conjuntos de treinamento e teste")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
import os
import urllib.request as request
from src.mlops_wine_prediction import logger
import zipfile
from src.mlops_wine_prediction.entity.config_entity import (DataIngestionConfig)


# Componente - Ingestão de Dados

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config
    
    # Baixando o arquivo zip
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} baixado! com as seguintes informações: \n{headers}")
        else:
            logger.info(f"O arquivo já existe")

    def extract_zip_file(self):
        """
        zip_file_path: str
        Extrai o arquivo zip para o diretório de dados
        A função não retorna nada
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

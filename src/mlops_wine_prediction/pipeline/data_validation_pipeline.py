from src.mlops_wine_prediction.config.configuration import ConfigurationManager
from src.mlops_wine_prediction.components.data_validation import DataValiadtion
from src.mlops_wine_prediction import logger

STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_validation(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_columns()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Estágio {STAGE_NAME} iniciado <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.initiate_data_validation()
        logger.info(f">>>>>> Estágio {STAGE_NAME} concluído <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
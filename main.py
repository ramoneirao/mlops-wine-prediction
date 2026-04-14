from src.mlops_wine_prediction import logger
from src.mlops_wine_prediction.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.mlops_wine_prediction.pipeline.data_validation_pipeline import DataValidationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Estágio {STAGE_NAME} iniciado <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>>> Estágio {STAGE_NAME} concluído <<<<<<\n\nx==========x")

    except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>>> Estágio {STAGE_NAME} iniciado <<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.initiate_data_validation()
    logger.info(f">>>>>> Estágio {STAGE_NAME} concluído <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
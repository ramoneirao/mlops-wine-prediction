from src.mlops_wine_prediction import logger
from src.mlops_wine_prediction.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.mlops_wine_prediction.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.mlops_wine_prediction.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.mlops_wine_prediction.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline
from src.mlops_wine_prediction.pipeline.model_evaluation_pipeline import ModelEvaluationTrainingPipeline


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

STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>> Estágio {STAGE_NAME} iniciado <<<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.initiate_data_transformation()
    logger.info(f">>>>>> Estágio {STAGE_NAME} concluído <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer Stage"
try:
    logger.info(f">>>>>> Estágio {STAGE_NAME} iniciado <<<<<<")
    obj = ModelTrainerTrainingPipeline()
    obj.initiate_model_training()
    logger.info(f">>>>>> Estágio {STAGE_NAME} concluído <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation Stage"

try:
    logger.info(f">>>>>> Estágio {STAGE_NAME} iniciado <<<<<<")
    obj = ModelEvaluationTrainingPipeline()
    obj.initiate_model_evaluation()
    logger.info(f">>>>>> Estágio {STAGE_NAME} concluído <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


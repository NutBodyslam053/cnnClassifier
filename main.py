from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_training import ModelTrainingPipeline
from cnnClassifier import logger


STAGE_NAME = ":: DATA INGESTION ::"
try:
    logger.info(f"=============== Stage {STAGE_NAME} Started ===============")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"=============== Stage {STAGE_NAME} Completed ===============\n\n")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = ":: PREPARE BASE MODEL ::"
try:
    logger.info(f"=============== Stage {STAGE_NAME} Started ===============")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f"=============== Stage {STAGE_NAME} Completed ===============\n\n")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = ":: TRAINING ::"
try:
    logger.info(f"=============== Stage {STAGE_NAME} Started ===============")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f"=============== Stage {STAGE_NAME} Completed ===============\n\n")
except Exception as e:
    logger.exception(e)
    raise e
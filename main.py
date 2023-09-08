from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier import logger


STAGE_NAME = ":: DATA INGESTION ::"
try:
    logger.info(f"=============== Stage {STAGE_NAME} Started ===============")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"=============== Stage {STAGE_NAME} Completed ===============\n")
except Exception as e:
    logger.exception(e)
    raise e
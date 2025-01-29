from mlproject import logger
from mlproject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = 'Data Ingestion stage'

try:
    logger.info(f'>>>>>>stage{STAGE_NAME}has started<<<<<<<<<<<<<<')
    obj= DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'>>>>>>stage{STAGE_NAME} completed<<<<<<<<<<\n\nxx=========xxx')
except Exception as e:
    logger.exception(e)
    raise e



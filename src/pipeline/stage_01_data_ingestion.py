from src.config.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion
from src.utils.logger import logger


class DataIngestionTrainingPipeline:

    def __init__(self):
        pass

    def main(self):

        logger.info("=" * 70)
        logger.info("Stage 01 : Data Ingestion Started")

        config = ConfigurationManager()

        ingestion_config = config.get_data_ingestion_config()

        data_ingestion = DataIngestion(ingestion_config)

        data_ingestion.copy_dataset()

        logger.info("Stage 01 : Data Ingestion Completed")

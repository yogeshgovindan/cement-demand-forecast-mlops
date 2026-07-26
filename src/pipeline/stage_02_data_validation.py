from src.config.configuration import ConfigurationManager
from src.components.data_validation import DataValidation
from src.utils.logger import logger


class DataValidationTrainingPipeline:

    def __init__(self):
        pass

    def main(self):

        logger.info("=" * 70)
        logger.info("Stage 02 : Data Validation Started")

        config = ConfigurationManager()

        validation_config = config.get_data_validation_config()

        validation = DataValidation(validation_config)

        validation.validate_dataset()

        logger.info("Stage 02 : Data Validation Completed")

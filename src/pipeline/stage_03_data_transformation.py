from src.config.configuration import ConfigurationManager
from src.components.data_transformation import DataTransformation
from src.utils.logger import logger


class DataTransformationTrainingPipeline:

    def __init__(self):
        pass

    def main(self):

        logger.info("=" * 70)
        logger.info("Stage 03 : Data Transformation Started")

        config = ConfigurationManager()

        transformation_config = config.get_data_transformation_config()

        transformation = DataTransformation(transformation_config)

        transformation.run()

        logger.info("Stage 03 : Data Transformation Completed")

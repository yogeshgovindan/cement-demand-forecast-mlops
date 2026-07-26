from src.config.configuration import ConfigurationManager
from src.components.model_trainer import ModelTrainer
from src.utils.logger import logger


class ModelTrainingPipeline:

    def __init__(self):
        pass

    def main(self):

        logger.info("=" * 70)
        logger.info("Stage 04 : Model Training Started")

        config = ConfigurationManager()

        model_trainer_config = (
            config.get_model_trainer_config()
        )

        model_trainer = ModelTrainer(
            model_trainer_config
        )

        model_trainer.train_model()

        logger.info(
            "Stage 04 : Model Training Completed"
        )

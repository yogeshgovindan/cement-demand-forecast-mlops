from src.config.configuration import ConfigurationManager
from src.components.model_evaluation import ModelEvaluation
from src.utils.logger import logger


class ModelEvaluationPipeline:

    def __init__(self):
        pass

    def main(self):

        logger.info(
            "=" * 70
        )

        logger.info(
            "Stage 05 : Model Evaluation Started"
        )

        config = ConfigurationManager()

        evaluation_config = (
            config.get_model_evaluation_config()
        )

        evaluation = ModelEvaluation(
            evaluation_config
        )

        evaluation.evaluate_model()

        logger.info(
            "Stage 05 : Model Evaluation Completed"
        )

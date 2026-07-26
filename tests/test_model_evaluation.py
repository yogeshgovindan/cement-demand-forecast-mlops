from src.config.configuration import ConfigurationManager
from src.components.model_evaluation import ModelEvaluation


config = ConfigurationManager()


evaluation_config = (
    config.get_model_evaluation_config()
)


evaluation = ModelEvaluation(
    evaluation_config
)


evaluation.evaluate_model()


print(
    "Model evaluation completed"
)

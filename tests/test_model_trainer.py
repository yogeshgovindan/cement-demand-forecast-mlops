from src.config.configuration import ConfigurationManager
from src.components.model_trainer import ModelTrainer


config = ConfigurationManager()


model_config = config.get_model_trainer_config()


trainer = ModelTrainer(
    model_config
)


trainer.train_model()


print("Model training completed")

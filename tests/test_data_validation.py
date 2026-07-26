from src.config.configuration import ConfigurationManager
from src.components.data_validation import DataValidation


config = ConfigurationManager()


validation_config = (
    config.get_data_validation_config()
)


validation = DataValidation(
    validation_config
)


result = validation.validate_dataset()


print(
    "Validation Result:",
    result
)

from src.config.configuration import ConfigurationManager
from src.components.data_transformation import DataTransformation

config = ConfigurationManager()

transformer = DataTransformation(
    config.get_data_transformation_config()
)

df = transformer.load_data()

print(df.shape)

df = transformer.preprocess_data()

print(df.shape)

from src.config.configuration import ConfigurationManager


config = ConfigurationManager()


print("CONFIG")
print(config.get_config())


print("\nPARAMS")
print(config.get_params())


print("\nSCHEMA")
print(config.get_schema())


print("\nDATA INGESTION CONFIG")

ingestion = config.get_data_ingestion_config()

print(ingestion)


print("\nDATA VALIDATION CONFIG")

validation = config.get_data_validation_config()

print(validation)


print("\nDATA TRANSFORMATION CONFIG")

transformation = config.get_data_transformation_config()

print(transformation)

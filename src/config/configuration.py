from pathlib import Path

from src.constants.paths import (
    CONFIG_FILE_PATH,
    PARAMS_FILE_PATH,
    SCHEMA_FILE_PATH,
)


from src.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
    ModelEvaluationConfig,
)

from src.utils.common import (
    create_directories,
    read_yaml,
)


class ConfigurationManager:

    def __init__(self):

        self.config = read_yaml(
            CONFIG_FILE_PATH
        )

        self.params = read_yaml(
            PARAMS_FILE_PATH
        )

        self.schema = read_yaml(
            SCHEMA_FILE_PATH
        )

        create_directories(
            [
                self.config.artifacts_root
            ]
        )

    def get_config(self):

        return self.config

    def get_params(self):

        return self.params

    def get_schema(self):

        return self.schema

    def get_data_ingestion_config(self):

        config = (
            self.config.data_ingestion
        )

        create_directories(
            [
                config.root_dir
            ]
        )

        return DataIngestionConfig(

            root_dir=Path(
                config.root_dir
            ),

            dataset_name=config.dataset_name,

            local_data_file=Path(
                config.local_data_file
            )

        )

    def get_data_validation_config(self):

        config = (
            self.config.data_validation
        )

        create_directories(
            [
                config.root_dir
            ]
        )

        return DataValidationConfig(

            root_dir=Path(
                config.root_dir
            ),

            status_file=Path(
                config.status_file
            )

        )

    def get_data_transformation_config(self):

        config = self.config.data_transformation

        create_directories(
            [config.root_dir]
        )

        return DataTransformationConfig(

            root_dir=Path(config.root_dir),

            input_file=Path(
                self.config.data_ingestion.local_data_file
            ),

            train_file=Path(config.train_file),

            test_file=Path(config.test_file),

            random_state=self.params.random_state,

            test_size=self.params.test_size

        )

    def get_model_trainer_config(self):

        config = self.config.model_trainer

        create_directories(
            [config.root_dir]
        )

        return ModelTrainerConfig(

            root_dir=Path(config.root_dir),

            train_file=Path(config.train_file),

            test_file=Path(config.test_file),

            model_file=Path(config.model_file),

            target_column=self.schema.columns.target_column

        )

    def get_model_evaluation_config(self):

        config = self.config.model_evaluation

        create_directories(
            [config.root_dir]
        )

        return ModelEvaluationConfig(

            root_dir=Path(config.root_dir),

            metric_file_name=Path(
                config.metric_file_name
            ),

            model_path=Path(
                self.config.model_trainer.model_file
            ),

            test_data_path=Path(
                self.config.data_transformation.test_file
            ),

            target_column=self.schema.columns.target_column
        )

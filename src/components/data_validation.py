import os
import sys

import pandas as pd

from src.entity.config_entity import DataValidationConfig
from src.exception.exception import CustomException
from src.utils.logger import logger
from src.config.configuration import ConfigurationManager


class DataValidation:

    def __init__(
        self,
        config: DataValidationConfig
    ):

        self.config = config

        self.schema = (
            ConfigurationManager()
            .get_schema()
        )

    def validate_columns(self, df):

        try:

            logger.info(
                "Column validation started"
            )

            # Remove extra spaces

            df.columns = (
                df.columns
                .str.strip()
            )

            required_columns = (
                self.schema.required_columns
            )

            missing_columns = []

            for column in required_columns:

                if column not in df.columns:

                    missing_columns.append(column)

            if missing_columns:

                return False, missing_columns

            return True, []

        except Exception as e:

            raise CustomException(
                e,
                sys
            )

    def validate_dataset(self):

        try:

            logger.info(
                "Dataset validation started"
            )

            data_file = (
                "artifacts/data_ingestion/data.csv"
            )

            df = pd.read_csv(
                data_file
            )

            validation_status, missing_columns = (
                self.validate_columns(df)
            )

            os.makedirs(
                self.config.root_dir,
                exist_ok=True
            )

            with open(
                self.config.status_file,
                "w"
            ) as file:

                if validation_status:

                    file.write(
                        "Validation Status: True"
                    )

                else:

                    file.write(
                        "Validation Status: False\n"
                    )

                    file.write(
                        f"Missing Columns: {missing_columns}"
                    )

            logger.info(
                "Validation completed successfully"
            )

            return validation_status

        except Exception as e:

            raise CustomException(
                e,
                sys
            )

import os
import shutil
import sys
from pathlib import Path

import kagglehub

from src.entity.config_entity import DataIngestionConfig
from src.utils.logger import logger
from src.exception.exception import CustomException


class DataIngestion:

    def __init__(
        self,
        config: DataIngestionConfig
    ):

        self.config = config

    def download_dataset(self):

        try:

            logger.info(
                "Dataset download started"
            )

            dataset_path = kagglehub.dataset_download(
                self.config.dataset_name
            )

            dataset_path = Path(dataset_path)

            logger.info(
                f"Dataset downloaded at: {dataset_path}"
            )

            logger.info(
                "Files available inside dataset:"
            )

            for file in dataset_path.rglob("*"):

                logger.info(
                    str(file)
                )

            return dataset_path

        except Exception as e:

            logger.exception(
                "Dataset download failed"
            )

            raise CustomException(
                e,
                sys
            )

    def find_dataset_file(
        self,
        dataset_path: Path
    ):

        try:

            logger.info(
                "Searching dataset file"
            )

            supported_extensions = [
                "*.csv",
                "*.xlsx",
                "*.parquet"
            ]

            dataset_files = []

            for extension in supported_extensions:

                dataset_files.extend(
                    dataset_path.rglob(extension)
                )

            if not dataset_files:

                raise FileNotFoundError(
                    "No supported dataset file found "
                    "(.csv/.xlsx/.parquet)"
                )

            # Select first dataset file

            selected_file = dataset_files[0]

            logger.info(
                f"Selected dataset file: {selected_file}"
            )

            return selected_file

        except Exception as e:

            logger.exception(
                "Dataset file detection failed"
            )

            raise CustomException(
                e,
                sys
            )

    def copy_dataset(self):

        try:

            logger.info(
                "Data ingestion process started"
            )

            # Step 1: Download dataset

            downloaded_path = (
                self.download_dataset()
            )

            # Step 2: Find actual data file

            source_file = (
                self.find_dataset_file(
                    downloaded_path
                )
            )

            # Step 3: Destination

            destination_file = (
                self.config.local_data_file
            )

            os.makedirs(
                destination_file.parent,
                exist_ok=True
            )

            # Step 4: Copy file

            shutil.copy(
                source_file,
                destination_file
            )

            logger.info(
                "Dataset copied successfully"
            )

            logger.info(
                f"Final location: {destination_file}"
            )

            return destination_file

        except Exception as e:

            logger.exception(
                "Data ingestion failed"
            )

            raise CustomException(
                e,
                sys
            )

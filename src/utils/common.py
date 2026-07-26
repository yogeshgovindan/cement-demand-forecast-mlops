import sys
import json
import yaml
import joblib
import pandas as pd

from pathlib import Path
from box import ConfigBox

from src.exception.exception import CustomException
from src.utils.logger import logger


# ============================================================
# YAML FUNCTIONS
# ============================================================

def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read a YAML file and return a ConfigBox object.

    Args:
        path_to_yaml (Path):
            Path to YAML file.

    Returns:
        ConfigBox:
            Parsed YAML configuration.
    """

    try:

        with open(path_to_yaml, "r") as yaml_file:

            content = yaml.safe_load(yaml_file)

            logger.info(
                f"YAML loaded successfully: {path_to_yaml}"
            )

            return ConfigBox(content)

    except Exception as e:

        logger.exception(
            "Failed while reading YAML file."
        )

        raise CustomException(e, sys)


# ============================================================
# DIRECTORY FUNCTIONS
# ============================================================

def create_directories(
        path_to_directories: list
) -> None:
    """
    Create directories if they do not already exist.

    Args:
        path_to_directories (list):
            List of directory paths.
    """

    try:

        for path in path_to_directories:

            Path(path).mkdir(
                parents=True,
                exist_ok=True
            )

            logger.info(
                f"Directory created: {path}"
            )

    except Exception as e:

        logger.exception(
            "Failed while creating directories."
        )

        raise CustomException(e, sys)


# ============================================================
# JSON FUNCTIONS
# ============================================================

def save_json(
        path: Path,
        data: dict
) -> None:
    """
    Save dictionary as JSON.
    """

    try:

        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(path, "w") as file:

            json.dump(
                data,
                file,
                indent=4
            )

        logger.info(
            f"JSON saved successfully: {path}"
        )

    except Exception as e:

        logger.exception(
            "Failed while saving JSON."
        )

        raise CustomException(e, sys)


def load_json(
        path: Path
) -> dict:
    """
    Load JSON file.
    """

    try:

        with open(path, "r") as file:

            data = json.load(file)

        logger.info(
            f"JSON loaded successfully: {path}"
        )

        return data

    except Exception as e:

        logger.exception(
            "Failed while loading JSON."
        )

        raise CustomException(e, sys)


# ============================================================
# MODEL FUNCTIONS
# ============================================================

def save_model(
        file_path: Path,
        model
) -> None:
    """
    Save ML model using Joblib.
    """

    try:

        file_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        joblib.dump(
            model,
            file_path
        )

        logger.info(
            f"Model saved successfully: {file_path}"
        )

    except Exception as e:

        logger.exception(
            "Failed while saving model."
        )

        raise CustomException(e, sys)


def load_model(
        file_path: Path
):
    """
    Load ML model.
    """

    try:

        model = joblib.load(
            file_path
        )

        logger.info(
            f"Model loaded successfully: {file_path}"
        )

        return model

    except Exception as e:

        logger.exception(
            "Failed while loading model."
        )

        raise CustomException(e, sys)


# ============================================================
# CSV FUNCTIONS
# ============================================================

def read_csv(
        path: Path
) -> pd.DataFrame:
    """
    Read CSV file.
    """

    try:

        dataframe = pd.read_csv(
            path
        )

        logger.info(
            f"CSV loaded successfully: {path}"
        )

        return dataframe

    except Exception as e:

        logger.exception(
            "Failed while reading CSV."
        )

        raise CustomException(e, sys)


def save_csv(
        path: Path,
        dataframe: pd.DataFrame
) -> None:
    """
    Save DataFrame as CSV.
    """

    try:

        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        dataframe.to_csv(
            path,
            index=False
        )

        logger.info(
            f"CSV saved successfully: {path}"
        )

    except Exception as e:

        logger.exception(
            "Failed while saving CSV."
        )

        raise CustomException(e, sys)


# ============================================================
# FILE SIZE
# ============================================================

def get_size(
        path: Path
) -> str:
    """
    Returns file size in KB.
    """

    size_in_kb = round(
        path.stat().st_size / 1024
    )

    return f"~ {size_in_kb} KB"

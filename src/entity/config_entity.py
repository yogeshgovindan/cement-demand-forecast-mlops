from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    dataset_name: str
    local_data_file: Path


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    status_file: Path


@dataclass(frozen=True)
class DataTransformationConfig:

    root_dir: Path

    input_file: Path

    train_file: Path

    test_file: Path

    random_state: int

    test_size: float


@dataclass(frozen=True)
class ModelTrainerConfig:

    root_dir: Path

    train_file: Path

    test_file: Path

    model_file: Path

    target_column: str


@dataclass(frozen=True)
class ModelEvaluationConfig:

    root_dir: Path

    metric_file_name: Path

    model_path: Path

    test_data_path: Path

    target_column: str

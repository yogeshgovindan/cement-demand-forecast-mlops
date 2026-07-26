from pathlib import Path


CONFIG_FILE_PATH = Path(
    "config/config.yaml"
)


PARAMS_FILE_PATH = Path(
    "config/params.yaml"
)


SCHEMA_FILE_PATH = Path(
    "config/schema.yaml"
)


LOG_DIR = Path(
    "logs"
)


LOG_FILE_PATH = LOG_DIR / "running_logs.log"


DATA_FILE_PATH = Path(
    "artifacts/data_ingestion/data.csv"
)

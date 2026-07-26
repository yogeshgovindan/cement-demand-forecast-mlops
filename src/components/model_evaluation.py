import sys
import json
import joblib
import pandas as pd

from sklearn.metrics import (
    mean_absolute_error,
    root_mean_squared_error,
    r2_score
)

from src.entity.config_entity import ModelEvaluationConfig
from src.exception.exception import CustomException
from src.utils.logger import logger


class ModelEvaluation:

    def __init__(
            self,
            config: ModelEvaluationConfig
    ):

        self.config = config

    def evaluate_model(self):

        try:

            logger.info(
                "Model Evaluation Started"
            )

            # Load trained model

            model = joblib.load(
                self.config.model_path
            )

            # Load test dataset

            test_data = pd.read_csv(
                self.config.test_data_path
            )

            X_test = test_data.drop(
                columns=[
                    self.config.target_column
                ]
            )

            y_test = test_data[
                self.config.target_column
            ]

            # Generate predictions

            predictions = model.predict(
                X_test
            )

            # Calculate metrics

            mae = mean_absolute_error(
                y_test,
                predictions
            )

            rmse = root_mean_squared_error(
                y_test,
                predictions
            )

            r2 = r2_score(
                y_test,
                predictions
            )

            metrics = {

                "MAE": float(mae),

                "RMSE": float(rmse),

                "R2_SCORE": float(r2)

            }

            # Save metrics

            with open(
                self.config.metric_file_name,
                "w"
            ) as file:

                json.dump(
                    metrics,
                    file,
                    indent=4
                )

            logger.info(
                "Model Evaluation Completed"
            )

        except Exception as e:

            raise CustomException(
                e,
                sys
            )

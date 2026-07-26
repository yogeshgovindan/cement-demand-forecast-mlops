import sys
import pandas as pd
import joblib
import mlflow
import mlflow.sklearn

from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import (
    mean_absolute_error,
    root_mean_squared_error,
    r2_score
)

from src.entity.config_entity import ModelTrainerConfig
from src.exception.exception import CustomException
from src.utils.logger import logger


class ModelTrainer:

    def __init__(
            self,
            config: ModelTrainerConfig
    ):

        self.config = config

    def train_model(self):

        try:

            logger.info("=" * 70)
            logger.info("Model Training Started")

            # ---------------------------------
            # Load Data
            # ---------------------------------

            train_df = pd.read_csv(
                self.config.train_file
            )

            test_df = pd.read_csv(
                self.config.test_file
            )

            logger.info(
                f"Train Shape : {train_df.shape}"
            )

            logger.info(
                f"Test Shape : {test_df.shape}"
            )

            # ---------------------------------
            # Split Features and Target
            # ---------------------------------

            X_train = train_df.drop(
                columns=[
                    self.config.target_column
                ]
            )

            y_train = train_df[
                self.config.target_column
            ]

            X_test = test_df.drop(
                columns=[
                    self.config.target_column
                ]
            )

            y_test = test_df[
                self.config.target_column
            ]

            # MLflow schema expects float values

            X_train = X_train.astype(float)

            X_test = X_test.astype(float)

            # ---------------------------------
            # Model Parameters
            # ---------------------------------

            n_estimators = 100

            random_state = 42

            model = RandomForestRegressor(

                n_estimators=n_estimators,

                random_state=random_state

            )

            # ---------------------------------
            # MLflow Configuration
            # ---------------------------------

            mlflow.set_tracking_uri(
                "sqlite:///mlflow.db"
            )

            mlflow.set_registry_uri(
                "sqlite:///mlflow.db"
            )

            mlflow.set_experiment(
                "cement-demand-forecast"
            )

            # ---------------------------------
            # MLflow Run
            # ---------------------------------

            with mlflow.start_run():

                # Train

                model.fit(
                    X_train,
                    y_train
                )

                logger.info(
                    "Model training completed"
                )

                # Prediction

                predictions = model.predict(
                    X_test
                )

                # Metrics

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

                logger.info(
                    f"MAE : {mae}"
                )

                logger.info(
                    f"RMSE : {rmse}"
                )

                logger.info(
                    f"R2 Score : {r2}"
                )

                # ---------------------------------
                # Log Parameters
                # ---------------------------------

                mlflow.log_param(
                    "model",
                    "RandomForestRegressor"
                )

                mlflow.log_param(
                    "n_estimators",
                    n_estimators
                )

                mlflow.log_param(
                    "random_state",
                    random_state
                )

                # ---------------------------------
                # Log Metrics
                # ---------------------------------

                mlflow.log_metric(
                    "MAE",
                    mae
                )

                mlflow.log_metric(
                    "RMSE",
                    rmse
                )

                mlflow.log_metric(
                    "R2_SCORE",
                    r2
                )

                # ---------------------------------
                # Register Model
                # ---------------------------------

                mlflow.sklearn.log_model(

                    sk_model=model,

                    artifact_path="model",

                    registered_model_name="cement_demand_model"

                )

            # ---------------------------------
            # Save Local Model
            # ---------------------------------

            joblib.dump(

                model,

                self.config.model_file

            )

            logger.info(
                f"Model saved at {self.config.model_file}"
            )

            logger.info(
                "Model Training Completed Successfully"
            )

        except Exception as e:

            raise CustomException(
                e,
                sys
            )

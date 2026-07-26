import sys
import pandas as pd

from sklearn.model_selection import train_test_split

from src.entity.config_entity import DataTransformationConfig
from src.exception.exception import CustomException
from src.utils.logger import logger


class DataTransformation:
    """
    Data Transformation Component

    Responsibilities:
    1. Load Dataset
    2. Preprocess Dataset
    3. Feature Engineering
    4. Validate Dataset
    5. Split Dataset
    6. Save Dataset
    """

    def __init__(self, config: DataTransformationConfig):

        self.config = config
        self.df = None

    ###########################################################################
    # Load Dataset
    ###########################################################################

    def load_data(self):
        """
        Load dataset from Data Ingestion output.
        """

        try:

            logger.info("=" * 70)
            logger.info("Loading dataset...")

            self.df = pd.read_csv(
                self.config.input_file
            )

            logger.info(
                f"Dataset Loaded Successfully : {self.df.shape}"
            )

            logger.info(
                f"Dataset Path : {self.config.input_file}"
            )

            return self.df

        except Exception as e:

            raise CustomException(e, sys)

    ###########################################################################
    # Preprocessing
    ###########################################################################

    def preprocess_data(self):
        """
        Generic preprocessing.
        """

        try:

            logger.info("=" * 70)
            logger.info("Starting preprocessing...")

            # Remove spaces from column names

            self.df.columns = self.df.columns.str.strip()

            logger.info("Column names cleaned.")

            ############################################################

            # Remove unnamed columns

            self.df = self.df.loc[
                :,
                ~self.df.columns.str.contains("^Unnamed")
            ].copy()

            logger.info(
                f"Unnamed columns removed : {self.df.shape}"
            )

            ############################################################

            # Remove completely empty rows

            self.df.dropna(
                how="all",
                inplace=True
            )

            logger.info(
                f"Empty rows removed : {self.df.shape}"
            )

            ############################################################

            # Remove duplicate rows

            before = len(self.df)

            self.df.drop_duplicates(
                inplace=True
            )

            after = len(self.df)

            logger.info(
                f"Duplicate rows removed : {before-after}"
            )

            logger.info(
                f"Final Shape : {self.df.shape}"
            )

            return self.df

        except Exception as e:

            raise CustomException(e, sys)

    ###########################################################################
    # Feature Engineering
    ###########################################################################

    def feature_engineering(self):
        """
        Create additional features.
        """

        try:

            logger.info("=" * 70)
            logger.info("Starting feature engineering...")

            ############################################################

            # Convert Month column

            self.df["Month"] = pd.to_datetime(
                self.df["Month"],
                format="%b-%y"
            )

            ############################################################

            # Extract Year

            self.df["year"] = self.df["Month"].dt.year

            ############################################################

            # Extract Month

            self.df["month"] = self.df["Month"].dt.month

            ############################################################

            # Drop original Month column

            self.df.drop(
                columns=["Month"],
                inplace=True
            )

            logger.info(
                f"Feature Engineering Completed : {self.df.shape}"
            )

            return self.df

        except Exception as e:

            raise CustomException(e, sys)

    ###########################################################################
    # Dataset Validation
    ###########################################################################

    def validate_dataset(self):
        """
        Validate transformed dataset.
        """

        try:

            logger.info("=" * 70)
            logger.info("Validating dataset...")

            if self.df.empty:

                raise ValueError(
                    "Dataset is empty."
                )

            if "demand" not in self.df.columns:

                raise ValueError(
                    "Target column 'demand' not found."
                )

            missing_values = self.df.isnull().sum().sum()

            if missing_values > 0:

                raise ValueError(
                    f"Dataset contains {missing_values} missing values."
                )

            logger.info("Dataset validation successful.")

        except Exception as e:

            raise CustomException(e, sys)

    ###########################################################################
    # Train Test Split
    ###########################################################################

    def split_data(self):
        """
        Split dataset into train and test.
        """

        try:

            logger.info("=" * 70)
            logger.info("Splitting dataset...")

            train_df, test_df = train_test_split(

                self.df,

                test_size=self.config.test_size,

                random_state=self.config.random_state

            )

            logger.info(
                f"Train Shape : {train_df.shape}"
            )

            logger.info(
                f"Test Shape : {test_df.shape}"
            )

            return train_df, test_df

        except Exception as e:

            raise CustomException(e, sys)

    ###########################################################################
    # Save Dataset
    ###########################################################################

    def save_data(self, train_df, test_df):
        """
        Save train and test datasets.
        """

        try:

            logger.info("=" * 70)
            logger.info("Saving datasets...")

            train_df.to_csv(
                self.config.train_file,
                index=False
            )

            test_df.to_csv(
                self.config.test_file,
                index=False
            )

            logger.info(
                f"Train Dataset Saved : {self.config.train_file}"
            )

            logger.info(
                f"Test Dataset Saved : {self.config.test_file}"
            )

        except Exception as e:

            raise CustomException(e, sys)

    ###########################################################################
    # Run Complete Pipeline
    ###########################################################################

    def run(self):
        """
        Execute complete data transformation pipeline.
        """

        try:

            self.load_data()

            self.preprocess_data()

            self.feature_engineering()

            self.validate_dataset()

            train_df, test_df = self.split_data()

            self.save_data(
                train_df,
                test_df
            )

            logger.info("=" * 70)
            logger.info("Data Transformation Completed Successfully.")

            return (
                self.config.train_file,
                self.config.test_file
            )

        except Exception as e:

            raise CustomException(e, sys)

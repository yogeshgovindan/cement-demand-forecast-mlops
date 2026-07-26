from pathlib import Path

import pandas as pd

from src.config.configuration import ConfigurationManager
from src.utils.common import load_model


class ModelPredictor:

    def __init__(self):

        config = ConfigurationManager()

        model_path = config.get_prediction_model_path()

        self.model = load_model(
            model_path
        )

    def predict(
            self,
            data: dict
    ) -> float:

        df = pd.DataFrame(
            [data]
        )

        feature_order = [

            "Production",

            "Sales",

            "population",

            "gdp",

            "disbusment",

            "interestrate",

            "year",

            "month"

        ]

        df = df[feature_order]

        df = df.astype(float)

        prediction = self.model.predict(
            df
        )

        return float(
            prediction[0]
        )

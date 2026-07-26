from fastapi import FastAPI

from src.api.schema import CementDemandInput
from src.api.predictor import ModelPredictor


app = FastAPI(
    title="Cement Demand Forecast API",
    version="1.0"
)


model = ModelPredictor()


@app.get("/")
def home():

    return {
        "message": "Cement Demand Prediction API Running"
    }


@app.post("/predict")
def predict(
        request: CementDemandInput
):

    prediction = model.predict(
        request.dict()
    )

    return {

        "predicted_demand": prediction

    }

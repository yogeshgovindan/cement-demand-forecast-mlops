from pydantic import BaseModel


class CementDemandInput(BaseModel):

    Production: float

    Sales: float

    population: float

    gdp: float

    disbusment: float

    interestrate: float

    year: int

    month: int

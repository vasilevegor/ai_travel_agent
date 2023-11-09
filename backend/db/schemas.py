from datetime import date
from pydantic import BaseModel, Field


class AirportSchema(BaseModel):
    name: str = Field(alias="label")
    iata: str = Field(alias="value")

    class Config:
        populate_by_name = True
        from_attributes = True


class FlightPriceOverviewSchema(BaseModel): # Pydantic
    id: int
    flightDate: date
    startingAirport: str
    destinationAirport: str
    # isBasicEconomy: bool
    # isRefundable: bool
    # isNonStop: bool
    segmentsAirlineName: str
    totalFare: int

    class Config:
        from_attributes = True
        
        
class FlightPriceDetailSchema(BaseModel): # Pydantic
    id: int
    flightDate: date
    startingAirport: str
    destinationAirport: str
    isBasicEconomy: bool
    isRefundable: bool
    isNonStop: bool
    segmentsAirlineName: str
    totalFare: int

    class Config:
        from_attributes = True
        

class PredictSchema(BaseModel): # Pydantic
    startingAirport: str
    destinationAirport: str
    flightDate: date = "2022-04-21"
    isBasicEconomy: bool = True
    isRefundable: bool = True
    isNonStop: bool = True

    # class Config:
    #     from_attributes = True
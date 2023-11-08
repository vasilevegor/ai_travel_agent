from datetime import date
from pydantic import BaseModel


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
from ast import List
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from requests import Session as RequestsSession

from backend.ai import predict
from backend.ai.connect import get_mindsdb_session
from backend.env import config
from backend.db import schemas as db_schemas, utils as db_utils
from backend.db.connect import get_db_session, SessionLocal


DEBUG = config("DEBUG", cast=bool, default=False)
FRONTEND_ORIGINS = config("FRONTEND_ORIGINS", cast=lambda x: [s.strip() for s in x.split(",")], default="")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/hello-world')
def get_hello():
    return {
        'hello': 'world',
        "Debug": DEBUG,
    }
    
@app.get('/airports', response_model=list[db_schemas.AirportSchema])
def read_flight_prices(offset: int=0, limit: int=100, db_session: SessionLocal = Depends(get_db_session)):
    return db_utils.get_airports(db_session, offset=offset, limit=limit)


@app.get('/flights', response_model=list[db_schemas.FlightPriceOverviewSchema])
def read_flight_prices(offset: int=0, limit: int=100, db_session: SessionLocal = Depends(get_db_session)):
    return db_utils.get_flight_prices(db_session, offset=offset, limit=limit)


@app.get('/flights/{flight_price}', response_model=db_schemas.FlightPriceDetailSchema)
def read_flight_prices(flight_price: int, db_session: SessionLocal = Depends(get_db_session)):
    db_flight_value = db_utils.get_flight_price(db_session, flight_price)
    if db_flight_value is None:
        raise HTTPException(status_code=404, detail="Flight price not found")
    return db_flight_value


@app.post('/predict')
def write_to_predict(ai_session: RequestsSession = Depends(get_mindsdb_session)):
    predictions = predict.predict_query(
        ai_session,
        flightDate="2022-04-21", 
        startingAirport="LAX", 
        isNonStop=1, 
        destinationAirport="JFK",
        raw_request=False
    )
    return {
        "prediction": predictions,
    }
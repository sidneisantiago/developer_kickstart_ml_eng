#from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI()

class Data(BaseModel):
    housing_median_age : float
    total_rooms : float
    total_bedrooms : float
    population : float
    households : float
    median_income : float
    ocean_proximity : int

@app.get("/teste")
def rota_de_teste():
    return {"Status": "Ok"}


@app.post("/inference")
def inference(data: Data):
    list_data = list(data.model_dump().values())
    array_data = np.array(list_data)


    model = pickle.load(open('modelo_dataway.pkl', 'rb'))
    result = model.predict(array_data.reshape(1, -1))

    return result.tolist()
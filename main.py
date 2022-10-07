from typing import Union, TYPE_CHECKING, List

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from schemas import SwapIndexValue
from services import get_all_swaps, get_db


app = FastAPI(title='API Malonso',
              description = 'Esta es la API de Malonso, un loco vio pa la wea')

@app.get('/')
async def index():
      return 'No hay mucho que ver :/'
    

@app.post('/swaps', response_model = List[SwapIndexValue])
async def read_all_swaps(db: Session = Depends(get_db)):
        return await get_all_swaps(db=db)
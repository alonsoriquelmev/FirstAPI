from typing import Union, TYPE_CHECKING, List

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from services import get_all_swaps, get_db, swaps_by_id, swap_by_date, swap_by_date_range

import schemas
app = FastAPI(title='API Malonso',
              description = 'Esta es la API de Malonso, un loco vio pa la wea')

@app.get('/swaps', response_model = List[schemas.SwapIndexValue])
async def read_all_swaps(db: Session = Depends(get_db)):
        return await get_all_swaps(db=db)

    
@app.post('/swaps', response_model = List[schemas.SwapIndexValue])
async def swap_by_id(id_swap: schemas.Id, db: Session = Depends(get_db)):
        swap_by_id = await swaps_by_id(id_swap.id, db=db)
        return swap_by_id

@app.post('/swap/date/', response_model = List[schemas.SwapIndexValue])
async def get_swap_by_date(id_swap: schemas.Id, date: schemas.Date, db: Session = Depends(get_db)):
        get_swap_by_date = await swap_by_date(id_swap.id,date,db=db)
        return get_swap_by_date
    
@app.post('/swap/daterange/', response_model = List[schemas.SwapIndexValue])
async def get_swap_by_daterange(date_range: schemas.DateRange, db: Session = Depends(get_db)):
        get_swap_by_daterange = await swap_by_date_range(date_range, db=db)
        return get_swap_by_daterange

        




# @app.post('/fx_rate_index')
# @app.post('/forwards')
# @app.post('/interest_rate')


    

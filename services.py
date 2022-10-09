from typing import TYPE_CHECKING, List

import database 
import models 
import schemas
import fastapi
if TYPE_CHECKING:
    from sqlalchemy.orm import Session

    
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    except:
        db.close()
        
        

async def get_all_swaps(db: "Session") -> List[schemas.SwapIndexValue]:
        swaps = db.query(models.SwapIndexValue).all()
        return list(map(schemas.SwapIndexValue.from_orm,swaps))
    
    
async def swaps_by_id(swap_id: int, db: "Session") -> List[schemas.SwapIndexValue]:
        swap_by_id = db.query(models.SwapIndexValue).filter(models.SwapIndexValue.id_swap_index == swap_id)
        return list(map(schemas.SwapIndexValue.from_orm,swap_by_id))


async def swap_by_date(swap_id: int, date: schemas.Date, db: "Session") -> List[schemas.SwapIndexValue]:
         swap_by_date = db.query(models.SwapIndexValue).filter(models.SwapIndexValue.id_swap_index == swap_id, models.SwapIndexValue.swap_index_date == date.date_unique)
         return list(map(schemas.SwapIndexValue.from_orm,swap_by_date))
        
        
async def swap_by_date_range(date_range: schemas.DateRange, db:"Session") -> List[schemas.SwapIndexValue]:
    if (date_range.type_data == 'swap'):
            by_date_range = db.query(models.SwapIndexValue).filter(models.SwapIndexValue.id_swap_index == date_range.id, models.SwapIndexValue.swap_index_date >= date_range.date_ini,models.SwapIndexValue.swap_index_date <= date_range.date_end)
            return list(map(schemas.SwapIndexValue.from_orm,by_date_range))
    else:
        raise fastapi.HTTPException(status_code = 404, detail = 'No valido')
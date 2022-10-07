from typing import TYPE_CHECKING, List

import database 
import models 
import schemas

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
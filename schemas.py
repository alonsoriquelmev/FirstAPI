from pydantic import BaseModel
import datetime as dt


class SwapIndexValue(BaseModel):
        id: int    
        swap_index_date: dt.date
        id_swap_index: int
        id_quote_side: int
        value: float
        id_md_source: int
        effective_end_date: dt.date
        class Config:
            orm_mode = True
            
class DateRange(BaseModel):
        type_data: str
        id: int
        date_ini: dt.date
        date_end: dt.date
            
            
class Date(BaseModel):
        date_unique: dt.date

class Id(BaseModel):
        id: int
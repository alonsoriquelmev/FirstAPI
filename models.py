from sqlalchemy import BigInteger, String, Date, Integer
from sqlalchemy.sql.schema import Column
from database import Base
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION



class SwapIndexValue(Base):
        __tablename__ = 'swap_index_value'
        __table_args__ = {"schema": "test_datavalues"}
        
        id=Column(BigInteger,primary_key = True)
        swap_index_date=Column(Date, nullable = False)
        id_swap_index=Column(BigInteger)
        id_quote_side=Column(BigInteger)
        value=Column(DOUBLE_PRECISION())
        id_md_source= Column(Integer)
        effective_end_date=Column(Date, nullable = False)
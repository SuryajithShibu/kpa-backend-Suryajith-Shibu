from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base
from datetime import datetime

class BogieChecksheet(Base):
    __tablename__ = "bogie_checksheet"

    id = Column(Integer, primary_key=True, index=True)
    bogie_number = Column(String, nullable=False)
    inspector_name = Column(String, nullable=False)
    remarks = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

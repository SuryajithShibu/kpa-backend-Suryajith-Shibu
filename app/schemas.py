from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class BogieChecksheetBase(BaseModel):
    bogie_number: str
    inspector_name: str
    remarks: Optional[str] = None

class BogieChecksheetCreate(BogieChecksheetBase):
    pass

class BogieChecksheetResponse(BogieChecksheetBase):
    id: int
    created_at: datetime

    model_config = {
        "from_attributes": True  # ✅ Required for Pydantic v2
    }

from sqlalchemy.orm import Session

from .app import models
from .app import schemas

def create_bogie_checksheet(db: Session, form: schemas.BogieChecksheetCreate):
    bogie_form = models.BogieChecksheet(**form.dict())
    db.add(bogie_form)
    db.commit()
    db.refresh(bogie_form)
    return bogie_form

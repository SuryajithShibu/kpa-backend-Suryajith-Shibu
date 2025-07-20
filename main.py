from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from app import models, schemas, database
from app.database import get_db
from app.models import BogieChecksheet
from app.schemas import BogieChecksheetResponse

# ✅ Create DB tables on startup
models.Base.metadata.create_all(bind=database.engine)

# ✅ Initialize FastAPI app
app = FastAPI()

# ✅ Mount static folder (correct directory)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# ✅ Serve favicon.ico correctly from static directory
@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return FileResponse("app/static/favicon.ico")

# ✅ Optional: handle Apple touch icon fallback
@app.get("/apple-touch-icon.png", include_in_schema=False)
async def touch_icon_redirect():
    return RedirectResponse(url="/static/apple-touch-icon.png")

# ✅ POST endpoint to create a new bogie checksheet
@app.post("/bogie-checksheet/", response_model=BogieChecksheetResponse)
def create_bogie_checksheet(
    data: schemas.BogieChecksheetCreate,
    db: Session = Depends(get_db)
):
    new_entry = BogieChecksheet(**data.dict())
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry

# ✅ GET endpoint to list all bogie checksheets
@app.get("/bogie-checksheet/", response_model=list[BogieChecksheetResponse])
def list_bogie_checksheets(db: Session = Depends(get_db)):
    return db.query(BogieChecksheet).all()

# ✅ GET endpoint for a specific checksheet by ID
@app.get("/bogie-checksheet/{id}", response_model=BogieChecksheetResponse)
def get_bogie_checksheet(id: int, db: Session = Depends(get_db)):
    db_checksheet = db.query(BogieChecksheet).filter(BogieChecksheet.id == id).first()
    if not db_checksheet:
        raise HTTPException(status_code=404, detail="Checksheet not found")
    return db_checksheet

# ✅ Create Homepage
import os

@app.get("/", response_class=HTMLResponse)
def homepage():
    file_path = os.path.join("app", "static", "index.html")
    if not os.path.exists(file_path):
        return HTMLResponse(content="<h1>❌ index.html not found</h1>", status_code=404)
    with open(file_path, "r") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

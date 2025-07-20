from app.database import Base, engine
from app.models import BogieChecksheet

print("✅ Creating tables in PostgreSQL...")
Base.metadata.create_all(bind=engine)
print("✅ Done.")

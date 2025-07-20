from app.database import Base, engine
from app.models import BogieChecksheet

print("✅ Creating all tables...")

# Explicit reference to avoid 'unused import' warnings
_ = BogieChecksheet

Base.metadata.create_all(bind=engine)

print("✅ Tables created successfully!")

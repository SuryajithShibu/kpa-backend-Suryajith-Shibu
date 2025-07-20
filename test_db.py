# test_db.py
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    print("❌ DATABASE_URL not found in .env file")
else:
    try:
        engine = create_engine(DATABASE_URL)
        with engine.connect() as connection:
            print("✅ Connected to the database successfully!")
    except Exception as e:
        print("❌ Failed to connect to the database")
        print(e)


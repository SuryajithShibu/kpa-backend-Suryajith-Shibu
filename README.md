# kpa-backend-Suryajith-Shibu
# 🚆 KPA Backend

This is a FastAPI-based backend service for managing **Bogie Checksheet** data, developed as part of the KPA assignment. It includes a PostgreSQL database and a user-friendly HTML homepage.

---

## 🔧 Tech Stack

- **Backend:** FastAPI
- **Database:** PostgreSQL (via Docker)
- **ORM:** SQLAlchemy
- **Containerization:** Docker & Docker Compose
- **Frontend:** Basic HTML (static index page)

---

## 📁 Project Structure

kpa_backend/
├── app/
│ ├── main.py # FastAPI application
│ ├── models.py # SQLAlchemy DB models
│ ├── schemas.py # Pydantic schemas
│ ├── database.py # DB connection
│ └── static/
│ ├── index.html # Homepage
│ └── favicon.ico # App icon
├── requirements.txt # Python dependencies
├── Dockerfile # Image for FastAPI
├── docker-compose.yml # Compose with PostgreSQL
└── README.md

---

## 🚀 Features

- ✅ Create & view bogie checksheets via REST APIs
- ✅ Automatic DB table creation
- ✅ Clean homepage at `/`
- ✅ API documentation available at `/docs`
- ✅ Favicon and static files supported
- ✅ Fully Dockerized (PostgreSQL + FastAPI)

---

## 🧪 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/bogie-checksheet/` | Create new checksheet |
| `GET`  | `/bogie-checksheet/` | List all checksheets |
| `GET`  | `/bogie-checksheet/{id}` | Get a checksheet by ID |
| `GET`  | `/` | Static HTML homepage |
| `GET`  | `/docs` | Swagger UI |
| `GET`  | `/favicon.ico` | Serve favicon |

---

## 🐳 Run via Docker Compose

```bash
docker-compose up --build

Access:
App: http://localhost:8000
Swagger Docs: http://localhost:8000/docs

👨‍💻 Developer

Name: Suryajith Shibu
GitHub: @SuryajithShibu

📃 License

This project is for educational purposes only.

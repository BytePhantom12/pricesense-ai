# PriceSense AI Backend

Production-ready FastAPI backend scaffold for the PriceSense AI dynamic pricing and revenue optimisation platform.

## Stack

- FastAPI
- SQLAlchemy 2.0
- Alembic
- PostgreSQL
- Pydantic v2
- JWT authentication
- python-dotenv
- Joblib placeholder for future ML integration

## Project Structure

- `app/main.py`
- `app/database.py`
- `app/config.py`
- `app/models/`
- `app/schemas/`
- `app/routers/`
- `app/services/`
- `app/repositories/`
- `app/auth/`
- `app/middleware/`
- `app/utils/`

## Environment

Copy `.env.example` to `.env` and set:

- `DATABASE_URL`
- `SECRET_KEY`
- `ALGORITHM`
- `ACCESS_TOKEN_EXPIRE_MINUTES`

## Run

1. Create and activate a Python environment.
2. Install dependencies from `requirements.txt`.
3. Create the PostgreSQL database.
4. Run Alembic migrations when you add them.
5. Start the app from the `backend` directory:

```bash
uvicorn app.main:app --reload
```

## API Surface

- `POST /api/v1/auth/register`
- `POST /api/v1/auth/login`
- `GET /api/v1/auth/me`
- `GET /api/v1/users`
- `GET /api/v1/products`
- `GET /api/v1/transactions`
- `GET /api/v1/predictions`

Swagger UI is available automatically at `/docs`.

## Notes

- Business logic lives in services, not routers.
- Database access stays in repositories.
- ML inference is intentionally not implemented yet.

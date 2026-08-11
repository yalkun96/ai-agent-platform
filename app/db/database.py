from app.core.config import settings
from sqlachemy import create_engine, sessionmaker

DATABASE_URL = (
    f"postgresql+psycopg://"
    f"{settings.db_user}:{settings.db_password}"
    f"@{settings.db_host}:{settings.db_port}"
    f"/{settings.db_name}"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(engine)

db = SessionLocal()
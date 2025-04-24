from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root@localhost/aperwan"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Pour dépendance FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

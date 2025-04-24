import os

class Settings:
    PROJECT_NAME: str = "Aperwan API"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "mysql+pymysql://root@localhost/aperwan")

settings = Settings()

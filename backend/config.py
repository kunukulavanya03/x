class Config:
    SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost:5432/database"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "secret"

config = Config()
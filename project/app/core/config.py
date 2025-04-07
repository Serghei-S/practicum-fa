import os
from dotenv import load_dotenv

load_dotenv()  # загрузка переменных из .env

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
JWT_SECRET = os.getenv("JWT_SECRET", "your_jwt_secret")
JWT_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

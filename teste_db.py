# test_db.py
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

# carrega .env
load_dotenv()

# lê a URL do .env
DATABASE_URL = os.getenv('DATABASE_URL')
if not DATABASE_URL:
    raise RuntimeError("Não achei a variável DATABASE_URL no .env")

# cria engine SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)

# executa SELECT 1
with engine.connect() as conn:
    result = conn.execute(text("SELECT 1"))
    print("Conexão OK:", result.scalar())

# drop_schema.py
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

# carrega .env
load_dotenv()

# monta engine usando DATABASE_URL do seu .env (com porta 54327)
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL não encontrada no .env")
engine = create_engine(DATABASE_URL)

# apaga e recria o schema público
with engine.begin() as conn:
    conn.execute(text("DROP SCHEMA public CASCADE"))
    conn.execute(text("CREATE SCHEMA public"))

print("Schema público limpo e recriado com sucesso!")

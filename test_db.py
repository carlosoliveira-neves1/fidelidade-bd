# test_db.py
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

# carrega variáveis do .env
load_dotenv()

# pega a URL do banco
DATABASE_URL = os.getenv('DATABASE_URL')
if not DATABASE_URL:
    raise RuntimeError("Não encontrei variável DATABASE_URL no .env")

# cria engine e testa um SELECT simples
engine = create_engine(DATABASE_URL, echo=True)
with engine.connect() as conn:
    result = conn.execute(text("SELECT 1"))
    print("Conexão OK:", result.scalar())

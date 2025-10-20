from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

params = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
}

def conectar():
    try:
        conexao = psycopg2.connect(**params)
        print(" Conexão bem-sucedida com o banco de dados!")
        return conexao
    except Exception as erro:
        print(" Erro ao conectar:", erro)

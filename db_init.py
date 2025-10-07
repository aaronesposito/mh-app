import psycopg2
from dotenv import load_dotenv
import os

def initialize_conn():

    load_dotenv()

    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST", "http://localhost:5432")
    DB_PORT = os.getenv("DB_PORT", "5432")

    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

    return conn

def initialize_database():

    conn = initialize_conn()
    cur = conn.cursor()
    cur.execute(
        '''
        CREATE TABLE IF NOT EXISTS "day" (
            "date" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            "mood" INTEGER NOT NULL,
            "sleep" REAL NOT NULL,
            "note" TEXT NOT NULL DEFAULT ' ',
            "focus" INTEGER NOT NULL DEFAULT 0
        );
        '''
    )

    cur.execute(
        '''        
        CREATE TABLE IF NOT EXISTS "journals" (
            "created_on" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            "entry" TEXT NOT NULL,
            "title" TEXT
        );
        '''
    )
    conn.commit()
    cur.close()
    conn.close()


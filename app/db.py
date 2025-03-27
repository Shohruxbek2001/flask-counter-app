import psycopg2
import os

DB_PARAMS = {
    "dbname": os.getenv("POSTGRES_DB"),
    "user": os.getenv("POSTGRES_USER"),
    "password": os.getenv("POSTGRES_PASSWORD"),
    "host": os.getenv("POSTGRES_HOST"),
    "port": os.getenv("POSTGRES_PORT"),
}

conn = psycopg2.connect(**DB_PARAMS)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS counter (
    id SERIAL PRIMARY KEY,
    datetime TEXT NOT NULL,
    client_info TEXT NOT NULL
);
""")

conn.commit()
cursor.close()
conn.close()

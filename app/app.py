from flask import Flask, request, jsonify
from datetime import datetime
import psycopg2
import os

app = Flask(__name__)

DB_PARAMS = {
    "dbname": os.getenv("POSTGRES_DB"),
    "user": os.getenv("POSTGRES_USER"),
    "password": os.getenv("POSTGRES_PASSWORD"),
    "host": os.getenv("POSTGRES_HOST"),
    "port": os.getenv("POSTGRES_PORT"),
}

def get_db_connection():
    return psycopg2.connect(**DB_PARAMS)

@app.route('/count', methods=['POST'])
def count_request():
    user_agent = request.headers.get('User-Agent', 'Unknown')
    timestamp = datetime.now().strftime("%d/%b/%Y %H:%M:%S")
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO counter (datetime, client_info) VALUES (%s, %s) RETURNING id;",
        (timestamp, user_agent)
    )
    counter_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"id": counter_id, "datetime": timestamp, "client_info": user_agent})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
